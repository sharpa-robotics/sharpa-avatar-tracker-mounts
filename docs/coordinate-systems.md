# Coordinate systems and transforms

[Home](../README.md) · [Validation](validation.md)

## Contract

We use homogeneous **column vectors**. `T_A_B` maps coordinates expressed in B into A:

```text
p_A = T_A_B @ p_B
T_A_B = [ R_A_B  t_A_B ]
        [   0       1  ]
```

For every file in `transforms/`, A is `right_hand_mount_frame` and B is the right tracker/controller frame in the source calibration table. The matrix is named `T_mount_tracker`; it is not the inverse and is not a world alignment transform.

| Frame / convention | Definition and evidence status |
|---|---|
| `right_hand_mount_frame` | The source coordinate drawing locates the origin at the midpoint of an edge on the interface bottom face, with axes parallel to `right_hand_virtual_base_frame`. The corresponding hardware revision must be confirmed. |
| Current manual interface origin | The current manual marks `*` at the midpoint of an upper edge in its mechanical interface drawing. This view and the earlier coordinate drawing have not been shown to be the same hardware revision. Do not combine their dimensions without review. |
| Tracker frame | Physical/reference frame used by the source calibration. VIVE 3.0 references the vendor developer guideline; Ultimate references the vendor SDK. PICO and Meta runtime pose names are unspecified. |
| Axis interpretation | In `R_mount_tracker`, each column is one positive tracker basis axis expressed in mount coordinates. This gives an exact mathematical axis definition, even where a physical assembly axis illustration is still required. |
| Length | CAD is mm. Runtime JSON `matrix` translations are m. `source_matrix` preserves the source numeric translations interpreted as mm. |
| Handedness | The supplied rotation matrices are consistent with proper right-handed rotations within source rounding. That check cannot identify a runtime's actual coordinate convention. |
| Hands | All five source matrices are explicitly right-hand. Left-hand transforms are unavailable. |

**Unit evidence:** the VIVE derivation explicitly uses millimetres; all checked STEP files declare millimetres. The newer multi-device table does not explicitly label a unit for each translation column. This draft interprets the five rows consistently as mm, converts only the top three entries of the last column by 1/1000, and marks the result unvalidated until the calibration owner confirms the units for every product. Rotations and the last row are never scaled.

The source rotations are rounded decimals. They are preserved without silently orthonormalizing them. The offline helper uses a matrix inverse so round-trip tests do not introduce the additional transpose approximation.

## Points versus poses

For a point measured in the tracker frame:

```text
p_mount = T_mount_tracker @ p_tracker
```

For a runtime reporting the tracker pose in world coordinates:

```text
T_world_mount = T_world_tracker @ inverse(T_mount_tracker)
```

An offline pose example is included. It uses a synthetic tracker pose at `(1, 2, 3)` m with a 90-degree rotation about world X; it is not captured device data:

```console
python examples/transform_pose.py --product vive-tracker --world-tracker examples/world-tracker-pose.json --allow-unvalidated
```

The resulting mount translation is `(1, 2.0175, 2.9895)` m. The output contains the full `T_world_mount` matrix.

If the runtime reports another frame (for example `grip`), first construct `T_world_tracker = T_world_grip @ T_grip_tracker`. Neither that extra transform nor world-to-robot registration is supplied by this repository. Timestamp alignment and tracking-valid handling belong to the integrating application.

Example: the VIVE tracker origin maps to `[-10.5, 0, 17.5]` mm in the mount frame. A tracker point `[1, 0, 0]` m maps to `[-0.0105, 1, 0.0175]` m. This is a convention check, not a physical measurement.

## Source matrices

The following matrices reproduce the source table numerically. **Translations below are interpreted as mm; JSON `matrix` values use m.** All are unvalidated. A matrix's existence does not prove that it matches the downloaded adapter revision.

<a id="vive-tracker"></a>

### VIVE Tracker 3.0

```text
[ 0  -1  0  -10.5 ]
[ 1  0  0  0 ]
[ 0  0  1  17.5 ]
[ 0  0  0  1 ]
```

[JSON in metres](../transforms/vive-tracker/right.json) · [Product / assembly scope](../products/vive-tracker/README.md)

<a id="vive-ultimate-tracker"></a>

### VIVE Ultimate Tracker

```text
[ -1  0  0  -20.6 ]
[ 0  -1  0  0 ]
[ 0  0  1  -19.1 ]
[ 0  0  0  1 ]
```

[JSON in metres](../transforms/vive-ultimate-tracker/right.json) · [Product / assembly scope](../products/vive-ultimate-tracker/README.md)

<a id="pico-controller"></a>

### PICO controller

```text
[ -0.99871  0.050223  0.0069817  -8.0421 ]
[ 0.0037749  0.21095  -0.97749  15.278 ]
[ -0.050566  -0.97621  -0.21087  -59.188 ]
[ 0  0  0  1 ]
```

[JSON in metres](../transforms/pico-controller/right.json) · [Product / assembly scope](../products/pico-controller/README.md)

<a id="meta-touch-plus"></a>

### Meta Quest 3 / Touch Plus

```text
[ -0.98798  -0.085132  0.12907  -24.981 ]
[ -0.1244  -0.05803  -0.99053  46.203 ]
[ 0.091816  -0.99468  0.046742  -38.765 ]
[ 0  0  0  1 ]
```

[JSON in metres](../transforms/meta-touch-plus/right.json) · [Product / assembly scope](../products/meta-touch-plus/README.md)

<a id="meta-touch-pro"></a>

### Meta Quest Touch Pro

```text
[ -0.99205  -0.069042  0.10526  -23.086 ]
[ -0.098608  -0.093511  -0.99072  48.502 ]
[ 0.078244  -0.99322  0.085959  -37.87 ]
[ 0  0  0  1 ]
```

[JSON in metres](../transforms/meta-touch-pro/right.json) · [Product / assembly scope](../products/meta-touch-pro/README.md)

## Promoting a calibration

Confirm the runtime pose origin/axes, translation unit, hand, exact controller model, adapter CAD hash, glove hardware revision and mounting orientation. Record the tested positions/rotations, residuals, measurement reference and acceptance limits. Add the evidence and reviewer/date before changing `status` or `hardware_verified`. Left-hand support requires a separate measured or explicitly documented calibration, not a sign flip of the right-hand matrix.

The source snapshot was “多种tracker坐标系与hand mount坐标系的转换矩阵”, revision 390. Internal URLs and message-level provenance are held with the local review materials, outside the prospective public repository.
