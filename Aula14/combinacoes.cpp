#include <iostream>
using namespace std;
#define ULL unsigned long long int
int S[5] = {1, 2, 3, 4, 5};
int N = 5;

void imprimeCombinacoes(bool combs[], int begin, int n) {
	if (begin >= n) {
		cout << '{' << ' ';
		for (int i = 0; i < n; i++) {
			if (combs[i]) //# Se comb[i] é True, então S[i] pertence ao subconjunto
				cout << S[i] << ' ';
		}
		cout << '}' << endl;
	} else {
		combs[begin] = 0;
		imprimeCombinacoes(combs, begin + 1, n);
		combs[begin] = 1;
		imprimeCombinacoes(combs, begin + 1, n);
	}
}

void conjuntoDasPartes(int n) {
	for(ULL i = 0; i < (1LLU << n); i++) {
		cout << '{' << ' ';
		for (int j = 0; j < n; j++) {
			if (i & (1 << j))
				cout << S[j] << ' ';
		}
		cout << '}' << endl;
	}
}

int main() {
	bool combs[N];
	imprimeCombinacoes(combs, 0, N);
	cout << "---" << endl;
	conjuntoDasPartes(N);
}