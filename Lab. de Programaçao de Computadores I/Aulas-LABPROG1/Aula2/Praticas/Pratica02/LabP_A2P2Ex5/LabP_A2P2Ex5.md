```markdown
INÍCIO
    // Definição de variáveis
    
    DECLARE opcao COMO CARACTERE
    DECLARE base, expoente, dividendo, divisor COMO INTEIRO
    DECLARE fator1, fator2 COMO REAL
    DECLARE resultado COMO REAL

    ESCREVER "--------- MENU ---------"
    ESCREVER "A - X^2 (inteiro)"
    ESCREVER "B - X^Y (inteiros)"
    ESCREVER "C - X/Y (inteiros)"
    ESCREVER "D - X*Y (flutuantes)"
    ESCREVER "------------------------"
    
    ESCREVER "Escolha uma opção:"
    LER opcao

    SE opcao == "A" OU opcao == "a" ENTÃO
        ESCREVER "Digite a base:"
        LER base
        resultado <- base ^ 2
        ESCREVER "O resultado", base, "^2 é:", resultado

    SENÃO SE opcao == "B" OU opcao == "b" ENTÃO
        ESCREVER "Digite a base:"
        LER base
        ESCREVER "Digite o expoente:"
        LER expoente
        resultado <- base ^ expoente
        ESCREVER "O resultado de", base, "^", expoente, "é", resultado

    SENÃO SE opcao == "C" OU opcao == "c" ENTÃO
        ESCREVER "Digite o dividendo:"
        LER dividendo
        ESCREVER "Digite o divisor:"
        LER divisor
        SE divisor == 0 ENTÃO
            ESCREVER "Erro! Divisão por zero não é permitida."
        SENÃO
            resultado <- dividendo / divisor
            ESCREVER "O resultado de", dividendo, "/", divisor, "é", resultado
        FIMSE

    SENÃO SE opcao == "D" OU opcao == "d" ENTÃO
        ESCREVER "Digite o primeiro fator:"
        LER fator1
        ESCREVER "Digite o segundo fator:"
        LER fator2
        resultado <- fator1 * fator2
        ESCREVER "O resultado de", fator1, "*", fator2, "é", resultado

    SENÃO
        ESCREVER "Opção inválida"
    FIMSE

FIM
```


# Código em Python
```python
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

```
# Descrição
## O programa apresenta um menu de opções para o usuário, permitindo calcular a potência de um número, a divisão de dois números inteiros ou a multiplicação de dois números de ponto flutuante. O código verifica se a operação é válida, como evitar divisão por zero. A implementação foi testada com diferentes entradas e funcionou conforme esperado, exibindo os resultados corretos.

# Resultado
## Bem Sucedido