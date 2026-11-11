import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.transforms import (ROOT, inverse, load_transform, multiply,
                              transform_point, validate_matrix, world_mount_pose)

IDENTITY = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


class TransformTests(unittest.TestCase):
    def setUp(self):
        self.vive = load_transform('vive-tracker', allow_unvalidated=True)['matrix']

    def assertMatrixClose(self, a, b, places=10):
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(a[i][j], b[i][j], places=places)

    def test_tracker_origin_is_mount_translation_in_metres(self):
        self.assertEqual(transform_point(self.vive, [0,0,0]), [-0.0105, 0.0, 0.0175])

    def test_axis_mapping_includes_translation(self):
        self.assertEqual(transform_point(self.vive, [1,0,0]), [-0.0105, 1.0, 0.0175])
        self.assertEqual(transform_point(self.vive, [0,1,0]), [-1.0105, 0.0, 0.0175])

    def test_world_pose_uses_inverse_on_the_right(self):
        # R_x(90 deg), translation (1,2,3): deliberately noncommuting with R_z.
        world_tracker = [[1,0,0,1],[0,0,-1,2],[0,1,0,3],[0,0,0,1]]
        expected = [[0,1,0,1],[0,0,-1,2.0175],[-1,0,0,2.9895],[0,0,0,1]]
        self.assertMatrixClose(world_mount_pose(world_tracker, self.vive), expected)

    def test_all_rounded_source_matrices_round_trip(self):
        for p in json.loads((ROOT / 'catalog/products.json').read_text())['products']:
            with self.subTest(product=p['id']):
                matrix = load_transform(p['id'], allow_unvalidated=True)['matrix']
                inv = inverse(matrix)
                self.assertMatrixClose(multiply(matrix, inv), IDENTITY)
                self.assertMatrixClose(multiply(inv, matrix), IDENTITY)

    def test_ultimate_keeps_negative_z_offset(self):
        matrix = load_transform('vive-ultimate-tracker', allow_unvalidated=True)['matrix']
        for actual, expected in zip(transform_point(matrix, [0,0,0]), [-0.0206, 0.0, -0.0191]):
            self.assertAlmostEqual(actual, expected, places=12)

    def test_draft_requires_explicit_acknowledgement(self):
        with self.assertRaisesRegex(ValueError, 'unvalidated'):
            load_transform('vive-tracker')

    def test_left_hand_is_never_inferred(self):
        with self.assertRaisesRegex(ValueError, 'No left-hand'):
            load_transform('vive-tracker', side='left', allow_unvalidated=True)

    def test_unknown_product_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unknown product'):
            load_transform('../vive-tracker', allow_unvalidated=True)

    def test_nonrigid_and_malformed_inputs_rejected(self):
        reflection = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        scale = [[2,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        invalid = [[[1]], reflection, scale]
        for value in (float('nan'), float('inf'), True, '1'):
            bad = copy.deepcopy(IDENTITY)
            bad[0][3] = value
            invalid.append(bad)
        bad_last = copy.deepcopy(IDENTITY)
        bad_last[3][0] = 0.1
        invalid.append(bad_last)
        for matrix in invalid:
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                validate_matrix(matrix)

    def test_nonfinite_point_rejected(self):
        with self.assertRaises(ValueError):
            transform_point(self.vive, [float('nan'), 0, 0])

    def test_cli_from_another_working_directory(self):
        script = ROOT / 'examples/transform_pose.py'
        result = subprocess.run([sys.executable, str(script), '--product', 'vive-tracker',
                                 '--point', '0', '0', '0', '--allow-unvalidated'],
                                cwd=ROOT.parent, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['point_in_mount'], [-0.0105,0,0.0175])

    def test_cli_rejects_draft_without_flag(self):
        result = subprocess.run([sys.executable, str(ROOT / 'examples/transform_pose.py'),
                                 '--product', 'vive-tracker', '--point', '0', '0', '0'],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('unvalidated', result.stderr)


if __name__ == '__main__':
    unittest.main()
