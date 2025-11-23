from collections import defaultdict
from typing import List

class Solution:
    def SubarraySum(self, nums: List[int], k: int) -> int:
        """
        和为 K 的子数组
        :param nums: 数组，元素不是全为整数
        :param k: 子数组元素求和的目标值
        :return: 子数组和为k的个数
        时间复杂度：O(n)，其中 n 为 nums 的长度。
        空间复杂度：O(n)
        """
        # 思路：前缀和s + 哈希表(s[0]=0 也加到哈希表中)
        # 遍历s，一边枚举右边的sj，一边用哈希表统计左边有多少个i满足 i < j 且 s[i] = s[j]−k
        s = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s[i + 1] = s[i] + nums[i]
        cnt = defaultdict(int)
        ans = 0
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    # 1. 题目给的常规用例
    print(sol.SubarraySum([1,1,1], 2))     # 2
    print(sol.SubarraySum([1,2,3], 3))     # 2


