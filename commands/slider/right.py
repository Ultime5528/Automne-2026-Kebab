import wpilib
from ultime.command import Command
from subsystems.slider import Slider
from ultime.autoproperty import autoproperty


class SlideRight(Command):

    def __init__(self, slider: Slider):
        super().__init__()
        self.slider = slider
        self.addRequirements(self.slider)


    def execute(self):
        self.slider.slide_right()


    def end(self, interrupted: bool):
        self.slider.stop()
