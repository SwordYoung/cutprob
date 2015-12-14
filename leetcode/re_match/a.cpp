#include <iostream>
#include <cassert>
#include <cstring>

using namespace std;

class Solution {
private:
    int has_star(const char *p, int j) {
        if (j >= strlen(p) + 1) {
            return 0;
        }
        if (p[j+1] == '*') {
            int sub_step = has_star(p, j+2);
            if (sub_step != 0) {
                if (p[j] == p[j+2]) {
                    return sub_step+2;
                }
            }
            return 2;
        }
        return 0;
    }
    bool isMatchFirst(const char *s, const char *p, int i, int j) {
        return i < strlen(s) && j < strlen(p) && (s[i] == p[j] || p[j] == '.');
    }
    bool isMatch(const char *s, const char *p, int i, int j) {
        cout << "matching: " << s << " and " << p << " i=" << i << " j=" << j << endl;
        if (j == strlen(p)) {
            return i == strlen(s);
        }
        int star_step = has_star(p, j);
        if (star_step != 0) {
            if (isMatchFirst(s, p, i, j)) {
                cout << "matching 3: " << s+i << " and " << p+j << " i=" << i << " j=" << j << endl;
                cout << "matching 3.1: " << s+i+1 << " and " << p+j+2 << " i=" << i << " j=" << j << endl;
                cout << "matching 3.2: " << s+i+1 << " and " << p+j << " i=" << i << " j=" << j << endl;
                return isMatch(s, p, i+1, j+star_step) || isMatch(s, p, i, j+star_step) || isMatch(s, p, i+1, j);
            } else {
                cout << "matching 4: " << s << " and " << p << " i=" << i << " j=" << j << endl;
                return isMatch(s, p, i, j+star_step);
            }
        } else {
            cout << "matching 2: " << s << " and " << p << " i=" << i << " j=" << j << endl;
            if (isMatchFirst(s, p, i, j)) {
                return isMatch(s, p, i+1, j+1);
            } else {
                return false;
            }
        }
        assert(0);
        return true;
    }
    
public:
    bool isMatch(const char *s, const char *p) {
        return isMatch(s, p, 0, 0);
    }
};


int main() {
    cout << "is match " << Solution().isMatch("aaaaaaaaaaaab", "a*c") << endl;
    cout << "is match " << Solution().isMatch("aaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*c") << endl;
    return 0;
}
