#include<iostream>
using namespace std;
int main()
{
	int n,m;
	cin>>n>>m;
	int a=m+1,b=m+1;
	for(int i=n;i<m;++i)
		{
			if(i>(a+b)/2+1)
				break;
		for(int j=i+1;j<=m;j++)
			{
				if(i+j>a+b)
					break;
				if(i*j%(i+j)==0)
				{
					if(i+j<a+b)
					{
						a=i;
						b=j;
					}
					else if(i+j==a+b&&i<a)
					a=i;
					b=j;
				}
			}
		}
 } 
