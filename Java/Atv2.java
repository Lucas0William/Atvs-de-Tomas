package Java;

import java.util.Scanner;

public class Atv2 {
    
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);

        String nome;
        int dia;
        int mes;
        int anos;
        double alt;
        double peso;
        double tot;

        System.out.println("Insira seu nome: ");
        nome = s.nextLine();

        System.out.println("Insira o dia do seu nascimento: ");
        dia = s.nextInt();

        System.out.println("Insira o mes do seu nascimento: ");
        mes = s.nextInt();
        
        System.out.println("Insira o ano do seu nascimento: ");
        anos = s.nextInt();
        anos = 2024 - anos;

        System.out.println("insira sua altura atual: ");
        alt = s.nextDouble();

        System.out.println("insira seu peso atual: ");
        peso = s.nextDouble();

        tot = peso / (Math.pow(alt, 2));

        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");

        System.out.println("Saudações " + nome + ", Seja bem vindo ao seu cálculo de IMC!");
        
        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");

        System.out.println("Você tem " + anos + " anos");

        System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");

        System.out.println();
        System.out.println("O seu calculo de IMC teve um resultado de: " + tot);

        if(tot <= 18.5) {

            System.out.println("Com esse resultado, você está em situação de magreza!");
            System.out.println();

        } else if (tot > 18.5 && tot < 25) {

            System.out.println("Com esse resultado você está em situação Normal!");
            System.out.println();

        } else if (tot >= 25 && tot < 30) {

            System.out.println("Com esse resultado, você está em situação de Sobrepeso!");
            System.out.println();

        } else if (tot >= 30 && tot < 40 ) {

            System.out.println("Cuidado! com esse resultado você está em situação de Obesidade!");
            System.out.println();

        } else {

            System.out.println("Cuidado! com esse resultado você está em situação de Obesidade grave");
            System.out.println();

        }

        s.close();
        
    }
}