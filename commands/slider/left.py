import wpilib
from ultime.command import Command
from subsystems.slider import Slider
from ultime.autoproperty import autoproperty


class SlideLeft(Command):
    duration = autoproperty(0.5)

    def __init__(self, slider: Slider):
        super().__init__()
        self.slider = slider
        self.timer = wpilib.Timer()
        self.addRequirements(self.slider)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.slider.slide_left()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        self.slider.stop()
