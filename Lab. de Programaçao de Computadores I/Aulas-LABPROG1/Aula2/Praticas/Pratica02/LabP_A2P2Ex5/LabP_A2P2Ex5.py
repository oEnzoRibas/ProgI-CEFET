"""
CEFET-MG - Laboratorio de Programação de Computadores 1
Prática 2 da Aula 2 - Estrutura Sequencial e Condicional
Grupo - Alunos: Sofia Guimarães, Enzo Ribas, Rafael Aquino, Alexandre Silva
Turma Mecânica T13 de Quinta-Feira de 10:40 às 12:20.
Código em Python para o exemplo 1.

5)  Faça  um  programa  em  Python  para  mostrar  o  menu  de  opções,  a  seguir.  O 
algoritmo  deve  receber  a  opção  do  usuário  e  os  dados  necessários  para  executar  cada 
operação disponível no menu. Obs.: Verifique se a operação é possível com os números 
fornecidos, exemplo, se a divisão é por 0 (zero) imprimir uma mensagem de “Erro” na tela. 
Menu de Opções: 
A. A potencia de um número por 2; 
B. A potencia de um número X por um número Y; 
C. A divisão de dois números inteiros; 
D. A multiplicação de dois números de ponto flutuante.
"""

print("--------- MENU ---------\n"
      "A - X^2 (inteiro)\n"
      "B - X^Y (inteiros)\n"
      "C - X/Y (inteiros)\n"
      "D - X*Y (flutuantes)\n"
      "------------------------")
opcao = input("Escolha uma opção: ")

if opcao == "A" or opcao == "a":
    base = int(input("Digite a base: "))
    resultado = base**2
    print(f"O resultado {base}^2 é: {resultado}")

elif opcao == "B" or opcao == "b":
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    resultado = base**expoente
    print(f"O resultado de {base}^{expoente} é {resultado}")

elif opcao == "C" or opcao == "c":
    divisor = int(input("Digite o divisor: "))
    dividendo = int(input("Digite o dividendo: "))
    if dividendo == 0:
        print(f"Erro!")
    else:
        resultado = divisor/dividendo
        print(f"O resultado de {divisor}/{dividendo} é {resultado}")

elif opcao == "D" or opcao == "d":
    fator1 = float(input("Digite o primeiro fator: "))
    fator2 = float(input("Digite o segundo fator: "))
    resultado = fator1*fator2
    print(f"O resultado de {fator1}*{fator2} é {resultado}")

else:
    print(f"Opção invalida")