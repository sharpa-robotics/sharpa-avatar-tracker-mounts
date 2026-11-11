# Licensing review

The requirements request an open-source license but do not choose one. This draft contains the [standard MIT text](https://opensource.org/license/mit) as a concrete [candidate](../licenses/MIT.proposed.txt). It is not active; [LICENSE](../LICENSE) states the current status.

The owner should confirm the legal copyright holder, final license choice and which files it covers. In particular, confirm coverage for CAD hardware designs as well as documentation and helper scripts, and inspect any third-party geometry or metadata embedded in STEP files. No company legal name has been guessed.

Vendor device-body models and SDK packages are linked rather than redistributed. Their own license and attribution terms continue to apply. An upstream repository's license does not by itself license these project assets.

Once approved, replace the root LICENSE with the final complete text, update asset license statuses and `release-status.json`, and remove or resolve this candidate notice. The repository is a public preview; a final licensed release remains subject to owner review.
