class MyClass{
    int Myvalue;
    void setValue(int Myvalue){
        this.Myvalue = Myvalue;
    }
    int getMyal(){
        return this.Myvalue;
    }
public static void main(String[] args){
    MyClass obj = new MyClass();
    obj.setValue(30);
    System.out.println("My value is:"+obj.getMyal());
   }
}