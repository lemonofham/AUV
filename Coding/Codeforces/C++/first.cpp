#include <iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	bool valid = true;
	int lucky = 0;
	while(n > 0)
	{
		if(n % 10 == 4 || n % 10 == 7)
			lucky += 1;
		n /= 10;
	}
	while(lucky > 0)
	{
		if(lucky % 10 != 4 || lucky % 10 != 7)
			valid = false;
		lucky /= 10;
	}
	if(valid)
		cout<<"YES";
	else
		cout<<"NO";
}