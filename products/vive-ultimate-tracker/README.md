# VIVE Ultimate Tracker

[All products](../../README.md) · [File catalog](../../CATALOG.md) · [Support](../../SUPPORT.md)

**Status:** review draft; physical fit and calibration are not yet verified in this repository.

**Hardware scope:** Ultimate Tracker with its mounting base.

## Use and connect

The source document states that this product uses the same [VIVE adapter STEP](../vive-tracker/cad/vive-mount.step), with the Ultimate mounting base included in the assembly.

**The mounting base is not keyed against reversed insertion.** Confirm the tracker/base installation orientation against the calibration owner's assembly reference before using the matrix. The source installation image is available to internal reviewers but has not been cleared as a public illustration. A hardware owner must supply an approved assembly image or drawing before a customer release.

Set up the dongle, pairing and environment map using the [official Linux SDK setup guide](https://github.com/ViveRoboticsSoftware/vive-ultimate-tracker-sdk/blob/main/VIVE-Ultimate-Tracker-SDK-Guide-EN.md). The [SDK coordinate convention](https://github.com/ViveRoboticsSoftware/vive-ultimate-tracker-sdk#coordinate-system) is right-handed, +X forward and +Z up. Confirm that the calibration's physical tracking frame and your SDK pose reference agree. Do not apply the VIVE 3.0 matrix to Ultimate.

Follow the [common assembly and data workflow](../../docs/installation.md) for unit checks, retention testing and pose-stream integration.

## Files

Use the shared VIVE files linked above.

STEP files use mm. Available files do not establish printability or compatibility with a different glove revision.

## Coordinate transform

[Right-hand JSON](../../transforms/vive-ultimate-tracker/right.json) · [Definitions, matrix and equations](../../docs/coordinate-systems.md#vive-ultimate-tracker)

The matrix maps points from this device's right tracker frame to `right_hand_mount_frame`, using column vectors. JSON translations use metres. Its source numbers are preserved separately with a provisional mm interpretation. The source does not provide a verified runtime pose reference or a calibration-to-CAD revision binding.

No left-hand transform is supplied. Left-hand CAD must not be used with the right-hand matrix by assumption.

```console
python examples/transform_pose.py --product vive-ultimate-tracker --point 0 0 0 --allow-unvalidated
```

Run the command from the repository root. It is an offline calculation, not a device connection test.
