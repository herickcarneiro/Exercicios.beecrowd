import java.util.Scanner;
public class ex1070 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, c = 0;
        x = sc.nextInt();
        while (c < 6){
            if(x%2 != 0){
                System.out.println(x);
                c++;
            }
            x++;
        }
    }
}
