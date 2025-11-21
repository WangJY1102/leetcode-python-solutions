from typing import List

class Solution:
    def twoSumii(self, numbers: List[int], target: int) -> List[int]:
        """
        有序列表，两数之和
        初始时两个指针分别指向第一个元素位置和最后一个元素的位置。
        每次计算两个指针指向的两个元素之和，并和目标值比较。
        如果两个元素之和等于目标值，则发现了唯一解。
        如果两个元素之和小于目标值，则将左侧指针右移一位。
        如果两个元素之和大于目标值，则将右侧指针左移一位。

        :param numbers:
        :param target:
        :return: 两个值的和为target的下标，从1开始
        时间复杂度：O(n)，其中 n 是数组的长度。两个指针移动的总次数最多为 n 次。
        空间复杂度：O(1)
        """
        low = 0
        high = len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total < target:
                low += 1
            elif total > target:
                high -= 1
            else:
                return [low + 1, high + 1]
        return [-1, -1]

    def twoSumii2(self, numbers: List[int], target: int) -> List[int]:
        """
        二分法，同样应用双指针
        时间复杂度：O(nlogn)
        空间复杂度：O(1)
        """
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return [-1, -1]



if __name__ == "__main__":
    nums = list(map(int, input("请输出数组（空格分格）：").split()))
    target = int(input("请输入目标值："))
    ans = Solution().twoSumii(nums, target)
    print("下标：", ans)