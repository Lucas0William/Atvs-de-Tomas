package Java;

import java.util.ArrayList;
import java.util.Scanner;

public class Vetor {

    public static void main(String[] args) {
        
        ArrayList<String> cpfs = new ArrayList<String>();
        ArrayList<String> nomes = new ArrayList<String>();
        ArrayList<Integer> medias = new ArrayList<Integer>();

        String nome = "";
        String cpf = "";
        String cpf_busca = "";
        int media = 0;
        boolean encontrado;

        int opcao;

        Scanner scan = new Scanner(System.in);

        while (true) {


            System.out.println("|---- Faculdade Nova Roma ----|");

            System.out.println("Escolha a opcao desejada:");
            System.out.println("1 - Criar Aluno");
            System.out.println("2 - Buscar Aluno");
            System.out.println("3 - Atualizar Aluno");
            System.out.println("4 - Remover Aluno");
            System.out.println("5 - Listar Tudo");
            System.out.println("9 - Sair");

            opcao = scan.nextInt();

            if (opcao == 1){
                System.out.println("Create");
                System.out.println("Digite o nome do aluno");
                nome = scan.next();
                System.out.println("Digite o cpf do aluno");
                cpf = scan.next();
                System.out.println("Digite a media do aluno");
                media = scan.nextInt();

                // add no arrayList
                cpfs.add(cpf);
                nomes.add(nome);
                medias.add(media);

                System.out.println("Aluno cadastrado com sucesso");
            }else if (opcao == 2){
                System.out.println("Read");

                System.out.println("Digite o cpf do aluno");
                cpf = scan.next();

                encontrado = false;
                for(int i = 0; i < cpfs.size(); i++){
                    cpf_busca = cpfs.get(i);
                    if (cpf_busca.equals(cpf)){
                        nome = nomes.get(i);
                        media = medias.get(i);
                        encontrado = true;
                        break;
                    }
                }
                
                if (encontrado){
                    System.out.println(cpf);
                    System.out.println(nome);
                    System.out.println(media);
                }else {
                    System.out.println("Aluno n encontrado");
                }
                

            }else if (opcao == 3){
                System.out.println("Update");
            }else if (opcao == 4){
                System.out.println("Delete");
            }else if(opcao == 5){
                System.out.println(cpfs);
                System.out.println(nomes);
                System.out.println(medias);
            }else if(opcao == 9){
                System.out.println("Saindo...");
                break;
            }else {
                System.out.println("Opcao invalida");
            }

            
        }
        
        

    }

    
}