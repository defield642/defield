public class Animal{
    Animal(){
        int age;
    }
        void eat(){
            System.out.println("Animal eat");
        }
        void move(){
            System.out.println("Animal moves");
        }

    
}
class Cow extends Animal{
    Cow(){}
    void sound(){
        System.out.println("Cow mouws");
    }
}
class culf extends Cow{
    void jump(){
        System.out.println("Culf jump");
    }
}
class MainClass{
    public static void main(String args[]){
        culf c = new culf();
        Animal b =new Animal();
        b.eat();
        b.move();
        c.sound();
        c.jump();
    }
}