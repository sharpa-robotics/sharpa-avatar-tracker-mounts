# Contributing

Use a product directory for each confirmed tracker/controller model. Preserve the distinction between main-hand, robot-arm and retention parts. Avoid silently reassigning a file to another controller generation.

For a CAD update, add the STEP file, state the hardware revision and hand, and update `catalog/assets.json` with the exact byte count and SHA-256. Keep STEP units in mm. Add the file to the product metadata and download tables. Record the hardware validation evidence.

For a calibration update, preserve its source numeric matrix and document frame direction, vector convention, units, runtime pose reference, hand, assembly orientation and CAD revision. Runtime JSON translations use m. Never label a matrix verified solely because the numerical checks pass.

Before review, run:

```console
python tools/validate_repository.py
python -m unittest discover -s tests -v
```

Private chat logs, authentication data and internal-only review materials do not belong in pull requests. Contact [support](SUPPORT.md) for questions about unpublished source material.
