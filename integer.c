/*Write a program that takes an integer as input and returns true if input is a power of two.*/
#include<stdio.h>
#include<stdbool.h>

bool isPowerOfTtwo(int num){
//Checking if integer is greater than 0 and a set of bit of 1
    return(num>0) && ((num & (num - 1)) == 0);
}
int main(){
    int integer;
    printf("Enter your integer:\n");
    scanf("%d", &integer);

    if(isPowerOfTtwo(integer)){
        printf("%d => true",integer);
    }else{
        printf("%d => false",integer);
    }
    
    return 0;
}