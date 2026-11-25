from ultime.immutable import Immutable

"""
Respect the naming convention : "subsystem" _ "component type" _ "precision"

Put port variables into the right category: CAN - PWM - DIO

Order port numbers, ex:
    shooter_motor = 0
    drivetrain_motor_fr = 1
    drivetrain_motor_rr = 2
"""


class CAN(Immutable):

    claw_motor = 0
    arm_motor = 1
    slider_motor = 2

class PWM(Immutable):
    pass

class DIO(Immutable):
    claw_switch_min = 0
    arm_switch_min = 1
    arm_switch_max = 2

class PDP(Immutable):
    pass
