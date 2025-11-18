from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        """先查询哈希表中是否存在当前的 target-x 值
            时间复杂度O(N)
            空间复杂度O(N)
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []

    def twoSum2(self,nums: List[int], target: int):
        """暴力枚举法"""
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]



if __name__ == "__main__":
    nums = list(map(int, input("请输出数组（空格分格）：").split()))
    target = int(input("请输入目标值："))
    ans = Solution().twoSum(nums, target)
    print("下标：", ans)