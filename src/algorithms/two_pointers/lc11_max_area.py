from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        盛最多的水
        :param height: 一个长度 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
        :return:找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水，返回最大的储水量的值。
        时间复杂度：O(N)双指针遍历一次底边宽度 N。
        空间复杂度：O(1)
        """
        # 思路：双指针
        # 1.若向内 移动短板 ，水槽的短板 min(h[i],h[j]) 可能变大，因此下个水槽的面积可能增大
        # 2.若向内 移动长板 ，水槽的短板 min(h[i],h[j]) 不变或变小，因此下个水槽的面积 一定变小
        left = 0
        right = len(height) - 1
        ans = 0
        while left != right:
            if height[left] > height[right]:
                ans = max(ans, height[right]*(right - left))
                right -= 1
            else:
                ans = max(ans, height[left]*(right - left))
                left += 1
        return ans

if __name__ =='__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # 49
    print(sol.maxArea([1,1])) # 1