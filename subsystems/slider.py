import rev

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Slider(Subsystem):
    speed = autoproperty(0.1)

    def __init__(self):
        super().__init__()
        self._motor = rev.SparkMax(
            ports.CAN.slider_motor, rev.SparkMax.MotorType.kBrushless
        )


    def slide_right(self):
        self._motor.set(self.speed)

    def slide_left(self):
        self._motor.set(-self.speed)

    def stop(self):
        self._motor.stopMotor()

    def logValues(self):
        super().logValues()
        self.log("motor_output", self._motor.get())
    
