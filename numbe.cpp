/*program that prints the numbers from 1 to 100 for multiples of 3,print "Fizz",
for multiples of 5, print "buzz", and for numbers that are multiples of both 3 and 5, print "FizzBuzz"
*/
#include<iostream>
using namespace std;
class MyNubers{
    public:
    MyNubers(){}
        void printnum(){
            for(int i=1;i<=100;i++){
                cout<<i<<endl;
                if(i%3==0){
                    cout<<"Fizz"<<endl;
                }
                else if(i%5==0){
                    cout<<"Buzz"<<endl;
                }
                else if(i%3==0 && i%5==0){
                    cout<<"FizzBuzz"<<endl;
                }
                else{
                cout<<i<<endl;
                }
            }
        }
    

};
int main(){
    MyNubers obj;
    obj.printnum();
    return 0;
}