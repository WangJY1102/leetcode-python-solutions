from collections import defaultdict

class Solution:
    def minwindowsubstring(self, s: str, t: str) -> str:
        """
        最小覆盖子串
        :param s: 一个字符串
        :param t: 一个字符串
        :return: 返回s中涵盖t所有字符的最小子串，否则空字符串
        时间复杂度：O(m+n)，
        空间复杂度：O(k)，k为S和T中的字符集合。
        """
        # 思路：滑动窗口
        # 1.不断增加j使滑动窗口增大，直到窗口包含了T的所有元素
        # 2.不断增加i使滑动窗口缩小，将不必要的元素排除在外，使长度减小，直到碰到一个必须包含的元素，记录此时滑动窗口的长度，并保存最小值
        # 3.让i再增加一个位置，这个时候滑动窗口肯定不满足条件了，重复1.，寻找新的满足条件的滑动窗口，如此反复，直到j超出了字符串S范围。
        # 用一个字典need来表示当前滑动窗口中需要的各元素的数量，用T中各元素来初始化need。
        # 当need中所有元素的数量都小于等于0时，表示当前滑动窗口不再需要任何元素。
        # 维护一个额外的变量needCnt来记录所需元素的总数量，不用遍历need看是否所有元素数量都小于等于0（避免耗费O(k)的时间复杂度）
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j,c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True: # 2.增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0: # 碰到的第一个必须包含的元素
                        break
                    need[c] += 1 # i右移，需要的+1
                    i += 1
                if j - i < res[1] - res[0]: # 记录结果
                    res = (i, j)
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]

if __name__ == "__main__":
    sol = Solution()
    # 1. 题目给的常规用例
    print(sol.minwindowsubstring("ADOBECODEBANC", "ABC"))  # "BANC"
    print(sol.minwindowsubstring("a", "a"))     #"a"
    print(sol.minwindowsubstring("a", "aa"))   # ""




