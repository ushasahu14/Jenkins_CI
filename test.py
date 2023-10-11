import pytest
from longestsubstring import Solution


def test_x(input):
    for (key,value)in input.items():
        assert Solution.lengthOfLongestSubstring(key)==value
