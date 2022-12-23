import unittest
import numpy as np
from helpers import fibonacci as fb


class FibonacciTestCase(unittest.TestCase):

    def test_generate_fibs(self):
        np.testing.assert_array_equal(np.array([0,1,1,2,3]), fb.generate_fibs(5))

    def test_generate_fibs2(self):
        np.testing.assert_array_equal(np.array([0,1]), fb.generate_fibs(2))
