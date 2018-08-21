# 140. Word Break II

from typing import List, Dict


class Solution:
    def __init__(self):
        self.map: Dict[str, List[str]] = dict()
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s in self.map.keys(): return self.map[s]
        if not len(s): return ['']
        res = []
        for word in wordDict:
            if s[0:len(word)] != word:
                continue
            rem = self.wordBreak(s[len(word):], wordDict)
            for str_ in rem:
                res.append(word + (' ' if str_ else '') + str_)
        self.map[s] = res
        return res


def test():
    s = Solution()

    string = 'catsanddog'
    wordDict = ['cat', 'cats', 'and', 'sand', 'dog']
    output = s.wordBreak(string, wordDict)
    print(f'{string=}\n{wordDict=}\n{output=}\n')

    string = 'pineapplepenapple'
    wordDict = ['apple', 'pen', 'applepen', 'pine', 'pineapple']
    output = s.wordBreak(string, wordDict)
    print(f'{string=}\n{wordDict=}\n{output=}\n')

    string = 'catsandog'
    wordDict = ['cats', 'dog', 'sand', 'and', 'cat']
    output = s.wordBreak(string, wordDict)
    print(f'{string=}\n{wordDict=}\n{output=}')

if __name__ == '__main__':
    test()
