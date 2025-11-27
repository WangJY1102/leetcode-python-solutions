from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和
        :param nums: 一个整数数组
        :return: 返回满足nums[i] + nums[j] + nums[k] == 0的不重复的三元组
        时间复杂度：O(N2)：其中固定指针k循环复杂度 O(N)，双指针 i，j 复杂度 O(N)
        空间复杂度：O(1)：指针使用常数大小的额外空间。
        """
        # 思路：排序+双指针
        # 1.固定 3 个指针中最左（最小）元素的指针 k，双指针 i，j 分设在数组索引 (k,len(nums)) 两端。
        # 2.双指针 i , j 交替向中间移动，记录对于每个固定指针 k 的所有满足 nums[k] + nums[i] + nums[j] == 0 的 i,j 组合。
        nums.sort()
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4])) # [[-1,-1,2],[-1,0,1]]
    print(sol.threeSum([0, 1, 1])) # []
    print(sol.threeSum([0, 0, 0])) # [[0,0,0]]