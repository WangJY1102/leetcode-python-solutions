from typing import List
import bisect

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        元素之和不小于目标值的，长度最小的子数组
        暴力解法（python超时）
        时间复杂度：O(n2)
        空间复杂度：O(1)
        """
        min_len = 1e9
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    min_len = min(min_len, j - i + 1)
                    break
        if min_len == 1e9:
            min_len = 0
        return min_len

    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        """
        前缀和 + 二分查找
        为了使用二分查找，需要额外创建一个数组 sums 用于存储数组 nums 的前缀和，其中 sums[i] 表示从 nums[0] 到 nums[i−1] 的元素和。
        通过二分查找得到大于或等于 i 的最小下标 bound，使得 sums[bound]−sums[i−1]≥s
        时间复杂度：O(nlogn)
        空间复杂度：O(n)
        """
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans

    def minSubArraylen3(self, s: int, nums: List[int]) -> int:
        """
        滑动窗口:两个指针 start 和 end 分别表示子数组（滑动窗口窗口）的开始位置和结束位置，
        维护变量 sum 存储子数组中的元素和（即从 nums[start] 到 nums[end] 的元素和）
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        start, end = 0, 0
        total = 0
        n = len(nums)
        ans = n + 1
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans

if __name__ == "__main__":
    nums = list(map(int, input("请输入数组（空格分隔）：").split()))
    target = int(input("请输出目标值："))
    min_len = Solution().minSubArrayLen(target, nums)
    print("最小子数组长度：", min_len)