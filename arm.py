""" code for controlling our robot arm."""

import lib

class Arm():

    "code for abstracting the robot's arm """

    def __init__(self):
        """Get logger object."""
        self.logger = lib.get_logger()
        self.arm_state = "retracted"
        self.logger.debug("Arm built")

    def extend(self):
        """Extend the robot's arm"""
        self.arm_state = "extended"
        self.logger.debug("Extended arm")

    def retract(self):
        """retract the robot's arm."""
        self.arm_state = "retracted"
        self.logger.debug("Retracted arm")
