# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = dict()
        ansidx = 0
        longest = 0
        i = 0
        for c in s:
            if c in char_map:
                if not char_map[c] < ansidx:
                    ansidx = char_map[c] + 1
            char_map[c] = i
            sublen = i - ansidx + 1
            if sublen > longest:
                longest = sublen
            i = i + 1
        return longest


def test():
    s = Solution()

    string = 'abcabcbb'
    output = s.lengthOfLongestSubstring(string)
    print(f'{string=}\n{output=}\n')

    string = 'bbbbb'
    output = s.lengthOfLongestSubstring(string)
    print(f'{string=}\n{output=}\n')

    string = 'pwwkew'
    output = s.lengthOfLongestSubstring(string)
    print(f'{string=}\n{output=}\n')

    string = 'dvdf'
    output = s.lengthOfLongestSubstring(string)
    print(f'{string=}\n{output=}')


if __name__ == '__main__':
    test()
