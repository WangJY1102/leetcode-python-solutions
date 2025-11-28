from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        字母异位词分组
        :param strs: 一个字符串数组
        :return: 将 字母异位词组合在一起,按任意顺序返回结果列表
        时间复杂度：O(nmlogm)，其中 n 为 strs 的长度，m 为 strs[i] 的长度。每个字符串排序需要 O(mlogm) 的时间，有 n 个字符串
        空间复杂度：O(nm)
        """
        # 思路： 排序+哈希表
        # 1.字母异位词中包含相同的字母，次序不同，将每个字符串进行排序，字母异位词的结果会是一样的
        # 2.把排序后的字符串作为哈希表的key，value装对应排序前的异位词
        d = defaultdict(list) # 如果 key 不在字典中，则自动插入一个空列表
        for s in strs:
            sort_s = ''.join(sorted(s)) # 把 s 排序，作为哈希表的 key
            d[sort_s].append(s)
        return list(d.values())

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams([""])) # [[""]]
    print(sol.groupAnagrams(["a"])) #[["a"]]