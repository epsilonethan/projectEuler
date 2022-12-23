import pytest
import numpy as np
from helpers import genMath as gm


class TestGenMath:

    def test_find_multiples_of(self):
        np.testing.assert_array_equal(np.array([0, 2, 4, 6, 8]), gm.find_multiples_of(2, 10))
        np.testing.assert_array_equal(np.array([0, 2, 4, 6, 8]), gm.find_multiples_of(2, 9))

        with pytest.raises(TypeError) as e:
            gm.find_multiples_of('string', 2)
            assert e.value == 'Only integers are allowed'

        with pytest.raises(TypeError) as e:
            gm.find_multiples_of(2, 'string')
            assert e.value == 'Only integers are allowed'

    def test_find_evens(self):
        np.testing.assert_array_equal(np.array([2, 4]), gm.find_evens(np.array([1, 2, 3, 4])))

        with pytest.raises(TypeError) as e:
            gm.find_evens('string')
            assert e.value == 'Only np.ndarray is allowed'

        with pytest.raises(TypeError) as e:
            gm.find_evens(1)
            assert e.value == 'Only np.ndarray is allowed'

    def test_find_factors(self):
        assert gm.find_factors(4) == [2, 2]
        assert gm.find_factors(12) == [2, 2, 3]

        with pytest.raises(TypeError) as e:
            gm.find_factors(1.0)
            assert e.value == 'Only integers are allowed'

        with pytest.raises(TypeError) as e:
            gm.find_factors('string')
            assert e.value == 'Only integers are allowed'
