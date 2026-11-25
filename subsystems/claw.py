import rev
import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Claw(Subsystem):
    speed_motor = autoproperty(0.1)
    speed_slow = autoproperty(0.05)
    speed_maintain = autoproperty(0.01)

    def __init__(self):
        super().__init__()


        self._motor = rev.SparkMax(
            ports.CAN.claw_motor, rev.SparkMax.MotorType.kBrushless
        )
        self._encoder = self._motor.getEncoder()
        self._switch = Switch(
            Switch.Type.NormallyOpen,
            ports.DIO.claw_switch_min,
        )

    def grab(self):
        self._motor.set(self.speed_motor)

    def slow_grab(self):
        self._motor.set(self.speed_slow)

    def maintain(self):
        self._motor.set(self.speed_maintain)

    def ungrab(self):
        self._motor.set(-self.speed_motor)

    def slow_ungrab(self):
        self._motor.set(-self.speed_slow)

    def stop(self):
        self._motor.stopMotor()

    def is_open(self) -> bool:
        return self._switch.isPressed()

    def get_position(self) -> float:
        return self._encoder.getPosition()

    def logValues(self):
        super().logValues()
        self.log("is_open", self.is_open())
        self.log("position", self.get_position())
        self.log("motor_output", self._motor.get())
