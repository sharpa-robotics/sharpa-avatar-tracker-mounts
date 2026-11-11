# Sharpa Avatar Tracker Mounts

Mechanical adapters and coordinate transforms for integrating external trackers and VR controllers with the Sharpa Avatar hand mount.

[GitHub repository](https://github.com/sharpa-robotics/sharpa-avatar-tracker-mounts) · [中文说明](README.zh-CN.md) · [Download catalog](CATALOG.md) · [Coordinate conventions](docs/coordinate-systems.md) · [Support](SUPPORT.md)

**Public preview — hardware validation is pending.** The CAD files and five right-hand matrices were collected from the project sources on 2026-11-10. Physical fit, retention and pose accuracy have not been verified here. Left-hand CAD availability does not imply a left-hand calibration. Licensing is pending owner review; see [LICENSE](LICENSE).

## Find your device

| Device | Mechanical files and scope | Calibration |
|---|---|---|
| [VIVE Tracker 3.0](products/vive-tracker/README.md) | STEP available; fit test pending | [Right / draft](transforms/vive-tracker/right.json) |
| [VIVE Ultimate Tracker](products/vive-ultimate-tracker/README.md) | Shared VIVE adapter per source document; mounting orientation must be checked | [Right / draft](transforms/vive-ultimate-tracker/right.json) |
| [PICO controller](products/pico-controller/README.md) | Left/right main-hand, robot-arm adapters and covers; fit test pending | [Right / draft](transforms/pico-controller/right.json) |
| [Meta Quest 3 / Touch Plus](products/meta-touch-plus/README.md) | Quest 3 fixture only; complete assembly mapping pending | [Right / draft](transforms/meta-touch-plus/right.json) |
| [Meta Quest Touch Pro](products/meta-touch-pro/README.md) | Left/right main-hand and robot-arm adapters plus switch parts; fit test pending | [Right / draft](transforms/meta-touch-pro/right.json) |

There are **14 STEP files**. The first version covers tracker/controller adapters. URDF and robot models are outside this repository's initial scope.

## Quick start

1. Select your device above. Check the controller generation, hand and glove interface revision.
2. Download files from the [catalog](CATALOG.md), or use GitHub **Code → Download ZIP** from the repository page. Use STEP for neutral CAD interchange.
3. Follow the product guide and [assembly workflow](docs/installation.md). Confirm fit and retention before a motion test. Print settings, screw lengths and torques still require hardware-owner confirmation.
4. Read the [coordinate contract](docs/coordinate-systems.md). The JSON translation unit is **metres**; the source matrix translations are recorded separately as interpreted **millimetres**. Matrices map tracker coordinates into `right_hand_mount_frame`.
5. Run the offline example with Python 3.10 or later. There are no third-party Python dependencies:

```console
python examples/transform_pose.py --product vive-tracker --point 0 0 0 --allow-unvalidated
python tools/validate_repository.py
python -m unittest discover -s tests -v
```

The example returns `[-0.0105, 0.0, 0.0175]` metres for the VIVE tracker origin. `--allow-unvalidated` explicitly acknowledges the draft calibration; it does not mark any hardware verified.

## Repository layout

```text
products/<device>/       device guide, product metadata, cad/*.step
transforms/<device>/     right.json: frame names, units, matrix and source status
catalog/                machine-readable product list and asset hashes
docs/                   coordinates, assembly, validation, references and licensing
examples/               offline point / pose conversion example
tools/                  transform helpers and repository checker
tests/                  transform direction, units and inverse tests
.github/                issue template and validation workflow
LICENSE                 current license status
licenses/               proposed license text for review
```

All model paths are relative. Git LFS is not required for this snapshot. Preserve filenames and directory structure so catalog links and checksums remain valid.

## Contact and license

Hardware and integration support: **[support@sharpa.com](mailto:support@sharpa.com)**, as listed in the Avatar user manual. Include the device, hand, glove revision, CAD filename and observed issue; see [SUPPORT.md](SUPPORT.md).

An [MIT license candidate](licenses/MIT.proposed.txt) is included for owner review. It is **not an active license grant**. The final copyright holder, license choice and model coverage remain pending. Public visibility does not itself grant an open-source license. Vendor device models and SDKs remain under their own terms; this repository links to them in [references](docs/references.md).
