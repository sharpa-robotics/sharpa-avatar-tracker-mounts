# Assembly and connection workflow

This is an integration checklist for the collected CAD, not a validated manufacturing instruction. Use each [product guide](../README.md#find-your-device) to select files.

## 1. Match the hardware

- Record the exact tracker/controller generation, left/right hand, Avatar hardware revision and selected CAD filenames.
- Confirm whether the part is a main-hand adapter, robot-arm adapter, cover or retention fixture. These are different roles; a robot-arm part is not a substitute for the glove adapter.
- The Quest 3 source row contained Touch Pro parts. File names have been separated, but interchangeable fit has not been established.

## 2. Prepare the mechanical parts

1. Open the STEP in a CAD application and confirm the millimetre length unit before exporting a print mesh.
2. Inspect the solid, mating surfaces and mounting features. No STL is supplied because tessellation tolerance, material, layer orientation, supports and fit allowance have not been approved.
3. Confirm the required hardware with the mechanical owner. The VIVE adapter discussion specifies a **1/4-20 camera screw**; the correct length and tightening torque are not documented. Other fasteners and retention details remain unconfirmed.
4. Print and dry-fit one assembly. Verify access to controls, clearance from moving glove parts and visibility of tracking surfaces/cameras.
5. Check retention by gentle manual loading in each direction. The source discussion reported a hook-and-loop retention issue for a controller adapter; it did not establish that all designs were corrected. Record the hook/loop placement and validated assembly revision.

## 3. Bring up the data streams

The glove and external tracker are separate data sources. Mounting a tracker on the glove does not by itself connect the tracker stream to the Avatar software.

1. Set up the glove using its matching Avatar user manual.
2. Pair/configure the external device with its vendor runtime, headset or receiver. See the device guide for the relevant official documentation.
3. Log the actual pose frame, axis convention, translation unit, timestamp and tracking-valid flag produced by that runtime. An OpenXR aim pose, grip pose and vendor tracking frame are not automatically identical.
4. Reconcile that frame with the source of the calibration before applying `T_mount_tracker`. Convert units once. If the runtime pose frame differs, an additional documented extrinsic transform is required.
5. Use the equations in [coordinate-systems.md](coordinate-systems.md) to compute the mount pose. This repository contains offline math examples; it does not implement a live acquisition driver or time synchronizer.

## 4. Check the assembly before integration

Test known static positions, rotations about each axis and reattachment repeatability. Record residual translation/angle errors against the application's acceptance limits. Check tracking loss and timestamp handling in the integrating application. The [validation record](validation.md) lists the information needed to promote a draft calibration.
