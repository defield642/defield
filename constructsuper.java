//use 'super' to call constructor of parent class 
class Parent{
    Parent(int x){
        System.out.println("Parent constructor with parameter"+ x);
    }
}
class Child extends Parent{
    Child(int y){
        super(y);// calling parent class constructor
        System.out.println("Child constructor");
    }
}