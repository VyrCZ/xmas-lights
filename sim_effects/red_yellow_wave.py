import numpy as np
import time
import math
import sys
import os
# add parent directory to path so I can import my scripts from a subfolder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mathutils as mu
import tree_sim

class RedYellowWave(tree_sim.Simulation):
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
            # Example: Assign random color to each point
            new_color = [255, 0, 0]
            # new_color[1] -> Z position same as current_z = 0; Z distance from current_z same as height = 125
            new_color[1] = mu.lerp(0, 255, mu.normalize(mu.clamp(abs(self.points[i][2] - self.current_z), 0, self.height), 0, self.height))
            self.colors[i] = new_color  # Update specific point's color

        self.update_colors()

lights = RedYellowWave()
while True:
    lights.update()
    time.sleep(0.1)  # Pause for a short time to visualize changes