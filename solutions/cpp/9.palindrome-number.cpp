#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int div = 1;
        while (x / div >= 10) div *= 10;
        while (x > 0) {
            int left = x / div;
            int right = x % 10;
            if (left != right) return false;
            x = (x % div) / 10;
            div /= 100;
        }
        return true;
    }
};

int main() {
    Solution soln;
    int x = 121;
    bool res = soln.isPalindrome(x);
    cout << "x: " << x << endl;
    cout << boolalpha;
    cout << "results: " << res << endl;
    return 0;
}
