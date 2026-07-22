# Tools

This folder contains helper scripts for model processing and migration.

## convert_model_to_add_fingers.py

Convert a URDF generated with hand as a single rigid part to the
 hand structure by adding only the new finger links and joints.

The converter keeps the original model unchanged and writes a new URDF.

### Usage

From the `code` directory:

```bash
python tools/convert_model_to_add_fingers.py <input_model.urdf>
```

Optional arguments:

```bash
python tools/convert_model_to_add_fingers.py <input_model.urdf> -o <output_model.urdf> -t <template.urdf>
```

### Parameters

- `<input_model.urdf>`: source URDF to convert.
- `-o, --output`: output URDF path. Default is `<input_name>_fingers.urdf`.
- `-t, --template`: path to the v2 template URDF. If omitted, the script uses:
  `code/models/humanModelTemplate/humanModelTemplate.urdf`.

### Example

```bash
python tools/convert_model_to_add_fingers.py "C:/Dataset-Human/models/humanSubjectWithSpinalCordMeshes.urdf" -o "C:/Dataset-Human/models/humanSubjectWithSpinalCordMeshes_fingers.urdf"
```
