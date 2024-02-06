import java.util.Scanner;
public class ex1066 {
    public static void main(String[] args) {
        int n = 0, x, p = 0, i = 0, pos = 0, neg = 0;
        Scanner sc = new Scanner(System.in);
        while(n < 5){
            x = sc.nextInt();
            if (x % 2 == 00) {
                p++;
            }
            else {
                i++;
            }
            if(x > 0){
                pos++;
            }
            if (x < 0){
                neg++;
            }
            n++;
        }
        System.out.println(p + " valor(es) par(es)");
        System.out.println(i + " valor(es) impar(es)");
        System.out.println(pos + " valor(es) positivo(s)");
        System.out.println(neg + " valor(es) negativo(s)");
    }
}
