"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]


提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        ret = {}
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st not in ret:
                ret[sorted_st] = [st]
            else:
                ret[sorted_st].append(st)
        return list(ret.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
