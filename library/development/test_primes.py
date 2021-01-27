import unittest

from library.development.primes import is_prime


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


class TestPrimes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up for class.
        Before running all tests.
        """
        pass

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

    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-6))


class TestOther(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @unittest.skip('Skip test test_div')
    def test_div(self):
        self.assertEqual((8 / 4), 2)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0)


@unittest.skip("Skip class TestOtherSkip")
class TestOtherSkip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_sqrt(self):
        pass

    def test_pow(self):
        pass


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestPrimes))
    suite.addTests(unittest.makeSuite(TestOther))
    suite.addTests(unittest.makeSuite(TestOtherSkip))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite())

