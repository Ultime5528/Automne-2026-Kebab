import rev
import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Slider(Subsystem):

    speed_motor = autoproperty(0.1)

    def __init__(self):
        super().__init__()
        self.motor = rev.SparkMax(
            ports.CAN.slider_motor, rev.SparkMax.MotorType.kBrushless
        )

    def slide_right(self):
        self.motor.set(self.speed_motor)

    def slide_left(self):
        self.motor.set(-self.speed_motor)

    def stop(self):
        self.motor.stopMotor()
