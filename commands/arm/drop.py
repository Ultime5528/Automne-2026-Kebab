from commands2 import SequentialCommandGroup

from commands.claw.ungrab import Ungrab
from commands.arm.move_up import Move_up
from subsystems.claw import Claw
from subsystems.arm import Arm


class Drop(SequentialCommandGroup):

    def __init__(self, claw: Claw, arm: Arm):
        super().__init__(
            Move_up(arm),
            Ungrab(claw),
        )
