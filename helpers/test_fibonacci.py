import pytest
import numpy as np
from helpers import fibonacci as fb


class TestFibonacci:

    def test_generate_fibs(self):
        np.testing.assert_array_equal(np.array([0, 1]), fb.generate_fibs(2))
        np.testing.assert_array_equal(np.array([0, 1, 1, 2, 3]), fb.generate_fibs(5))

        with pytest.raises(TypeError) as e:
            fb.generate_fibs('string')
            assert e.value == 'Only integers are allowed'

        with pytest.raises(TypeError) as e:
            fb.generate_fibs(1.5)
            assert e.value == 'Only integers are allowed'

    def test_all_fibs_up_to(self):
        np.testing.assert_array_equal(np.array([0, 1, 1, 2]), fb.all_fibs_up_to(2))
        np.testing.assert_array_equal(np.array([0, 1, 1, 2, 3, 5]), fb.all_fibs_up_to(5))
        np.testing.assert_array_equal(np.array([0, 1, 1, 2, 3, 5]), fb.all_fibs_up_to(7))

        with pytest.raises(TypeError) as e:
            fb.generate_fibs('string')
            assert e.value == 'Only integers are allowed'

        with pytest.raises(TypeError) as e:
            fb.generate_fibs(1.5)
            assert e.value == 'Only integers are allowed'

    def test_binet_formula(self):
        assert fb.binet_formula(2) == 1
        assert fb.binet_formula(5) == 5
        assert fb.binet_formula(7) == 13

        with pytest.raises(TypeError) as e:
            fb.binet_formula('string')
            assert e.value == 'Only integers are allowed'

        with pytest.raises(TypeError) as e:
            fb.binet_formula(1.5)
            assert e.value == 'Only integers are allowed'

