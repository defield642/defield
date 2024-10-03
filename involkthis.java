//Using 'this' keyword for involking current class method
class Myclass{
    void method1(){
        System.out.println("Method 1");

    }

    void method2(){
        System.out.println("Method 2");
        this.method1();//calling method1 of the current class
    }

public static void main(String[] args){
    Myclass obj = new Myclass();
    obj.method2();
}
}