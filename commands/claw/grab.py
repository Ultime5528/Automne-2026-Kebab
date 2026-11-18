from subsystems.claw import Claw
from ultime.autoproperty import autoproperty
from ultime.command import Command


class Grab(Command):

    rotation_encoder_claw = autoproperty(10)

    def __init__(self, claw: Claw):
        super().__init__()
        self.claw = claw
        self.addRequirements(self.claw)


    def execute(self):
        if self.claw.get_encoder() <= 9:
            self.claw.grab()
        elif self.claw.get_encoder() >= 9:
            self.claw.slow_grab()

    def isFinished(self) -> bool:
        return self.claw.get_encoder() >= self.rotation_encoder_claw

    def end(self, interrupted: bool):
        self.claw.maintain()
