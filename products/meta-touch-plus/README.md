# Meta Quest 3 / Touch Plus

[All products](../../README.md) · [File catalog](../../CATALOG.md) · [Support](../../SUPPORT.md)

**Status:** review draft; physical fit and calibration are not yet verified in this repository.

**Hardware scope:** Quest 3 Touch Plus; mounting set / handedness of fixture unresolved.

## Use and connect

Only the explicitly named [Quest 3 fixture STEP](cad/quest3-fixture.step) is assigned here. The source row named “Meta quest 3” also contained Touch Pro adapters; those are catalogued under [Touch Pro](../meta-touch-pro/README.md). They have not been asserted to be interchangeable.

The source does not specify whether this fixture is left, right or shared, or which additional parts form a complete assembly. Confirm the full part set, retention and glove revision before manufacturing. The draft Touch Plus matrix cannot be tied to this fixture revision from the available evidence alone.

[Meta's hardware-art catalog](https://developers.meta.com/vr/downloads/package/oculus-controller-art/) distinguishes Touch Plus (Quest 3) from Touch Pro. Pair the correct controllers with the headset and obtain poses through the chosen runtime. Confirm the tracking/aim/grip frame used by the calibration; it is not identified in the source table.

Follow the [common assembly and data workflow](../../docs/installation.md) for unit checks, retention testing and pose-stream integration.

## Files

| Part | Hand | File |
|---|---|---|
| Quest 3 fixture | unspecified | [quest3-fixture.step](cad/quest3-fixture.step) |

STEP files use mm. Available files do not establish printability or compatibility with a different glove revision.

## Coordinate transform

[Right-hand JSON](../../transforms/meta-touch-plus/right.json) · [Definitions, matrix and equations](../../docs/coordinate-systems.md#meta-touch-plus)

The matrix maps points from this device's right tracker frame to `right_hand_mount_frame`, using column vectors. JSON translations use metres. Its source numbers are preserved separately with a provisional mm interpretation. The source does not provide a verified runtime pose reference or a calibration-to-CAD revision binding.

No left-hand transform is supplied. Left-hand CAD must not be used with the right-hand matrix by assumption.

```console
python examples/transform_pose.py --product meta-touch-plus --point 0 0 0 --allow-unvalidated
```

Run the command from the repository root. It is an offline calculation, not a device connection test.
