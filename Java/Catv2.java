package Java;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Catv2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome completo: ");
        String nome = scanner.nextLine();

        System.out.print("Digite sua data de nascimento (Dia/Mês/Ano): ");
        String dataNascimentoStr = scanner.next();
        LocalDate dataNascimento = LocalDate.parse(dataNascimentoStr, DateTimeFormatter.ofPattern("dd/MM/yyyy"));

        System.out.print("Digite sua altura (em metros): ");
        double altura = scanner.nextDouble();

        System.out.print("Digite seu peso (em quilogramas): ");
        double peso = scanner.nextDouble();

        int idade = calcularIdade(dataNascimento);

        double imc = calcularIMC(peso, altura);

        System.out.println("\nOlá, " + nome + "!");
        System.out.println("Você tem " + idade + " anos de idade.");
        System.out.println("Seu Índice de Massa Corporal (IMC) é: " + imc);

        scanner.close();

    }

    public static int calcularIdade(LocalDate dataNascimento) {
        LocalDate hoje = LocalDate.now();
        return hoje.getYear() - dataNascimento.getYear();
    }

    public static double calcularIMC(double peso, double altura) {
        return peso / (altura * altura);
    }

}
