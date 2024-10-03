class ArithmeticException_Demo{
    public static void main(String() args){
        try{
            int a = 10, b = 0;
            int c = a/b;
            System.out.println("Result:" +c);
        }
        catch(ArithmeticException_Demo e)
        {
            System.out.println("Can't divide a number by zero");

        }
        try{
            int num = integer.persent("Edureka");
            System.out.println(num);
        }
    }
}