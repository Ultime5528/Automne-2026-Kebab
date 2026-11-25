from subsystems.claw import Claw
from ultime.command import Command


class Reset(Command):

    def __init__(self, claw: Claw):
        super().__init__()
        self.claw = claw
        self.addRequirements(self.claw)

    def execute(self):
        self.claw.grab()

    def isFinished(self) -> bool:
        return self.claw.is_open()

    def end(self, interrupted: bool):
        self.claw.stop()
        self.claw._encoder.setPosition(0)
