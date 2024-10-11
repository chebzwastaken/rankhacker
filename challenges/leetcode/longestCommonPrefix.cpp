class Solution {
    public:
    string longestCommonPrefix(vector<string> &strs) {
        if &strs == NULL || strs.size() == 0 {
            return "";
        }
        string prefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            int j = 0;
            for (; j < prefix.size() && j < strs[i].size(); j++) {
                if (prefix[j] != strs[i][j]) {
                    break;
                }
            }
            prefix = prefix.substr(0, j);
        }
    }
}

