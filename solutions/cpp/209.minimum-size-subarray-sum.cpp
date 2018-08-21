#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if (nums.empty()) return 0;
        int left = 0, right = 0, sum = 0, n = nums.size(), res = INT_MAX;
        while (right < n) {
            while (sum < s && right < n) {
                sum += nums[right++];
            }
            while (sum >= s) {
                res = min(res, right - left);
                sum -= nums[left++];
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};

void printVector(const vector<int>& v) {
   for (int i=0; i < v.size(); ++i) cout << v.at(i) << ' ';
   cout << endl;
   return;
}

int main() {
    Solution soln;
    int s = 7;
    vector<int> nums = {2, 3, 1, 2, 4, 3};
    int res = soln.minSubArrayLen(s, nums);
    cout << "s: " << s << endl;
    cout << "nums: ";
    printVector(nums);
    cout << "result: " << res << endl;
    return 0;
}
