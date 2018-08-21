# 28. Implement strStr()

class Solution_KMP:
    def strStr(self, haystack: str, needle: str) -> int:
        pmt = [0] # partial match table
        prefix = set()
        for i in range(1, len(needle)):
            prefix.add(needle[:i])
            surfix = {needle[j:i+1] for j in range(1, i+1)}
            pmt.append(max([len(x) for x in (prefix&surfix or {''})]))
        i = 0
        while i <= len(haystack)-len(needle):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    i += max(j - pmt[j-1], 1)
                    break
            else:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if  needle in haystack:
            length = len(needle)
            start_ind = [i for i,val in enumerate(haystack) if val==needle[0]]
            for i in start_ind:
                if haystack[i:i+length] == needle:
                    return i
        else:
            return -1


def test():
    s = Solution()

    haystack = "hello"
    needle = "ll"
    output = s.strStr(haystack, needle)
    print(f'{haystack=}\n{needle=}\n{output=}\n')

    haystack = "aaaaa"
    needle = "bba"
    output = s.strStr(haystack, needle)
    print(f'{haystack=}\n{needle=}\n{output=}\n')

    haystack = "mississippi"
    needle = "issi"
    output = s.strStr(haystack, needle)
    print(f'{haystack=}\n{needle=}\n{output=}\n')

    haystack = "mississippi"
    needle = "issip"
    output = s.strStr(haystack, needle)
    print(f'{haystack=}\n{needle=}\n{output=}\n')

    haystack = "abbabaaaabbbaabaabaabbbaaabaaaaaabbbabbaabbabaabbabaaaaababbabbaaaaabbbbaaabbaaabbbbabbbbaaabbaaaaababbaababbabaaabaabbbbbbbaabaabaabbbbababbbababbaaababbbabaabbaaabbbba"
    needle = "bbbbbbaa"
    output = s.strStr(haystack, needle)
    print(f'{haystack=}\n{needle=}\n{output=}')


if __name__ == '__main__':
    test()
