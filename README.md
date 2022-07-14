# Bake All Shape Keys With CATS

A Blender plugin to bake any shape key in a mesh that has the `_bake` suffix (that is used by CATS).

Useful if you do not want to run CATS and only want to perform a bake.

**Requires CATS (latest development version for Blender 3.1 or later)**

## Usage

**I recommend you backup your project and copy your mesh before doing this**

Tested in Blender 3.1 with development version of CATS.

1. Import the plugin
2. Open the "Misc" panel
3. Select your mesh that has the shape keys
4. Click "Bake"

All shape keys that have `_bake` in their name will be removed and the Basis shape key will be updated.
