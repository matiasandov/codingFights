//#include <bits/stdc++.h>

using namespace std;
#include <vector>


/*
 * Complete the 'reverseArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY a as parameter.
 */


vector<int> reverseArray(vector<int> a) {
    vector<int> result;
    for (int i = 1;i<=a.size(); i++) {
        result[i-1] = a[a.size()-i];
    }
    return result;
}


