from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        找到字符串中所有字母异位词
        :param s: 字符串
        :param p: 字符串
        :return: 找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。
        时间复杂度：O(m+(n−m)×Σ)，其中 n 为字符串 s 的长度，m 为字符串 p 的长度，Σ 为所有可能的字符数。
        空间复杂度：O(Σ)。用于存储字符串 p 和滑动窗口中每种字母的数量。
        """
        # 思路：滑动窗口（固定）
        # 1.构造一个len(p)的固定大小滑动窗口，并维护该窗口中目前个字母的数量，看与p中个字母数量是否相同
        # 2.如果len(s)<len(p),则返回空列表[]
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        # s_count用作维护s上滑动窗口中内容，p_count用于记录p中字母内容
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))  # [0,6]
    print(sol.findAnagrams("abab", "ab")) # [0,1,2]