#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode();
        ListNode *head = dummy;
        int carry = 0;
        while (l1 || l2) {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            int sum = val1 + val2 + carry;
            carry = sum / 10;
            head->next = new ListNode(sum % 10);
            head = head->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        if (carry) head->next = new ListNode(1);
        return dummy->next;
    }
};

void printLinkedList(const ListNode* l) {
    const ListNode *head = l;
    if (head == nullptr) {
        cout << endl;
        return;
    }
    while (head != nullptr) {
        cout << head->val;
        head = head->next;
        if (head != nullptr) {
            cout << "->";
        }
    }
    cout << endl;
    return;
}

ListNode* createLinkedList(const string& nums) {
    ListNode *temp = nullptr;
    ListNode *res = nullptr;
    for (int i = nums.length() - 1; i >= 0; i--) {
        int n = nums.at(i) - '0';
        res = new ListNode(n, temp);
        temp = res;
    }
    return res;
}

int main() {
    Solution soln;
    string l1_nums = "243";
    ListNode *l1 = createLinkedList(l1_nums);
    string l2_nums = "564";
    ListNode *l2 = createLinkedList(l2_nums);
    ListNode *res = soln.addTwoNumbers(l1, l2);
    cout << "l1: ";
    printLinkedList(l1);
    cout << "l2: ";
    printLinkedList(l2);
    cout << "result: ";
    printLinkedList(res);
    return 0;
}
