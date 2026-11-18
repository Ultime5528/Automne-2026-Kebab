import commands2
from wpilib import PowerDistribution

from subsystems.arm import Arm

from subsystems.claw import Claw
from ultime.module import Module
from ultime.subsystem import Subsystem
from subsystems.slider import Slider

class HardwareModule(Module):
    def __init__(self):
        super().__init__()
        self.subsystems: list[Subsystem] = []

        self.controller = commands2.button.CommandXboxController(0)
        self.panel_1 = commands2.button.CommandJoystick(1)
        self.panel_2 = commands2.button.CommandJoystick(2)

        self.pdp = PowerDistribution()

        self.arm = self.addSubsystem(Arm())
        self.slider = self.addSubsystem(Slider())
        self.claw = self.addSubsystem(Claw())

    def addSubsystem[T: Subsystem](self, subsystem: T) -> T:
        self.subsystems.append(subsystem)
        return subsystem