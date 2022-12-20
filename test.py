import math
import unittest
from main import start_command
from main import credits
from main import id
from main import return_chat_id

class TestStart(unittest.TestCase):
    # def test_start(self):
    #     self.assertEqual(start_command(message), start_command(message))
    #     print()
     def test_start(self):
         self.assertEqual(return_chat_id(),id)



if __name__ == '__main__':

    unittest.main()


