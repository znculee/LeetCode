#include <iostream>

using namespace std;

// Manacher's Algorithm
class Solution {
public:
    string longestPalindrome(string s) {
        string t = "^#";
        for (int i = 0; i < s.length(); ++i) {
            t += s[i];
            t += '#';
        }
        int p[t.length()], id = 0, mx = 0, resid = 0, resmx = 0;
        memset(p, 0, sizeof p);
        for (int i = 1; i < t.length(); ++i) {
            p[i] = mx > i ? min(p[2 * id - i], mx - i) : 1;
            while (t[i + p[i]] == t[i - p[i]]) ++p[i];
            if (mx < i + p[i]) {
                mx = i + p[i];
                id = i;
            }
            if (resmx < p[i]) {
                resmx = p[i];
                resid = i;
            }
        }
        return s.substr((resid - resmx) / 2, resmx - 1);
    }
};

/* Dynamic Programming
 * dp[i][j] = 1 if j == i
 * dp[i][j] = (s[i] == s[j]) if j = i + 1
 * dp[i][j] = ((s[i] == s[j] && dp[i + 1][j-1]) if j > i + 1 */
class SolutionDP {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        int n = s.length(), dp[n][n], left = 0, len = 1;
        memset(dp, 0, sizeof dp);
        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
            for (int j = 0; j < i; ++j) {
                dp[j][i] = (s[i] == s[j] && (i - j < 2 || dp[j + 1][i - 1]));
                if (dp[j][i] && len < i - j + 1) {
                    len = i - j + 1;
                    left = j;
                }
            }
        }
        return s.substr(left, len);
    }
};

int main() {
    Solution soln;
    string s = "babad";
    string res = soln.longestPalindrome(s);
    cout << "s: " << s << endl;
    cout << "result: " << res << endl;
    return 0;
}
