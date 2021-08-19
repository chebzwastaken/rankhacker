class HelloWorld {
    public static void main(String[] args){
       for (int i = 1; i <= 30; ++i ){
           condit(i);
       }
    }
    
    public static void condit(int n){
        if (n % 2 == 0 && n >= 2 && n <= 5){
            System.out.println("Not Wierd");
        }
        else if (n % 2 == 0 && n > 20){
            System.out.println("Not Wierd");
        }
        else {
            System.out.println("Wierd");
        }

        
    }

    // modifier static returnType nameOfMethod (parameter1, parameter2, ...) {
    //   method body
    // }
}