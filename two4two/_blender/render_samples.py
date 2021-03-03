import json
import os
from pathlib import Path
import sys

import bpy

# the two4two package is not visible for the blender python.
# we therfore add the package directory to the path.
blend_dir = os.path.dirname(bpy.data.filepath)
package_base_dir = str(Path(__file__).parents[2])

if package_base_dir not in sys.path:
    sys.path.append(package_base_dir)

from two4two._blender.scene import Scene  # noqa: E402
from two4two.scene_parameters import SceneParameters  # noqa: E402


def _render_files(param_file: str, save_location: str):
    with open(param_file) as fparam:
        for line in fparam.readlines():
            params = SceneParameters.load(json.loads(line))
            scene = Scene(params)
            image_fname = os.path.join(save_location, params.filename)
            base, ext = os.path.splitext(image_fname)
            mask_fname = f"{base}_mask{ext}"
            scene.render(image_fname, mask_fname)


if __name__ == '__main__':
    _render_files(sys.argv[-2], sys.argv[-1])
