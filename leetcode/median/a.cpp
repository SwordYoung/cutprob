#include <iostream>
#include <cassert>

using namespace std;

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a > b ? b : a;
}

class Solution {
private:
    int check(int A[], int m, int B[], int n, int i) {
        int j = (m+n+1)/2-i;
        if (j > 0 && i < m && B[j-1] > A[i]) {
            return 1;
        } else if (i > 0 && j < n && B[j] < A[i]) {
            return -1;
        }
        cout << "i is " << i << " j is " << j << endl;
        return 0;
    }
    double getMedian(int A[], int m, int B[], int n, int li) {
        int j = (m+n+1)/2-li;
        
        if ((m+n)%2 == 1) {
            return li == 0 ? B[j-1] : max(A[li-1], B[j-1]);
        }
        
        int n1 = 0;
        int n2 = 0;
        if (li == 0 || li == m) {
            n1 = j == 0 ? A[m-1] : B[j-1];
            n2 = B[j];
        cout << "n1 is " << n1 << " n2 is " << n2 << endl;
        } else {
            n1 = max(A[li-1], B[j-1]);
            n2 = min(A[li], B[j]);
        }
        cout << "i is " << li << " j is " << j << endl;
        cout << "n1 is " << n1 << " n2 is " << n2 << endl;
        return (double)(n1+n2) / 2.0;
    }
    
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        if (m > n) {
            return findMedianSortedArrays(B, n, A, m);
        }
        int li = 0;
        int ri = m+1;
        while (li < ri) {
            int mi = (li+ri)/2;
            cout << "l1 is " << li << " ri is " << ri << " mi is " << mi << endl;
            int check_cmp = check(A, m, B, n, mi);
            if (check_cmp == 0) {
                return getMedian(A, m, B, n, mi);
            } else if (check_cmp == 1) {
                li = mi+1;
            } else {
                ri = mi;
            }
        }
        return getMedian(A, m, B, n, li);
    }
};

int main() {
    int a[2] = {1, 3};
    int b[2] = {6, 7};
    cout << "result: " << Solution().findMedianSortedArrays(a, 2, b, 2) << endl;
    return 0;
}
