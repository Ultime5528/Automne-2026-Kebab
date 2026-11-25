from subsystems.arm import Arm
from ultime.command import Command


class Move_up(Command):

    def __init__(self, arm: Arm):
        super().__init__()
        self.arm = arm
        self.addRequirements(self.arm)


    def execute(self):
        if self.arm.get_position() > 1:
            self.arm.move_up()
        elif self.arm.get_position() <= 1:
            self.arm.slow_move_up()

    def isFinished(self) -> bool:
        return self.arm.is_up()

    def end(self, interrupted: bool):
        self.arm.maintain()

