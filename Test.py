import unittest
from FailureCount import FailureCollection

class AlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.file = "test.json"


    def test_build(self):
        fc = FailureCollection(self.file)
        self.assertEqual(fc.get_error_count(), 1)

    
if __name__ == '__main__':
    unittest.main()