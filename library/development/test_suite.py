import unittest

from library.development import test_calculator


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(test_calculator.TestCalculator))
    test_suite.addTest(unittest.makeSuite(test_calculator.TestCalculatorExt))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
