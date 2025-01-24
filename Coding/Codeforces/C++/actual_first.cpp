#include <iostream>
using namespace std;
int main()
{
	int tests;
	cin>>tests;
	int n;
	for(int i = 0; i < tests; i++)
	{
		int Janswer;
		int afterJanswer;
		cin>>n;
		if(n % 2 == 0)
		{
			for(int j = 1; j < n; j+=2)
			{
				cout<<"? "<<j<<" "<<(j+1)<<endl;
				cin>>Janswer;
				int x;
				cout<<"? "<<(j+1)<<" "<<j<<endl;
				cin>>x;
				Janswer = Janswer*10 + x;
				if(Janswer != 0 && Janswer != 11)
				{
					if(j != 1)
					{
						cout<<"? "<<(j-1)<<" "<<j<<endl;
						cin>>afterJanswer;
						int y;
						cout<<"? "<<j<<" "<<(j-1)<<endl;
						cin>>y;
						afterJanswer = afterJanswer*10 + y;
						if(afterJanswer != 0 && afterJanswer != 11)
							cout<<"! "<<j<<endl;
						else
							cout<<"! "<<(j+1)<<endl;
						break;
					}
					else
					{
						cout<<"? 2 3"<<endl;
						cin>>afterJanswer;
						int y;
						cout<<"? 3 2"<<endl;
						cin>>y;
						afterJanswer = afterJanswer*10 + y;
						if(afterJanswer != 0 && afterJanswer != 11)
							cout<<"! 2"<<endl;
						else
							cout<<"! 1"<<endl;
						break;
					}
				}
			}
		}
		else
		{
			bool done = false;
			for(int j = 1; j < n-1; j+=2)
			{
				cout<<"? "<<j<<" "<<(j+1)<<endl;
				cin>>Janswer;
				int x;
				cout<<"? "<<(j+1)<<" "<<j<<endl;
				cin>>x;
				Janswer = Janswer*10 + x;
				if(Janswer != 0 && Janswer != 11)
				{
					if(j != 1)
					{
						cout<<"? "<<(j-1)<<" "<<j<<endl;
						cin>>afterJanswer;
						int y;
						cout<<"? "<<j<<" "<<(j-1)<<endl;
						cin>>y;
						afterJanswer = afterJanswer*10 + y;
						if(afterJanswer != 0 && afterJanswer != 11)
							cout<<"! "<<j<<endl;
						else
							cout<<"! "<<(j+1)<<endl;
						done = true;
						break;
					}
					else
					{
						cout<<"? 2 3"<<endl;
						cin>>afterJanswer;
						int y;
						cout<<"? 3 2"<<endl;
						cin>>y;
						afterJanswer = afterJanswer*10 + y;
						if(afterJanswer != 0 && afterJanswer != 11)
							cout<<"! 2"<<endl;
						else
							cout<<"! 1"<<endl;
						done = true;
						break;
					}
				}
			}
			if(!done)
				cout<<"! "<<n<<endl;
		}
	}
}