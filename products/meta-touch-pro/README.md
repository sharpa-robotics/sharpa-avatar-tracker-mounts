# Meta Quest Touch Pro

[All products](../../README.md) · [File catalog](../../CATALOG.md) · [Support](../../SUPPORT.md)

**Status:** review draft; physical fit and calibration are not yet verified in this repository.

**Hardware scope:** Touch Pro; confirm exact assembly and glove revision.

## Use and connect

Select left/right **main-hand adapters** for glove-side integration, or the separately named **robot-arm adapters** for the corresponding robot-side assembly. Switch and right-hand switch-stop files are also provided. A released BOM and assembly drawing are not present in the collected sources.

STEP files exist for both sides of the main adapters and for the switch parts. The Touch Pro source row is used here.

Use the [Meta hardware-art catalog](https://developers.meta.com/vr/downloads/package/oculus-controller-art/) to distinguish Touch Pro from Touch Plus. Pair the controller through a compatible Meta headset/runtime, then confirm the pose frame used by the API. A controller's grip or aim pose is not necessarily the source matrix's “tracker” frame.

The source discussion reported insufficient hook-and-loop retention on a controller mount. Confirm the exact retention materials, orientation and revised geometry instead of assuming that the current CAD resolves that report.

Follow the [common assembly and data workflow](../../docs/installation.md) for unit checks, retention testing and pose-stream integration.

## Files

| Part | Hand | File |
|---|---|---|
| Main-hand adapter | left | [touch-pro-main-hand-adapter-left.step](cad/touch-pro-main-hand-adapter-left.step) |
| Robot-arm adapter | left | [touch-pro-robot-arm-adapter-left.step](cad/touch-pro-robot-arm-adapter-left.step) |
| Main-hand adapter | right | [touch-pro-main-hand-adapter-right.step](cad/touch-pro-main-hand-adapter-right.step) |
| Robot-arm adapter | right | [touch-pro-robot-arm-adapter-right.step](cad/touch-pro-robot-arm-adapter-right.step) |
| Switch part | unspecified | [touch-pro-switch.step](cad/touch-pro-switch.step) |
| Switch stop | right | [touch-pro-switch-stop-right.step](cad/touch-pro-switch-stop-right.step) |

STEP files use mm. Available files do not establish printability or compatibility with a different glove revision.

## Coordinate transform

[Right-hand JSON](../../transforms/meta-touch-pro/right.json) · [Definitions, matrix and equations](../../docs/coordinate-systems.md#meta-touch-pro)

The matrix maps points from this device's right tracker frame to `right_hand_mount_frame`, using column vectors. JSON translations use metres. Its source numbers are preserved separately with a provisional mm interpretation. The source does not provide a verified runtime pose reference or a calibration-to-CAD revision binding.

No left-hand transform is supplied. Left-hand CAD must not be used with the right-hand matrix by assumption.

```console
python examples/transform_pose.py --product meta-touch-pro --point 0 0 0 --allow-unvalidated
```

Run the command from the repository root. It is an offline calculation, not a device connection test.
