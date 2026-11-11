# VIVE Tracker 3.0

[All products](../../README.md) · [File catalog](../../CATALOG.md) · [Support](../../SUPPORT.md)

**Status:** review draft; physical fit and calibration are not yet verified in this repository.

**Hardware scope:** Tracker 3.0; other VIVE generations not verified.

## Use and connect

Use the [STEP adapter](cad/vive-mount.step). The source discussion calls for a 1/4-20 camera screw; screw length and torque are pending confirmation. Verify the Avatar interface revision before fitting the adapter.

The source derivation places the VIVE tracking origin 0.5 mm from the mounting plane. It uses a 10 mm adapter height and 17.5 mm offset. These dimensions explain the supplied transform but do not certify fit for a different hardware revision.

For tracking, set up the compatible SteamVR base stations and receiver using the [VIVE Tracker documentation](https://developer.vive.com/us/hardware/tracker3/). Confirm the reported pose frame against the developer guideline before using the calibration. This guide covers the 3.0 reference; compatibility with other VIVE Tracker generations is unverified.

Follow the [common assembly and data workflow](../../docs/installation.md) for unit checks, retention testing and pose-stream integration.

## Files

| Part | Hand | File |
|---|---|---|
| Tracker adapter | shared | [vive-mount.step](cad/vive-mount.step) |

STEP files use mm. Available files do not establish printability or compatibility with a different glove revision.

## Coordinate transform

[Right-hand JSON](../../transforms/vive-tracker/right.json) · [Definitions, matrix and equations](../../docs/coordinate-systems.md#vive-tracker)

The matrix maps points from this device's right tracker frame to `right_hand_mount_frame`, using column vectors. JSON translations use metres. Its source numbers are preserved separately with a provisional mm interpretation. The source does not provide a verified runtime pose reference or a calibration-to-CAD revision binding.

No left-hand transform is supplied. Left-hand CAD must not be used with the right-hand matrix by assumption.

```console
python examples/transform_pose.py --product vive-tracker --point 0 0 0 --allow-unvalidated
```

Run the command from the repository root. It is an offline calculation, not a device connection test.
