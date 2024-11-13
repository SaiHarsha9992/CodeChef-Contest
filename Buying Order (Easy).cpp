#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

    int t;
    cin >> t;
    
    for(int l = 0; l < t; l++){
        int n;
    cin >> n;
    
    vector<int> arr(n+1);
    
    for(int i = 1; i <= n; i++){
        cin >> arr[i];
    }
    
    int co = 0;
    for(int i = 1; i < n; i++){
        if(arr[i] == 1) co++;
    }
    
    int cz = 0;
    for(int i = 2; i <= n; i++){
        if(arr[i] == 0) cz++;
    }
    
    int minc = min(co + cz, n-1);
    
    int toc = n+minc;
    
    cout << toc << endl;
    }
}
