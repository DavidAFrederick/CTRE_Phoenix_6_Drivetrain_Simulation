from commands2 import Command
from drivetrain_subsystem import DriveTrain
from wpilib import XboxController


class TeleOpDriveCommmand(Command):
    def __init__(self, drivetrain: DriveTrain, controller : XboxController ) -> None:
        super().__init__()

        self.drivetrain = drivetrain
        self.controller = controller

        # Tell the scheduler this requires the drivetrain
        self.addRequirements(self.drivetrain)

    def initialize(self):
        pass

    def execute(self):
        self.drivetrain.drive_teleop(self.controller.getLeftY() * -1, self.controller.getLeftX() )

    def isFinished(self) -> bool:     # Since this is the default task for the drivetrain, don't end it
        return False

    def end(self, interrupted: bool):   # Stop the robot (but we should never get here)
        self.drivetrain.drive_teleop(0,0)
        