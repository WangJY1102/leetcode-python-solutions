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

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 遍历列表
        for i in range(len(nums)):
            # 计算需要找到的下一个目标数字
            res = target-nums[i]
                # 遍历剩下的元素，查找是否存在该数字
            if res in nums[i+1:]:
                # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
                # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
                return [i, nums[i+1:].index(res)+i+1]


if __name__ == "__main__":
    nums = list(map(int, input("请输出数组（空格分格）：").split()))
    target = int(input("请输入目标值："))
    ans = Solution().twoSum(nums, target)
    print("下标：", ans)