from subsystems.arm import Arm
from ultime.command import Command

class Move_down(Command):

    def __init__(self, arm: Arm):
        super().__init__()
        self.arm = arm
        self.addRequirements(self.arm)


    def execute(self):
        self.arm.move_down()

    def isFinished(self) -> bool:
        return self.arm.is_down()

    def end(self, interrupted: bool):
        self.arm.stop()

