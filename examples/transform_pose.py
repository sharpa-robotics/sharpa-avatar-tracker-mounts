"""Offline point / pose conversion. No device I/O or robot commands."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.transforms import load_transform, transform_point, world_mount_pose


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--product', required=True)
    parser.add_argument('--side', choices=['left', 'right'], default='right')
    parser.add_argument('--allow-unvalidated', action='store_true')
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument('--point', nargs=3, type=float, metavar=('X', 'Y', 'Z'),
                           help='Tracker-frame point, in metres')
    operation.add_argument('--world-tracker', type=Path,
                           help='JSON 4x4 T_world_tracker array, translations in metres')
    args = parser.parse_args()
    try:
        data = load_transform(args.product, args.side, args.allow_unvalidated)
        result = dict(product=args.product, side=args.side,
                      calibration_status=data['status'], translation_unit='m')
        if args.point is not None:
            result['point_in_mount'] = transform_point(data['matrix'], args.point)
        else:
            world_tracker = json.loads(args.world_tracker.read_text(encoding='utf-8'))
            result['T_world_mount'] = world_mount_pose(world_tracker, data['matrix'])
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    main()
