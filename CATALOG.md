# File catalog

Review snapshot: 2026-11-10. STEP files use millimetres. This repository distributes models in STEP format only.

Click a filename to open it on GitHub, then use **Download raw file**. After downloading the repository ZIP, the same paths work locally.

File availability is separate from fit, manufacturing and calibration validation. See [validation status](docs/validation.md).

## VIVE Tracker 3.0

[Product guide](products/vive-tracker/README.md) · [Right-hand transform](transforms/vive-tracker/right.json)

| Part | Hand | Format | File | Size |
|---|---|---|---|---|
| Tracker adapter | shared | STEP | [vive-mount.step](products/vive-tracker/cad/vive-mount.step) | 368.4 KiB |

## VIVE Ultimate Tracker

[Product guide](products/vive-ultimate-tracker/README.md) · [Right-hand transform](transforms/vive-ultimate-tracker/right.json)

Uses the VIVE adapter listed above according to the source document. The Ultimate mounting base and orientation remain part of the assembly; the VIVE 3.0 transform does not apply.

## PICO controller

[Product guide](products/pico-controller/README.md) · [Right-hand transform](transforms/pico-controller/right.json)

| Part | Hand | Format | File | Size |
|---|---|---|---|---|
| Main-hand adapter | left | STEP | [pico-main-hand-adapter-left.step](products/pico-controller/cad/pico-main-hand-adapter-left.step) | 1523.9 KiB |
| Robot-arm adapter | left | STEP | [pico-robot-arm-adapter-left.step](products/pico-controller/cad/pico-robot-arm-adapter-left.step) | 1288.8 KiB |
| Cover | left | STEP | [pico-cover-left.step](products/pico-controller/cad/pico-cover-left.step) | 1551.2 KiB |
| Main-hand adapter | right | STEP | [pico-main-hand-adapter-right.step](products/pico-controller/cad/pico-main-hand-adapter-right.step) | 1597.4 KiB |
| Robot-arm adapter | right | STEP | [pico-robot-arm-adapter-right.step](products/pico-controller/cad/pico-robot-arm-adapter-right.step) | 1347.1 KiB |
| Cover | right | STEP | [pico-cover-right.step](products/pico-controller/cad/pico-cover-right.step) | 1617.6 KiB |

## Meta Quest 3 / Touch Plus

[Product guide](products/meta-touch-plus/README.md) · [Right-hand transform](transforms/meta-touch-plus/right.json)

| Part | Hand | Format | File | Size |
|---|---|---|---|---|
| Quest 3 fixture | unspecified | STEP | [quest3-fixture.step](products/meta-touch-plus/cad/quest3-fixture.step) | 304.5 KiB |

## Meta Quest Touch Pro

[Product guide](products/meta-touch-pro/README.md) · [Right-hand transform](transforms/meta-touch-pro/right.json)

| Part | Hand | Format | File | Size |
|---|---|---|---|---|
| Main-hand adapter | left | STEP | [touch-pro-main-hand-adapter-left.step](products/meta-touch-pro/cad/touch-pro-main-hand-adapter-left.step) | 4255.1 KiB |
| Robot-arm adapter | left | STEP | [touch-pro-robot-arm-adapter-left.step](products/meta-touch-pro/cad/touch-pro-robot-arm-adapter-left.step) | 7515.4 KiB |
| Main-hand adapter | right | STEP | [touch-pro-main-hand-adapter-right.step](products/meta-touch-pro/cad/touch-pro-main-hand-adapter-right.step) | 5324.1 KiB |
| Robot-arm adapter | right | STEP | [touch-pro-robot-arm-adapter-right.step](products/meta-touch-pro/cad/touch-pro-robot-arm-adapter-right.step) | 9465.6 KiB |
| Switch part | unspecified | STEP | [touch-pro-switch.step](products/meta-touch-pro/cad/touch-pro-switch.step) | 264.5 KiB |
| Switch stop | right | STEP | [touch-pro-switch-stop-right.step](products/meta-touch-pro/cad/touch-pro-switch-stop-right.step) | 210.6 KiB |

## Integrity

SHA-256 hashes and exact byte counts are in [catalog/assets.json](catalog/assets.json). Run `python tools/validate_repository.py` to check your local copy. This checks file integrity and STEP envelopes, not CAD solids or printability.
