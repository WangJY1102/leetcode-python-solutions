from lc1_two_sum import Solution

def test_two_sum():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_empty():
    assert Solution().twoSum([], 9) == []