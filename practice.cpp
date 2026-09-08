#include "iostream"
#include "unordered_map"
#include <array>
#include <queue>
#include <unordered_map>
#include "vector"
#include "queue"

using namespace std;
struct val
{
    double x,y,dist = 0;  
};

double compare(val a, val b){
    double diff =  a.x - b.x;
    return diff;
}
int main(){
    int map[5][5] = {{0,0,0,0,0},
                     {0,1,0,0,0},
                     {0,0,2,0,0},
                     {0,0,0,0,0},
                     {0,0,0,0,0},}; 
    // priority_queue<int>
    vector<val> openList;
    val a = {5, 0, 0};
    val b = {9, 0, 0};
    double x = compare(a, b);

    cout << "diff :" << x << endl;

    
}