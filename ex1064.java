import java.util.Scanner;
public class ex1064 {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        float x, s = 0, m;
        int n = 0;
        for (int i = 0; i < 6; i++) {
            x = leitor.nextFloat();
            if (x > 0) {
                n++;
                s = s + x;
            }
        }
        m = s / n;
        System.out.print(n + " valores positivos");
        System.out.println();
        System.out.printf("%.1f", m);
        System.out.println();
    }
}
