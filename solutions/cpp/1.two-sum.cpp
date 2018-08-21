#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            if (m.count(nums[i])) {
                return {m[nums[i]], i};
            } else {
                m[diff] = i;
            }
        }
        return {};
    }
};

void printVector(const vector<int>& v) {
   for (int i=0; i < v.size(); ++i) cout << v.at(i) << ' ';
   cout << endl;
   return;
}

int main() {
    Solution soln;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> res = soln.twoSum(nums, target);
    cout << "nums: ";
    printVector(nums);
    cout << "target: " << target << endl;
    cout << "result: ";
    printVector(res);
    return 0;
}
