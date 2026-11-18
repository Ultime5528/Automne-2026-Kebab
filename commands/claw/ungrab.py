from subsystems.claw import Claw
from ultime.command import Command


class Ungrab(Command):

    def __init__(self, claw: Claw):
        super().__init__()
        self.claw = claw
        self.addRequirements(self.claw)


    def execute(self):
        if self.claw.get_encoder() >= 1:
            self.claw.ungrab()
        elif self.claw.get_encoder() <= 1:
            self.claw.slow_ungrab()

    def isFinished(self) -> bool:
        return self.claw.is_switch_pressed()

    def end(self, interrupted: bool):
        self.claw.stop()
        self.claw.encoder.setPosition(0)
