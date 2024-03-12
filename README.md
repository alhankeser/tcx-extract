# TCX Extractor

A speed-optimized data extractor for .tcx (Garmin) files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Installation
Can be installed using: 

```bash
pip install tcx-extract
```

Then run this once to build the Zig executable:
```python
import tcx_extract as tcx
tcx.build_zig()
```

## Usage
```python
import tcx_extract as tcx
watts = tcx.extract(filepath="example.tcx", tag_name="ns3:Watts")
print(watts)

# Output:
# ['402', '380', '304'...]
```
- By default, an item for every `<TrackPoint>` will be included in the resulting Python list.
- `filepath` path to the .tcx file to extract from.
- `tag_name` tag to get value from. 
  - Nested or multiple tags are not currently supported.

## Support
Please [create an issue](https://github.com/alhankeser/tcx-extract/issues/new) if you're having an issue or have questions. 
