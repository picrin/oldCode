#include <iostream>

using namespace std;

int t[10];

int f(int lewy, int prawy, int szuk)
{
	if (lewy==prawy)
	{
		if(t[lewy]==szuk)
		return lewy;
		return -1;
	}
	
	else
	{
		int sr = (prawy-lewy)/2+lewy;
		int w1 = f(lewy, sr, szuk);
		int w2 = f(sr+1, prawy, szuk);
		if(w1!=-1) return w1;
		if(w2!=-1) return w2;
		return -1;
	}
}

int main()
{
	cout<<"podaj zmienna do wyszukania: ";
	int szuk;
	cin>>szuk;
	cout<<endl;
	cout<<"podaj elementy tablicy:"<<endl;
	for(int i=0; i<=9; i++) cin>>t[i];
	int k=0;
	int l;
	int lewy;
	
	for(l=0; l<=9; l++)
	{
		lewy=f(0,9,szuk);
		if (lewy!=-1)
		{
			t[lewy]=t[lewy]-1;
			k++;
		}
	}
	
	cout<<lewy<<endl;
	cout<<k<<endl;
	system( "pause>nul" );
	return 0;
}
