import unittest
import calculation

class CalTest(unittest.TestCase):
    def setUp(self):
        self.cal = calculation.Cal()

    def tearDown(self):
        del self.cal

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

    @unittest.skip('skip')
    def test_add_num_and_double_skip(self):
        print('skip')

if __name__ == '__main__':
    unittest.main()
