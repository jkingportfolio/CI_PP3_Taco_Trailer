"""
Unit testing for valia and invalid password
"""
import unittest
import taco_trailer_command_line as ttcl


class TestPassword(unittest.TestCase):
    """
    Verification of the user password creation input
    """

    def test_validate_password(self):
        """
        Test for valid password input
        """
        self.assertTrue(ttcl.validate_password('Password1#'), True)

    def test_validate_wrong_password(self):
        """
        Test for invalid password input
        """
        self.assertEqual(ttcl.validate_password('pass'), None)


if __name__ == '__main__':
    unittest.main()
