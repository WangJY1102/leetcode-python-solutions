class Solution:
    def happy_number(self,n: int) -> bool:
        """
        判断 n 是否为快乐数。
        使用哈希表（检查数字是否在哈希集合中需要 O(1) 的时间，而对于其他数据结构，则需要 O(n) 的时间。）。

        Args:
            n (int): 正整数，范围 ≥ 1
        Returns:
            bool: True 如果是快乐数，否则 False

        Time Complexity:
            O(log n)
        Space Complexity:
            O(logn)
        """
        def get_next(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit**2
            return total

        # seen哈希集合，专用来判重/检测环
        seen = set()
        # n的两种情况：1快乐数；数n出现过了，陷入循环
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n ==1


if __name__ == "__main__":
    n = int(input("请输出整数n："))
    ans = Solution().happy_number(n)
    print("n是否为快乐数：", ans)