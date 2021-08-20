public class Person {
    private int age;
    
    public Person(int initialAge){
        age = initialAge;
        if( initialAge < 0){
            initialAge = 0;
            System.out.println("Age is not valid, setting age to 0");
        }
    }

    public void amIOLd(){

        if (age < 13){
            System.out.println("You are young");
        }
        else if (age >= 13){
            System.out.println("You are a teenager");
        }
        else{
            System.out.println("You are old");
        }
    }

    public void yearPasses(){
        age++;
        System.out.println(age);
    }

    public static void main(String[] args) {
        Person obj = new Person(-1);
        int T = 2;
        for (int i = 0; i < T; ++i){
            obj.amIOLd();
            obj.yearPasses();
        }
    }
}
