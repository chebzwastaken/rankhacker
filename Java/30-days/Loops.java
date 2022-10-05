public class Loops {

    public static void multiples(int n){
        for (int i = 1; i < 11; ++i){
            int x = n * i;
            System.out.println(String.format("%d x %d = %d", n, i, x));
        }
    }
    public static void main(String[] args) {
        multiples(3);
    }
}
