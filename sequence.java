/*write a program to generate the fibonaacci sequence up to 100 */
public class Fibonacci{
    int a=0;
    int b=1;
    int c;
    int limit;
    Fibonacci(int limit)
    {
        this.limit=limit;
    }
    void sequence()
    {
        System.out.println("Fibonacci sequence up to "+limit+" is:");
        while(a<=limit){
            System.out.println(a);
            c=a+b;
            a=b;
            b=c;
        }
    }
public static void main(String[] args){
    Fibonacci obj = new Fibonacci(100);
    obj.sequence();
}
}