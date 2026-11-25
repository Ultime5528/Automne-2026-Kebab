from commands2 import SequentialCommandGroup

from commands.claw.ungrab import Ungrab
from commands.arm.move_up import MoveUp
from subsystems.claw import Claw
from subsystems.arm import Arm

class Drop(SequentialCommandGroup):

    def __init__(self, claw: Claw, arm: Arm):
        super().__init__(
            MoveUp(arm),
            Ungrab(claw),
        )