#include <iostream>
using namespace std;
int main()
{
	int n;
	int Janswer;
	int afterJanswer;
	cout<<"How many players?"<<endl;
	cin>>n;
	int A[n];
	int imposter;
	bool B[n];
	cout<<"How many knights?"<<endl;
	int x;
	cin>>x;
	if(x != 0)
		cout<<"Enter numbers of knights : "<<endl;
	for(int j = 0; j < x; j++)
	{
		int y;
		cin>>y;
		A[y-1] = 1;
		B[y-1] = true;
	}
	int y = n - x - 1;
	if(y != 0)
	{
		cout<<"Enter number of imposter : "<<endl;
		cin>>imposter;
		A[imposter-1] = 2;
		B[imposter-1] = true;
		for(int j = 0; j < n; j++)
			if(!B[j])
				A[j] = 0;
	}
	else
	{
		for(int j = 0; j < n; j++)
		{
			if(!B[j])
			{
				imposter = j + 1;
				A[j] = 2;
			}
		}
	}
	if(n % 2 == 0)
	{
		for(int j = 1; j < n; j+=2)
		{
			cout<<"? "<<j<<" "<<(j+1)<<endl;
			if(A[j-1] == A[j])
				Janswer = 1;
			else if(A[j-1] == 2 && A[j] == 0)
				Janswer = 1;
			else if(A[j-1]*A[j] == 0)
				Janswer = 0;
			else if(A[j-1] == 2)
				Janswer = 0;
			else
				Janswer = 1;
			cout<<Janswer<<endl;
			int x;
			cout<<"? "<<(j+1)<<" "<<j<<endl;
			if(A[j] == A[j-1])
				x = 1;
			else if(A[j] == 2 && A[j-1] == 0)
				x = 1;
			else if(A[j]*A[j-1] == 0)
				x = 0;
			else if(A[j] == 2)
				x = 0;
			else
				x = 1;
			cout<<x<<endl;
			Janswer = Janswer*10 + x;
			if(Janswer != 0 && Janswer != 11)
			{
				if(j != 1)
				{
					cout<<"? "<<(j-1)<<" "<<j<<endl;
					if(A[j-2] == A[j-1])
						afterJanswer = 1;
					else if(A[j-2] == 2 && A[j-1] == 0)
						afterJanswer = 1;
					else if(A[j-2]*A[j-1] == 0)
						afterJanswer = 0;
					else if(A[j-2] == 2)
						afterJanswer = 0;
					else
						afterJanswer = 1;
					cout<<afterJanswer<<endl;
					int y;
					cout<<"? "<<j<<" "<<(j-1)<<endl;
					if(A[j-1] == A[j-2])
						y = 1;
					else if(A[j-1] == 2 && A[j-2] == 0)
						y = 1;
					else if(A[j-1]*A[j-2] == 0)
						y = 0;
					else if(A[j-1] == 2)
						y = 0;
					else
						y = 1;
					cout<<y<<endl;
					afterJanswer = afterJanswer*10 + y;
					if(afterJanswer != 0 && afterJanswer != 11)
					{
						cout<<"! "<<j<<endl;
						if(j == imposter)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					else
					{
						cout<<"! "<<(j+1)<<endl;
						if(j == imposter - 1)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					break;
				}
				else
				{
					cout<<"? 2 3"<<endl;
					if(A[1] == A[2])
						afterJanswer = 1;
					else if(A[1] == 2 && A[2] == 0)
						afterJanswer = 1;
					else if(A[1]*A[2] == 0)
						afterJanswer = 0;
					else if(A[1] == 2)
						afterJanswer = 0;
					else
						afterJanswer = 1;
					cout<<afterJanswer<<endl;
					int y;
					cout<<"? 3 2"<<endl;
					if(A[2] == A[1])
						y = 1;
					else if(A[2] == 2 && A[1] == 0)
						y = 1;
					else if(A[2]*A[1] == 0)
						y = 0;
					else if(A[2] == 2)
						y = 0;
					else
						y = 1;
					cout<<y<<endl;
					afterJanswer = afterJanswer*10 + y;
					if(afterJanswer != 0 && afterJanswer != 11)
					{
						cout<<"! 2"<<endl;
						if(2 == imposter)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					else
					{
						cout<<"! 1"<<endl;
						if(1 == imposter)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					break;
				}
			}
		}
	}
	else
	{
		bool done = false;
		for(int j = 1; j < n; j+=2)
		{
			cout<<"? "<<j<<" "<<(j+1)<<endl;
			if(A[j-1] == A[j])
				Janswer = 1;
			else if(A[j-1] == 2 && A[j] == 0)
				Janswer = 1;
			else if(A[j-1]*A[j] == 0)
				Janswer = 0;
			else if(A[j-1] == 2)
				Janswer = 0;
			else
				Janswer = 1;
			cout<<Janswer<<endl;
			int x;
			cout<<"? "<<(j+1)<<" "<<j<<endl;
			if(A[j] == A[j-1])
				x = 1;
			else if(A[j] == 2 && A[j-1] == 0)
				x = 1;
			else if(A[j]*A[j-1] == 0)
				x = 0;
			else if(A[j] == 2)
				x = 0;
			else
				x = 1;
			cout<<x<<endl;
			Janswer = Janswer*10 + x;
			if(Janswer != 0 && Janswer != 11)
			{
				if(j != 1)
				{
					cout<<"? "<<(j-1)<<" "<<j<<endl;
					if(A[j-2] == A[j-1])
						afterJanswer = 1;
					else if(A[j-2] == 2 && A[j-1] == 0)
						afterJanswer = 1;
					else if(A[j-2]*A[j-1] == 0)
						afterJanswer = 0;
					else if(A[j-2] == 2)
						afterJanswer = 0;
					else
						afterJanswer = 1;
					cout<<afterJanswer<<endl;
					int y;
					cout<<"? "<<j<<" "<<(j-1)<<endl;
					if(A[j-1] == A[j-2])
						y = 1;
					else if(A[j-1] == 2 && A[j-2] == 0)
						y = 1;
					else if(A[j-1]*A[j-2] == 0)
						y = 0;
					else if(A[j-1] == 2)
						y = 0;
					else
						y = 1;
					cout<<y<<endl;
					afterJanswer = afterJanswer*10 + y;
					if(afterJanswer != 0 && afterJanswer != 11)
					{
						cout<<"! "<<j<<endl;
						if(j == imposter)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					else
					{
						cout<<"! "<<(j+1)<<endl;
						if(j == imposter - 1)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					done = true;
					break;
				}
				else
				{
					cout<<"? 2 3"<<endl;
					if(A[1] == A[2])
						afterJanswer = 1;
					else if(A[1] == 2 && A[2] == 0)
						afterJanswer = 1;
					else if(A[1]*A[2] == 0)
						afterJanswer = 0;
					else if(A[1] == 2)
						afterJanswer = 0;
					else
						afterJanswer = 1;
					cout<<afterJanswer<<endl;
					int y;
					cout<<"? 3 2"<<endl;
					if(A[2] == A[1])
						y = 1;
					else if(A[2] == 2 && A[1] == 0)
						y = 1;
					else if(A[2]*A[1] == 0)
						y = 0;
					else if(A[2] == 2)
						y = 0;
					else
						y = 1;
					cout<<y<<endl;
					afterJanswer = afterJanswer*10 + y;
					if(afterJanswer != 0 && afterJanswer != 11)
					{
						cout<<"! 2"<<endl;
						if(2 == imposter)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					else
					{
						cout<<"! 1"<<endl;
						if(1 == imposter)
							cout<<"Code Correct"<<endl;
						else
							cout<<"Code Incorrect"<<endl;
					}
					done = true;
					break;
				}
			}
		}
		if(!done)
		{
			cout<<"! "<<n<<endl;
			if(n == imposter)
				cout<<"Code Correct"<<endl;
			else
				cout<<"Code Incorrect"<<endl;
		}
	}
}