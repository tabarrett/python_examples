""" Unittests for arm """

import unittest

import arm

class TestExtend(unittest.TestCase):

    """Test extending the robot's arm."""

    def setUp(self):
        """Build arm object."""
        self.arm = arm.Arm()

    def test_basic(self):
        """Test basic extention."""
        # put arm in known state
        self.arm.arm_state = "retracted"

        #Extemd the arm and test the result
        self.arm.extend()
        assert self.arm.arm_state == "extended" 


class TestRetracted(unittest.TestCase):

    """Test Retracting the robot's arm."""

    def setUp(self):
        """Build arm object."""
        self.arm = arm.Arm()

    def test_basic(self):
        """Test basic retraction."""
        # put arm in known state
        self.arm.arm_state = "retracted"

        #Extemd the arm and test the result
        self.arm.retracted()
        assert self.arm.arm_state == "retracted"
