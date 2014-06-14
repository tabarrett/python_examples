""" Test cases for lib module"""

import unittest
import logging

import lib

class TestGetLogger(unittest.TestCase):
     
    """Test case for get_logger function."""

    def test_type(self):
        """ Test the type of the logger object."""
        assert type(lib.get_logger()) is logging.Logger
        assert 1111 == 1111
        assert "blah" == "blah"
        assert True
        #assert False 
