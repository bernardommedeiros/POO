import java.util.Scanner;

public class Ex01 {
    // classe principal do programa
    // o nome dado a ela é atribuido ao programa e deve iniciar com letra maiuscula
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();
        System.out.println(String.format("Seja bem-vindo, %s!", nome));
        scanner.close();
    }
}
