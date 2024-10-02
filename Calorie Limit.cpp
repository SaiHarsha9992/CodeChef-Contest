#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	
	int t;
	cin >> t;
	
	for(int l = 0; l < t; l++){
	    int n, x;
	    cin >> n >> x;
	    
	    vector<int> v(n);
	    for(int i = 0; i < n; i++){
	        cin >> v[i];
	    }
	    
	    int s = 0, c = 0;
	    
	    for(int i = 0; i < n; i++){
	        if(s + v[i] > x){
	            break;
	        }
	        s += v[i];
	        c += 1;
	    }
	    cout << c << endl;
	}

}
