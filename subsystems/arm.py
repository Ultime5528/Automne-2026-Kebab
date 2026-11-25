import rev

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Arm(Subsystem):

    speed_motor = autoproperty(0.5)
    speed_slow = autoproperty(0.2)
    speed_maintain = autoproperty(0.05)

    def __init__(self):
        super().__init__()
        self._motor = rev.SparkMax(
            ports.CAN.arm_motor, rev.SparkMax.MotorType.kBrushless
        )
        self._encoder = self._motor.getEncoder()
        self._switch_min = Switch(
            Switch.Type.NormallyOpen,
            ports.DIO.arm_switch_min,
        )
        self._switch_max = Switch(
            Switch.Type.NormallyOpen,
            ports.DIO.arm_switch_max,
        )

    def move_up(self):
        self._motor.set(self.speed_motor)

    def slow_move_up(self):
        self._motor.set(self.speed_slow)

    def move_down(self):
        self._motor.set(-self.speed_motor)

    def slow_move_down(self):
        self._motor.set(-self.speed_slow)

    def maintain(self):
        self._motor.set(self.speed_maintain)

    def stop(self):
        self._motor.stopMotor()

    def is_down(self) -> bool:
        return self._switch_min.isPressed()

    def is_up(self) -> bool:
        return self._switch_max.isPressed()

    def get_position(self) -> float:
        return self._motor.getEncoder().getPosition()

    def logValues(self):
        super().logValues()
        self.log("is_down", self.is_down())
        self.log("is_up", self.is_up())
        self.log("position", self.get_position())
