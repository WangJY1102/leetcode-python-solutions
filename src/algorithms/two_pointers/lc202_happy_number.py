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

    def happy_number2(self, n: int) -> bool:
        """
        判断 n 是否为快乐数。
        使用快慢指针检测环；非快乐数必会进入 4→16→37→... 循环。
        问题就可以转换为检测一个链表是否有环，慢速在链表中前进 1 个节点，快跑者前进 2 个节点

        Args:
            n (int): 正整数，范围 ≥ 1
        Returns:
            bool: True 如果是快乐数，否则 False

        Time Complexity:
            O(log n) —— 每次 next 值递减量级
        Space Complexity:
            O(1) —— 快慢指针只占用常数空间
        """

        def get_next(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total

        # 快慢指针
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and fast_runner != slow_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


if __name__ == "__main__":
    n = int(input("请输出整数n："))
    ans = Solution().happy_number(n)
    print("n是否为快乐数：", ans)