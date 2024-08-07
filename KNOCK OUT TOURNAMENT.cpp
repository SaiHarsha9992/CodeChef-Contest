#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
    
    int t;
    cin >> t;
    for(int l = 0; l < t; l++){
        vector<pair<int,int>>v(16);
        vector<int>ans(16);
        
        for(int i = 0; i < 16; i++){
            cin>>v[i].first;
            v[i].second = i;
        }
        
        sort(v.begin(), v.end());
        
        for(int i = 0; i < 16; i++){
            if(i == 0){
                ans[v[i].second] = 0;
            }
            else if(i <= 2){
                ans[v[i].second] = 1;
            }
            else if(i <= 6){
                ans[v[i].second] = 2;
            }
            else if(i <= 14){
                ans[v[i].second] = 3;
            }
            else{
                ans[v[i].second] = 4;
            }
        }
        for(int j = 0; j < 16; j++){
            cout << ans[j] << " ";
        }
    }
}
