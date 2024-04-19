import unittest
import method_json
import json
import os


class MyTestCase(unittest.TestCase):

    def test_verifing_input(self):
        # Creating a test file.
        with open("test.json", "w") as file:
            json.dump({"Resource": "test"}, file)

            # Check that 'verifying_input_json' returns valid results.
            self.assertTrue(method_json.verifying_input_json("test.json")) # Expect it to return 'True' for {"Resource": "test"}
            self.assertFalse(method_json.verifying_input_json("data.json")) # Expect it to return 'False' for {"Resource": "*"}

            os.remove('test.json')


if __name__ == '__main__':
    unittest.main()
