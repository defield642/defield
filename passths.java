// Using 'this' keyword for passing current object as parameter
class Myclass{
    AnotherClass obj;

    Myclass(){
        obj = new AnotherClass(this); // passing current object to anotherclass constructor
    }
}
class AnotherClass {
    MyClass ref;

    AnotherClass(MyClass ref) {
        this.ref = ref;
    }
}