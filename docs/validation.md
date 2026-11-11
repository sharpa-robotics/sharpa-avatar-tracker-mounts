# Validation and release review

The current state is `public-preview`; see [release-status.json](../release-status.json).

## What the automated checks mean

| Check | Scope |
|---|---|
| Asset integrity | Every catalog file exists and matches its stored byte count / SHA-256. |
| STEP envelope | Text header, closing marker and millimetre length declaration are present. This is not a CAD-kernel solid check. |
| Matrices | Numeric 4×4 shape, finite values, homogeneous last row, approximate orthogonality / determinant, source-to-metre consistency. |
| Example behavior | Known point mappings, noncommuting world-pose composition, inverse round trips and rejection of unacknowledged drafts. |
| Documentation | Local Markdown file targets resolve. Remote link availability can change. |

## Hardware work remaining

- Confirm exact PICO model and Avatar interface revision.
- Resolve the Quest 3 / Touch Pro mixed source rows and identify complete assembly sets.
- Confirm screw specifications, cover/fixture roles, hook-and-loop placement and retention.
- Print and fit each advertised assembly, including the Ultimate mounting base and orientation.
- Confirm translation units, runtime tracker pose reference and calibration-to-CAD revision binding for each matrix.
- Supply left-hand matrices or explicitly release those assemblies without calibrated left-hand support.
- Supply approved installation and coordinate drawings suitable for public distribution.

For each tested assembly, record: product, hardware revision, hand, CAD hashes, printed material/process, fasteners, photos/drawing, runtime/API frame, coordinate convention, measurement method, translation/rotation residuals, acceptance limits, result, reviewer and date. No numerical acceptance limits are invented here.

## Work remaining before a validated release

Confirm the copyright holder and license coverage, replace the pending [LICENSE](../LICENSE) with the approved text, inspect STEP metadata / embedded third-party geometry, and approve the final release content. Then run the local validation commands and have the hardware owner review the evidence.

The source documents report intended support and supplied models, but do not contain complete acceptance records. Therefore no device is labelled hardware-verified in this snapshot.
