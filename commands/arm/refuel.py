from subsystems.arm import Arm
from ultime.command import Command

class Refuel(Command):

    def __init__(self, arm: Arm):
        super().__init__()
        self.arm = arm
        self.addRequirements(self.arm)


    def execute(self):
        self.arm.move_down()

    def isFinished(self) -> bool:
        return self.arm.is_switch_min_pressed()

    def end(self, interrupted: bool):
        self.arm.stop()

