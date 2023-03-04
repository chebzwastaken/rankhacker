#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    int q;
    cin >> q;
    map<string, int> m;
    for (int i = 0; i < q; i++)
    {
        int y, x;
        string name;
        cin >> y >> name;
        if (y == 1)
        {
            cin >> x;
            map<string, int>::iterator itr = m.find(name);
            if (itr == m.end())
            {
                m.insert(pair<string, int>(name, x));
            }
            else
            {
                itr->second += x;
            }
        }
        else if (y == 2)
        {
            m.erase(name);
        }
        else
        {
            map<string, int>::iterator itr = m.find(name);
            if (itr == m.end())
                cout << "0" << endl;
            else
                cout << itr->second << endl;
        }
    }
    return 0;
}
