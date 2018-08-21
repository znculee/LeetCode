# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        if x < 0:
            y = -1 * int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y <= max_int and y >= min_int:
            return y
        else:
            return 0


def test():
    s = Solution()

    x = 123
    output = s.reverse(x)
    print(f'{x=}\n{output=}\n')

    x = -123
    output = s.reverse(x)
    print(f'{x=}\n{output=}\n')

    x = 120
    output = s.reverse(x)
    print(f'{x=}\n{output=}')


if __name__ == '__main__':
    test()
