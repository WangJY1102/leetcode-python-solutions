from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        查找字符串数组中的最长公共前缀
        :param strs:一个字符串数组
        :return:若存在公共前缀，则输出；否则，输出""
        时间复杂度：O(mn)， m是字符串数组中的字符串的平均长度，n 是字符串的数量。
        空间复杂度：O(1)
        """
        # 纵向扫描
        s0 = strs[0]
        for i, ch in enumerate(s0):
            for s in strs:
                if ch != s[i] or i == len(s):
                    return s0[:i]
        return s0

if __name__ == "__main__":
    sol = Solution()
    # 1. 题目给的常规用例
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # fl
    print(sol.longestCommonPrefix(["dog","racecar","car"]))     #