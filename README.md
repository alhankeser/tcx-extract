# TCX Extractor

A speed-optimized data extractor for .tcx (Garmin) files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Installation
Can be installed using: 

```bash
pip install git+https://github.com/alhankeser/tcx-extract.git
```

Then run this once to build the Zig executable:
```python
import tcx_extract as tcx
tcx.build_zig()
```

## Usage
```python
import tcx_extract as tcx
print(tcx.extract("example.tcx", "Time"))
```

## Support
Please [create an issue](https://github.com/alhankeser/tcx-extract/issues/new) if you're having an issue or have questions. 
