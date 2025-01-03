from effects.base_effect import LightEffect, ParamType
import random

class Sparkles(LightEffect):
    def __init__(self, pixels, coords):
        super().__init__(pixels, coords)
        self.color = self.add_parameter("Color", ParamType.COLOR, "#FF0000"),
        self.speed = self.add_parameter("Speed", "slider", 20, min=1, max=100, step=1)
        self.amount = self.add_parameter("Amount", "slider", 1, min=1, max=10, step=1)
        self.states = [0] * len(self.pixels)

    def update(self):
        off_lights = []
        for i in range(len(self.pixels)):
            if self.states[i] == 0:
                off_lights.append(i)
        # randomly select amount of lights to turn on
        for _ in range(int(self.amount.get())):
            if len(off_lights) < 50:
                break
            pick = random.choice(off_lights)
            self.states[pick] = 1
            off_lights.remove(pick)
        for i in range(len(self.pixels)):
            if self.states[i] > 0:
                self.states[i] -= self.speed.get() / 1000
            if self.states[i] < 0:
                self.states[i] = 0
            self.pixels[i] = [int(channel) * self.states[i] for channel in self.color[0].get()]
        self.pixels.show()    