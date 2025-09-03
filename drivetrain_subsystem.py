from commands2 import Subsystem
from phoenix6 import CANBus, configs, controls, hardware

class DriveTrain(Subsystem):

    def __init__(self) -> None:
        super().__init__()

        self.front_left_motor  = hardware.TalonFX(1)
        self.front_right_motor = hardware.TalonFX(2)

        # Configure the motors
        cfg = configs.TalonFXConfiguration()
        cfg.motor_output.inverted = configs.config_groups.InvertedValue.COUNTER_CLOCKWISE_POSITIVE
        self.front_left_motor.configurator.apply(cfg)

        cfg.motor_output.inverted = configs.config_groups.InvertedValue.CLOCKWISE_POSITIVE
        self.front_right_motor.configurator.apply(cfg)

        # Keep a reference to the DutyCycleOut control request to update periodically
        self.left_out = controls.DutyCycleOut(0)
        self.right_out = controls.DutyCycleOut(0)


    def drive_teleop(self, forward: float, turn: float):

        # print(f"forward: {forward}  turn: {turn} ")

        # And set the DutyCycleOut to the motor controllers
        self.front_left_motor.set_control(self.left_out.with_output(forward + turn))
        self.front_right_motor.set_control(self.right_out.with_output(forward - turn))


    
