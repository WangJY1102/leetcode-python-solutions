from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        移动零
        :param nums: 一个整数数组
        :return:将所有0移动到数组末尾，同时保持非零元素的相对位置，返回数组
        时间复杂度：O(n)，其中 n 为序列长度。每个位置至多被遍历两次。
        空间复杂度：O(1)。只需要常数的空间存放若干变量。
        """
        # 思路：双指针
        # 1.左指针指向当前待覆盖的位置，右指针进行整个数组的遍历
        # 2.如果右指针指向的元素非零，则赋值到左指针的位置，循环结束后左右指针之间的位置全部置零
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                continue
            nums[left] = nums[right]
            left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
        return nums

if __name__ == '__main__':
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12])) # [1,3,12,0,0]
    print(sol.moveZeroes([0])) # [0]
