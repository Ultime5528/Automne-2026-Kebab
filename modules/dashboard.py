import commands2
import wpilib
from commands.slider.left import SlideLeft

from commands.arm.move_up import Move_up
from commands.arm.move_down import Move_down
from commands.slider.right import SlideRight
from commands.claw.grab import Grab
from commands.claw.ungrab import Ungrab
from modules.hardware import HardwareModule
from commands.claw.reset import Reset
from ultime.log import Logger
from ultime.module import Module, ModuleList


class DashboardModule(Module):
    def __init__(
        self,
        hardware: HardwareModule,
        module_list: ModuleList,
    ):
        super().__init__()
        self._hardware = hardware
        self._module_list = module_list
        self.setupCopilotCommands(hardware)
        self.setupCommands(hardware)

    def setupCopilotCommands(self, hardware: HardwareModule):
        pass

    def setupCommands(self, hardware):
        """
        Claw
        """
        putCommandOnDashboard("Claw", Grab(hardware.claw))
        putCommandOnDashboard("Claw", Ungrab(hardware.claw))
        putCommandOnDashboard("Claw", Reset(hardware.claw))

        """
        Arm
        """
        putCommandOnDashboard("Arm", Move_up(hardware.arm))
        putCommandOnDashboard("Arm", Move_down(hardware.arm))

        """
        Slider
        """
        putCommandOnDashboard("Slider", SlideRight(hardware.slider))
        putCommandOnDashboard("Slider", SlideLeft(hardware.slider))

    def robotInit(self) -> None:
        for subsystem in self._hardware.subsystems:
            Logger.getInstance().addLoggable(subsystem)

        for module in self._module_list.modules:
            Logger.getInstance().addLoggable(module)
        for module in self._module_list.modules:
            if module.redefines_init_sendable:
                """
                If a module keeps a reference to a subsystem or the HardwareModule,
                it should be wrapped in a weakref.proxy(). For example,
                self.hardware = proxy(hardware)
                """
                print("Putting on dashboard:", module.getName())
                wpilib.SmartDashboard.putData(module.getName(), module)


def putCommandOnDashboard(
    sub_table: str, cmd: commands2.Command, name: str = None, suffix: str = " commands"
) -> commands2.Command:
    if not isinstance(sub_table, str):
        raise ValueError(
            f"sub_table should be a str: '{sub_table}' of type '{type(sub_table)}'"
        )

    if suffix:
        sub_table += suffix

    sub_table += "/"

    if name is None:
        name = cmd.getName()
    else:
        cmd.setName(name)

    wpilib.SmartDashboard.putData(sub_table + name, cmd)

    return cmd
