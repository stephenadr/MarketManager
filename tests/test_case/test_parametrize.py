import pytest


class TestParametrize:
    @pytest.mark.parametrize("a ,b ,c",[(1,2,3),(4,5,9)])
    def test_parametrize(self,a,b,c):
            assert a + b == c


    @pytest.mark.parametrize("input_test,expect_test",[("3+5", 8), ("2+4", 6), ("6+7", 13)])
    def test_parametrize_2(self,input_test,expect_test):
        assert eval(input_test) == expect_test
import pytest


class TestParametrize:
    @pytest.mark.parametrize("a ,b ,c",[(1,2,3),(4,5,9)])
    def test_parametrize(self,a,b,c):
            assert a + b == c


    @pytest.mark.parametrize("input_test,expect_test",[("3+5", 8), ("2+4", 6), ("6+7", 13)])
    def test_parametrize_2(self,input_test,expect_test):
        assert eval(input_test) == expect_test