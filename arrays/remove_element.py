from typing import List

class Solution:
    def removeElenment(self, nums: List[int], val: int) -> int:
        """用栈思考，实现元素移除，把nums本身看作一个栈
        其实本质可以看作是双指针：右指针 right(for循环)指向当前将要处理的元素，左指针 left（stack_size） 指向下一个将要赋值的位置。
        时间复杂度：O(n)，其中 n 是 nums 的长度
        空间复杂度：O(1)"""
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