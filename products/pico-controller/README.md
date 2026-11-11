# PICO controller

[All products](../../README.md) · [File catalog](../../CATALOG.md) · [Support](../../SUPPORT.md)

**Status:** review draft; physical fit and calibration are not yet verified in this repository.

**Hardware scope:** Exact controller generation unresolved in source.

## Use and connect

The exact PICO controller generation is not recorded in the source. Confirm the device label with the mechanical owner before selecting the CAD; do not assume that the same files fit PICO 4, Neo3 or a body tracker.

The package contains left/right **main-hand adapters**, **robot-arm adapters** and **covers**, each in STEP format. Start with the main-hand adapter and matching cover for glove integration. The BOM, screw sizes, cover retention and assembly order require confirmation; a robot-arm adapter is a separate integration variant.

Pair the controller with its compatible headset/runtime and use the relevant [PICO input and tracking documentation](https://developer.picoxr.com/document/web/introduce-xr-hardware/). Log which pose reference your API returns. The source matrix is labelled only “pico”, without a runtime pose name, so the frame mapping must be confirmed before use.

Follow the [common assembly and data workflow](../../docs/installation.md) for unit checks, retention testing and pose-stream integration.

## Files

| Part | Hand | File |
|---|---|---|
| Main-hand adapter | left | [pico-main-hand-adapter-left.step](cad/pico-main-hand-adapter-left.step) |
| Robot-arm adapter | left | [pico-robot-arm-adapter-left.step](cad/pico-robot-arm-adapter-left.step) |
| Cover | left | [pico-cover-left.step](cad/pico-cover-left.step) |
| Main-hand adapter | right | [pico-main-hand-adapter-right.step](cad/pico-main-hand-adapter-right.step) |
| Robot-arm adapter | right | [pico-robot-arm-adapter-right.step](cad/pico-robot-arm-adapter-right.step) |
| Cover | right | [pico-cover-right.step](cad/pico-cover-right.step) |

STEP files use mm. Available files do not establish printability or compatibility with a different glove revision.

## Coordinate transform

[Right-hand JSON](../../transforms/pico-controller/right.json) · [Definitions, matrix and equations](../../docs/coordinate-systems.md#pico-controller)

The matrix maps points from this device's right tracker frame to `right_hand_mount_frame`, using column vectors. JSON translations use metres. Its source numbers are preserved separately with a provisional mm interpretation. The source does not provide a verified runtime pose reference or a calibration-to-CAD revision binding.

No left-hand transform is supplied. Left-hand CAD must not be used with the right-hand matrix by assumption.

```console
python examples/transform_pose.py --product pico-controller --point 0 0 0 --allow-unvalidated
```

Run the command from the repository root. It is an offline calculation, not a device connection test.
