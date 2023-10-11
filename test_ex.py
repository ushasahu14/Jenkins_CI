from typing import Literal
import pytest
from  longestsubstring import Solution

myclass =Solution()

@pytest.fixture
def input_var():
    inp_out={"aaab":1,"hsdkgha":5,"eworuewor":5}
    return "aaab",2

@pytest.mark.parametrize("a,b",[("aaaab",2),("rwrrwr",2)])
def test_x(a,b):
    #s,t=input_var
    assert myclass.lengthOfLongestSubstring(a)==b
   # assert myclass.lengthOfLongestSubstring(s)==t