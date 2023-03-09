using namespace std;
#include <bitset>/stdc++.h>
#include <iostream>
#define nxt(type) ({type x; cin >> x; x;})
#define nextline() ({string s; while(s.empty())getline(cin, s);s;})
int main(){
    string vals = nxt(string);
    int n = vals.size();
    int* games_won = new int[n];
    int* games_lost = new int[n];
    int* a_count = new int[n];
    int* b_count = new int[n];
    for( int i = 0; i< n; i++){
        games_won[i]= 0;
        games_lost[i]=0;
        a_count[i]=0;
        b_count[i] = 0;
    }
    for (int i = 0; i<n; i++){
        for (int j = 0; j< n; j++){
            if(vals[i] == 'A'){
                a_count[j] +=1;
                a_count[j] = a_count[j] % (j+1);
                if(a_count[j] ==0){
                    games_won[j] +=1;
                    b_count[j] =0;
                }
            }
            else{
                b_count[j] +=1;
                b_count[j] = b_count[j] % (j+1);
                if(b_count[j] ==0){
                    games_won[j] +=1;
                    a_count[j] =0;
                }
            }
        }
    }
    int sum = 0;
    for(int i =0; i<n; i++){
        if(games_won[i]> games_lost[i]){
            sum+=1; 
        }
    }
    if(sum > 0){
        cout << sum << '/n';
        for(int i =0; i<n; i++){
        if(games_won[i]> games_lost[i]){
             cout << i+1 << ' ';
        }
    }
    }
    cout << '\n';





}