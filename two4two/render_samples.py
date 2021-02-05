import bpy
import json
import uuid
import numpy as np
import os, sys

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

from two4two.scene_parameters import SceneParameters
from two4two.data_generator import DataGenerator

def render(param_file, save_location):
    with open(param_file) as fparam:
        for line in fparam.readlines():
            params = SceneParameters(**json.loads(line))
            scene = DataGenerator(params)
            render_name = os.path.join(save_location, params.filename)
            scene.render(render_name)

if __name__ == '__main__':
    render(sys.argv[-2], sys.argv[-1])