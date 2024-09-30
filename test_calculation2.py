import pytest
import calculation


class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        del cls.cal

    def setup_method(self, method):
        print('setup_method')

    def teardown_method(self, method):
        print('teardown_method')

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    @pytest.mark.skip(reason='skip')
    def test_add_num_and_double_skip(self):
        print('skip')