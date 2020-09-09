#include<iostream>
using namespace std;
int main()
{
    int n,k,no_tf=0,no_ff=0;
    
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>k;
        if(k==25)
        {
        
            no_tf++;
        }
        else if(k==50)
        {
            if(no_tf>=1)
            {
                no_tf--;
                 
                cout<<no_ff;
                
            }
            else{
                cout<<"NO";
                return 0;
           

            }
         no_ff++;
        }
        else if(k==100)
        {
            if(no_ff>=1 && no_tf>=1)
            {
                no_tf--;
                no_ff--;
            }
            else if(no_ff==0 && no_tf>=3)
            {
                no_tf-=3;
            }
            else{
               
                cout<<"NO";
                return 0;
            }

        }
         
    }
  cout<<"YES";
}