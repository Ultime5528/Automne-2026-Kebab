import rev
import wpilib

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
from ultime.switch import Switch


class Arm(Subsystem):

    speed_motor = autoproperty(0.5)
    slow_speed = autoproperty(0.2)
    speed_maintain = autoproperty(0.05)

    def __init__(self):
        super().__init__()
        self.arm_motor = rev.SparkMax(
            ports.CAN.arm_motor, rev.SparkMax.MotorType.kBrushless
        )
        self.arm_switch_min = Switch(
            Switch.Type.NormallyOpen, ports.DIO.switch_min_arm,
        )
        self.arm_switch_max = Switch(
            Switch.Type.NormallyOpen, ports.DIO.switch_max_arm,
        )


    def move_up(self):
        self.arm_motor.set(self.speed_motor)

    def slow_move_up(self):
        self.arm_motor.set(self.slow_speed)

    def move_down(self):
        self.arm_motor.set(-self.speed_motor)

    def slow_move_down(self):
        self.arm_motor.set(-self.slow_speed)

    def maintain(self):
        self.arm_motor.set(self.speed_maintain)

    def stop(self):
        self.arm_motor.stopMotor()

    def is_switch_min_pressed(self) -> bool:
        return self.arm_switch_min.isPressed()

    def is_switch_max_pressed(self) -> bool:
        return self.arm_switch_max.isPressed()

    def get_encoder(self) -> float:
        return self.arm_motor.getEncoder().getPosition()
