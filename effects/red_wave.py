import numpy as np
import time
import math
import sys
import os
# add parent directory to path so I can import my scripts from a subfolder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mathutils import *
import tree_sim

class RedWave(tree_sim.Simulation):
    def __init__(self):
        super().__init__()
        self.current_z = 0
        self.current_dir = 1

    def update(self):
        self.current_z += 0.1 * self.current_dir
        if self.current_z > self.height:
            self.current_dir = -1
        if self.current_z < 0:
            self.current_dir = 1
        for i in range(self.num_points):
            new_color = [255, 0, 0]
            new_color[0] = lerp(0, 255, 1 - normalize(clamp(abs(self.points[i][2] - self.current_z), 0, self.height/2), 0, self.height/2))
            self.colors[i] = new_color  # Update specific point's color

        self.update_colors()

lights = RedWave()
while True:
    lights.update()
    time.sleep(0.1)  # Pause for a short time to visualize changes