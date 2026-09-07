#include "iostream"
#include "unordered_map"

using namespace std;

int main(){
    std::cout << "dc" << std::endl;

    int n =5;
    int m =5;
    int map[n][m] = {{1,0,0,0,0},
                     {1,0,0,0,9},
                     {1,0,5,0,0},
                     {1,0,0,7,0},
                     {1,0,3,0,0},
                     };

    cout << "val : " << map[1][1]<< endl;

    for(int i = 0; i < n; i++){
        for (int j =0; j < m; j++){
            if(map[i][j] >= 5) cout << "hi" << endl;
        }
    }
    
}