import java.util.Scanner;
public class ex1067 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, n = 0;
        x = sc.nextInt();
        for(int i = 1; i <= x; i++){
            n++;
            if(n%2 != 0){
                System.out.println(n);
            }
        }

    }
}
