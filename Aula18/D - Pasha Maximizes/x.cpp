#include <bits/stdc++.h>
#define re return
#define ll long long
#define ld long double
#define f first
#define s second
#define pi acos(-1)
#define oo (ll)1e9
#define OO (ll)1e18
#define EPS 1e-7
#define FX(n) fixed<<setprecision(n)
#define mm(o,k) memset(o,k,sizeof o)
#define IO ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0);
using namespace std;
const int maxn=200005;
int main()
{
    IO;
    string s;
    int k;
    cin >> s >> k;
    int n=s.size();
    for(int i=0; i<n; ++i)
    {
        int Max=s[i]-'0';
        int idx=-1;
        int dis=0;
        for(int j=i+1; j<n; ++j)
        {
            if(s[j]-'0'>Max && k>=j-i)
            {
                idx=j;
                dis=j-i;
                Max=s[j]-'0';
            }
        }
        if(idx==-1)continue;
        k-=dis;
        for(int j=idx;j>i;--j)
            swap(s[j],s[j-1]);
    }
    cout<<s<<endl;
    re 0;
}