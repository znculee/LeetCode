# 2. Add Two Numbers

import copy


class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        next_add = 0
        header = l1
        current = None
        while l1 and l2:
            temp_sum = l1.val + l2.val + next_add
            l1.val = temp_sum % 10
            next_add = temp_sum // 10
            current = l1
            l1 = l1.next
            l2 = l2.next

        if l2:
            current.next = l2

        while next_add:
            if not current.next:
                current.next = ListNode(next_add)
                return header
            else:
                current = current.next
                temp_sum = current.val + next_add
                current.val = temp_sum % 10
                next_add = temp_sum // 10
        return header

def printLinkedList(l):
    while True:
        print(l.val, end='')
        l = l.next
        if l is not None:
            print('->', end='')
        else:
            break
    print()

def test():
    s = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = s.addTwoNumbers(copy.deepcopy(l1), copy.deepcopy(l2))
    print('l1: ', end='')
    printLinkedList(l1)
    print('l2: ', end='')
    printLinkedList(l2)
    print('res: ', end='')
    printLinkedList(result)


if __name__ == '__main__':
    test()
