#include <iostream>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) return s;
        string res;
        int step = 2 * numRows - 2, n = s.length();
        for (int i = 0; i < numRows; ++i) {
            for (int j = i; j < n; j += step) {
                res += s.at(j);
                int pos = j + step - 2 * i;
                if (i != 0 && i != numRows -1 && pos < n) res += s.at(pos);
            }
        }
        return res;
    }
};

int main() {
    Solution soln;
    string s = "123456789ABCDEF";
    int numRows = 4;
    string res = soln.convert(s, numRows);
    cout << "s: " << s << endl;
    cout << "numRows: " << numRows << endl;
    cout << "result: " << res << endl;
    return 0;
}

/* 123456789ABCDEF
 * 1     7     D
 * 2   6 8   C E
 * 3 5   9 B   F
 * 4     A       */
