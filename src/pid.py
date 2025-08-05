from helper import clamp
from pybricks.tools import StopWatch

class PID_Controller:
    """A PID controller class implementation"""

    def __init__(self, config, setpoint, output_limit=None):
        """
        Initializes the PID controller with the given configuration and setpoint.
        
        :param config: Configuration dictionary containing PID parameters
        :param setpoint: Desired setpoint value
        """
        self.kp = config.get("kp", 0)
        self.ki = config.get("ki", 0)
        self.kd = config.get("kd", 0)
        self.i_limit = config.get("i_limit", None)
        self.output_limit = output_limit if output_limit else config.get("output_limit", None)

        self._setpoint = setpoint

        self._proportional = 0
        self._integral = 0
        self._derivative = 0

        self._timer = StopWatch()
        self._error = float('inf')

        self._last_time = 0
        self._last_error = 0
    
    def update(self, input):
        """
        Updates the PID controller with the new input value.
        
        :param input: The current input value
        :return: The correction value
        """
        self._error = input - self._setpoint

        d_time = self._timer.time() - self._last_time
        

        self._proportional = self._error * self.kp * d_time
        self._integral += self._error * self.ki * d_time
        self._derivative = ((self._error - self._last_error) / d_time) * self.kd if d_time > 0 else 0

        if self.i_limit is not None:
            self._integral = clamp(self._integral, self.i_limit[0], self.i_limit[1])

        correction = self._proportional + self._integral + self._derivative
        if self.output_limit is not None:
            correction = clamp(correction, self.output_limit[0], self.output_limit[1])

        self._last_error = self._error
        self._last_time = self._timer.time()
        return correction
    
    def reset(self):
        """
        Resets the PID controller.
        
        :return: None
        """
        self._proportional = 0
        self._integral = 0
        self._derivative = 0
        self._last_error = 0

    # --- Getters and Setters ---

    def get_tunings(self):
        """
        Returns the current PID tunings.
        
        :return: A dictionary containing the current PID tunings
        """
        return {
            "kp": self.kp,
            "ki": self.ki,
            "kd": self.kd,
            "i_max": self.i_limit,
            "output_max": self.output_max
        }
    
    def set_tunings(self, tunings):
        """
        Sets new tunings for the PID controller.
        
        :param tunings: A dictionary containing the new PID tunings
        :return: None
        """
        self.kp = tunings.get("kp", self.kp)
        self.ki = tunings.get("ki", self.ki)
        self.kd = tunings.get("kd", self.kd)
        self.i_limit = tunings.get("i_max", self.i_limit)
        self.output_max = tunings.get("output_max", self.output_max)
        self.reset()
    
    def get_setpoint(self):
        """
        Returns the current setpoint of the PID controller.
        
        :return: The current setpoint value
        """
        return self._setpoint

    def set_setpoint(self, setpoint):
        """
        Sets a new setpoint for the PID controller.
        
        :param setpoint: The new setpoint value
        :return: None
        """
        self._setpoint = setpoint
    
    def get_diagnostics(self):
        """
        Returns the PID controller's diagnostic information.

        :return: A dictionary containing the PID controller's diagnostic information
        """
        return {
            "proportional": self._proportional,
            "integral": self._integral,
            "derivative": self._derivative,
            "last_error": self._last_error,
            "error": self._error
        }

    def get_error(self):
        """
        Returns the current error of the PID controller.
        
        :return: The current error value
        """
        return self._error