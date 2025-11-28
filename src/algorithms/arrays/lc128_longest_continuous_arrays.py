from typing import List

from sympy.solvers.ode.single import solver_map


class Solution:
    def longestContArray(self, nums: List[int]) -> int:
        """
        最长连续数组
        :param nums:一个未排序的整数序列
        :return: 找出数字连续的最长序列的长度（不要求序列元素在原数组中连续）
        时间复杂度：O(n)，其中 n 是 nums 的长度。
        空间复杂度：O(m)。其中 m 是 nums 中的不同元素个数。
        """
        # 思路：哈希集合
        # 1.题目要求时间复杂度O(n)，所以不能排序，利用哈希集合看某元素是否存在只需O(1)，不遍历数组
        # 2.以x为起点，不断查找下一个x+1、x+2...是否存在，记录最大长度
        # 3.如果x-1存在，则跳过当前的x，等遍历到x-1时再进行统计
        st = set(nums)
        ans = 0
        for x in st:
            if x - 1 in st:
                continue
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y - x)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestContArray([100,4,200,1,3,2])) # 4
    print(sol.longestContArray([0,3,7,2,5,8,4,6,0,1])) # 9
    print(sol.longestContArray([1,0,1,2])) # 3