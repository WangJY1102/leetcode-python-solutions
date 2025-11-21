from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        判断两个字符串是否为有效字母异位词。
        :param s:第一个字符串
        :param t:第二个字符串
        :return: 是异位词返回 True，否则 False
        """
        # 哈希表：统计 s1各字符时执行 +1 ，统计 s2各字符时−1
        # 若两字符串互为重排，则最终哈希表中所有字符统计数值都应为0
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            dic[c] -=1
        for val in dic.values():
            if val != 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    # 1. 题目给的常规用例
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False

