// low bound stl 

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, q, x;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }
    cin >> q;
    for (int i = 0; i < q; i++) {
        cin >> x;
        vector<int>::iterator low = lower_bound(v.begin(), v.end(), x);
        if (v[low - v.begin()] == x) {
            cout << "Yes " << (low - v.begin() + 1) << endl;
        } else {
            cout << "No " << (low - v.begin() + 1) << endl;
        }
    }
    return 0;
}