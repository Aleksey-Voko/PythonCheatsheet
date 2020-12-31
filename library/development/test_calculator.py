import unittest

from library.development.calculator import Calculator, ExtCalculator


# noinspection PyPep8Naming
def setUpModule():
    """
    Before running module.
    """
    pass


# noinspection PyPep8Naming
def tearDownModule():
    """
    After running module.
    """
    pass


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up for class.
        Before running all tests.
        """
        cls.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down for class.
        After running all tests.
        """
        pass

    def setUp(self):
        """
        Set up for test.
        Before running each test.
        """
        pass

    def tearDown(self):
        """
        Tear down for test.
        After running each test.
        """
        pass

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(self.calc.sub(4, 2), 2)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 5), 10)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(3, 0)

    @unittest.skip('Skip test test_div')
    def test_div(self):
        self.assertEqual(self.calc.div(8, 4), 2)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0)


@unittest.skip("Skip class TestCalculatorExt")
class TestCalculatorExt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = ExtCalculator()

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(self.calc.pow(3, 3), 27)


if __name__ == '__main__':
    unittest.main()
