import rev
import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Claw(Subsystem):
    speed_motor = autoproperty(0.5)
    slow_motor = autoproperty(0.2)
    maintain_speed = autoproperty(0.05)

    def __init__(self):
        super().__init__()


        self.claw_motor = rev.SparkMax(
            ports.CAN.claw_motor, rev.SparkMax.MotorType.kBrushless
        )
        self.encoder = self.claw_motor.getEncoder()
        self.switch = Switch(
            Switch.Type.NormallyOpen, ports.DIO.switch_min_claw,
        )

    def grab(self):
        self.claw_motor.set(self.speed_motor)

    def slow_grab(self):
        self.claw_motor.set(self.slow_motor)

    def maintain(self):
        self.claw_motor.set(self.maintain_speed)

    def ungrab(self):
        self.claw_motor.set(-self.speed_motor)

    def slow_ungrab(self):
        self.claw_motor.set(-self.slow_motor)

    def stop(self):
        self.claw_motor.stopMotor()

    def is_switch_pressed(self) -> bool:
        return self.switch.isPressed()

    def get_encoder(self) -> float:
        return self.claw_motor.getEncoder().getPosition()
