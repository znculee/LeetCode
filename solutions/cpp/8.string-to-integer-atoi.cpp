#include <iostream>

using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        if (s.empty()) return 0;
        int sign = 1, base = 0, i = 0, n = s.length();
        while (i < n && s.at(i) == ' ') ++i;
        if (i < n && (s.at(i) == '+' || s.at(i) == '-')) {
            sign = (s.at(i++) == '+') ? 1 : -1;
        }
        while (i < n && s.at(i) >= '0' && s.at(i) <= '9') {
            if (base > INT_MAX / 10 || (base == INT_MAX / 10 && s.at(i) - '0' > 7)) {
                // INT_MAX == 2147483647, INT_MIN = -2147483648
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            base = 10 * base + (s.at(i++) - '0');
        }
        return base * sign;
    }
};

int main() {
    Solution soln;
    string s = "42";
    int res = soln.myAtoi(s);
    cout << "str: " << s << endl;
    cout << "result: " << res << endl;
    return 0;
}
