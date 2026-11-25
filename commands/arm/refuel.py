from commands2 import SequentialCommandGroup

from commands.claw.grab import Grab
from commands.arm.move_down import Move_down
from subsystems.claw import Claw
from subsystems.arm import Arm

class Drop(SequentialCommandGroup):

    def __init__(self, claw: Claw, arm: Arm):
        super().__init__(
            Move_down(arm),
            Grab(claw),
        )