from commands2 import SequentialCommandGroup

from commands.claw.grab import Grab
from commands.arm.move_down import MoveDown
from subsystems.claw import Claw
from subsystems.arm import Arm

class Refuel(SequentialCommandGroup):

    def __init__(self, claw: Claw, arm: Arm):
        super().__init__(
            MoveDown(arm),
            Grab(claw),
        )
