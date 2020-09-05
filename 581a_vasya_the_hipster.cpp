#include<iostream>
using namespace std;
 
int main()
{
    int a,b;
 
    scanf("%d %d",&a,&b);
    printf("%d ",min(a,b));
    printf("%d",max((a-min(a,b))/2,(b-min(a,b))/2 ));
 
}