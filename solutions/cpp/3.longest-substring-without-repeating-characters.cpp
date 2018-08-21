#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) return 0;
        int res = 0, n = s.length();
        unordered_map<int, int> m;
        for (int left = -1, right = 0; right < n; ++right) {
            if (m.count(s[right]) && m[s[right]] > left) {
                left = m[s[right]];
            }
            m[s[right]] = right;
            res = max(res, right - left);
        }
        return res;
    }
};

int main() {
    Solution soln;
    string s = "abcabcbb";
    int res = soln.lengthOfLongestSubstring(s);
    cout << "string: " << s << endl;
    cout << "length of longest substring: " << res << endl;
    return 0;
}
