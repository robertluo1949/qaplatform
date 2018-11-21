import unittest


def test_startTest(self):
    class Foo(unittest.TestCase):
        def test_1(self):
            pass
        def test_1(self):
            pass
    test = Foo('test_1')

    result = unittest.TestResult()

    result.startTest(test)

    self.assertTrue(result.wasSuccessful())
    self.assertEqual(len(result.errors), 0)
    self.assertEqual(len(result.failures), 0)
    self.assertEqual(result.testsRun, 1)
    self.assertEqual(result.shouldStop, False)
    print(result.failures)
    print(result.addSuccess())
    result.stopTest(test)


    # "Called after the test case test has been executed, regardless of
    # the outcome. The default implementation does nothing."


if __name__ == '__main__':
    unittest.main()