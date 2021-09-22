#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define LLI long long int

int n_items, W;
vector<vector <LLI>> items, F;

LLI MFKnapsack(LLI i, LLI j) {
    LLI value;
    if (F[i][j] < 0){
        if (j < items[i][0]){
            value = MFKnapsack(i - 1, j);
        } else {
            value = max(
                MFKnapsack(i - 1, j),
                items[i][1] + MFKnapsack(i - 1, j - items[i][0])
            );
        }
        F[i][j] = value;
    }
    return F[i][j];
}

int main(){

    cin >> n_items >> W;
    items = vector<vector <LLI>>(n_items + 1, vector<LLI>(2));

    for(int i = 1; i < (n_items + 1); i++) cin >> items[i][0] >> items[i][1];

    F = vector<vector <LLI>>(n_items + 1, vector<LLI>(W + 1, -1));
    for(int j = 0; j < (W + 1); j++)       F[0][j] = 0;
    for(int i = 0; i < (n_items + 1); i++) F[i][0] = 0;

    cout << MFKnapsack(n_items, W) << endl;
}