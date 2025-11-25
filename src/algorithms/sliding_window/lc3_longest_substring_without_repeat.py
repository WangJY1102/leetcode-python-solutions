from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        无重复子串的最长子串
        :param s: 给定一个字符串
        :return: 返回不含有重复字符的最长子串的长度
        时间复杂度：O(n)
        空间复杂度：O(O(∣Σ∣))，其中 ∣Σ∣ 为字符集合的大小，本题中字符均为 ASCII 字符，所以 ∣Σ∣≤128
        """
        # 哈希表，dic维护从下标 left 到下标 right 的字符及其出现次数
        # 窗口内有重复字母，移除窗口左端点字母，缩小窗口，更新窗口长度最大值
        left = ans = 0
        dic = defaultdict(int)
        for right, ch in enumerate(s):
            dic[ch] += 1
            while dic[ch] > 1:
                dic[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    # 1. 题目给的常规用例
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # 1
