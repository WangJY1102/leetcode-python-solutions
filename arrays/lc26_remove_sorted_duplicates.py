from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """删除有序数组中的重复元素
        采用双指针（快慢指针）
        快指针表示遍历数组到达的下标位置，慢指针表示下一个不同元素要填入的下标位置，初始时两个指针都指向下标 1。"""
        if len(nums) == 0:
            return 0
        fast = slow = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == "__main__":
    nums = list(map(int, input("请输入整数数组（以空格为分隔）：").split()))
    slow = Solution().remove_duplicates(nums)
    print("未重复的元素个数为：", slow)