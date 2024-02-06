import java.util.Scanner;

public class ex1065 {
    public static void main(String[] args) {
        int n = 0, x, c =0;
        Scanner sc = new Scanner(System.in);
        while(n < 5){
            x = sc.nextInt();
            if (x % 2 == 00) {
                c++;
            }
            n++;
        }
        System.out.println((c + " valores pares"));
    }
}
