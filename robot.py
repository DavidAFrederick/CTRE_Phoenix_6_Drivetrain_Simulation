#!/usr/bin/env python3
"""
    This is a demo program for arcade drive in Python with Phoenix 6
    https://github.com/CrossTheRoadElec/Phoenix6-Examples/tree/main/python/ArcadeDrive
"""
import wpilib
from commands2 import TimedCommandRobot, Command

from drivetrain_subsystem import DriveTrain
from manual_drive_command import TeleOpDriveCommmand
from driveshortdistance_command import DriveShortDistance


class MyRobot(TimedCommandRobot):
    """
    Example program that shows to do simple arcade drive in robotpy
    with Phoenix 6
    """

    def robotInit(self):
        """Robot initialization function"""

        # Keep a reference to an Xbox Controller for teleop control
        self.joystick = wpilib.XboxController(0)
        self.drivetrain = DriveTrain()

        self.drivetrain.setDefaultCommand(TeleOpDriveCommmand(self.drivetrain, self.joystick))

    def autonomousInit(self) -> None:
        self._auto_command = self.getAutonomousCommand()

        if self._auto_command is not None:
            self._auto_command.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass
        
    def teleopPeriodic(self) -> None:
        """Runs the motors with arcade drive"""
        # TeleOpDriveCommmand(self.drivetrain, self.joystick)
        return super().teleopPeriodic()

    def getAutonomousCommand(self) -> Command:
        return DriveShortDistance(self.drivetrain)

if __name__ == "__main__":
    wpilib.run(MyRobot)