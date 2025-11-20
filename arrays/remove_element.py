from typing import List

class Solution:
    def removeElenment(self, nums: List[int], val: int) -> int:
        """用栈思考，实现元素移除，把nums本身看作一个栈"""
        stack_size = 0
        for num in nums:
            if num != val:
                nums[stack_size] = num
                stack_size += 1
        return stack_size

if __name__ == "__main__":
    nums = list(map(int, input("请输入数组（用空格分隔）：").split()))
    val = int(input("请输入val的值："))
    k = Solution().removeElenment(nums, val)
    print("不等于val的元素个数：", k)