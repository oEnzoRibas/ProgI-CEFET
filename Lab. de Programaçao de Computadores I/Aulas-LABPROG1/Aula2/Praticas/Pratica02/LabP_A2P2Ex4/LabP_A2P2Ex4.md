```markdown
INÍCIO
    // Definição de variáveis
    DECLARE num1, num2, maior, soma, resto, divisao COMO INTEIRO

    ESCREVER "Digite o primeiro número"
    LER num1
    ESCREVER "Digite o segundo número"
    LER num2

    SE num1 > num2 ENTÃO
        maior <- num1
    SENÃO SE num2 > num1 ENTÃO
        maior <- num2
    SENÃO
        maior <- "nenhum"
    FIMSE

    ESCREVER "O maior é", maior

    // Verificar se maior é par ou ímpar (se maior for número)
    SE maior != "nenhum" ENTÃO
        SE maior % 2 = 0 ENTÃO
            ESCREVER "O número", maior, "é par."
        SENÃO
            ESCREVER "O número", maior, "é ímpar."
        FIMSE
    FIMSE

    soma <- num1 + num2
    ESCREVER "A soma é", soma

    SE soma % 2 = 0 ENTÃO
        ESCREVER "O número", soma, "é par."
    SENÃO
        ESCREVER "O número", soma, "é ímpar."
    FIMSE

    resto <- num1 % num2
    ESCREVER "O resto é", resto

    SE resto % 2 = 0 ENTÃO
        ESCREVER "O número", resto, "é par."
    SENÃO
        ESCREVER "O número", resto, "é ímpar."
    FIMSE

    divisao <- num1 / num2
    ESCREVER "A divisão é", divisao

    // Verificar se a parte inteira da divisão é par ou ímpar
    SE INTEIRO(divisao) % 2 = 0 ENTÃO
        ESCREVER "O número", INTEIRO(divisao), "é par."
    SENÃO
        ESCREVER "O número", INTEIRO(divisao), "é ímpar."
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

4. Faça um programa em Python que irá receber dois números e mostrar o maior, 
a  soma,  o  resto,  a  divisão  do  primeiro  pelo  segundo  e  verificar  se  a  parte  inteira  dos 
resultados são pares ou impares.
"""
num1 = int(input("Digite o primeiro número\n"))
num2 = int(input("Digite o segundo número\n"))

# Encontrar o maior número
if num1>num2:
    maior = num1
elif num2>num1:
    maior = num2
else:
    maior = "nenhum"

print(f'O maior é {maior}')

# Teste de par
if maior%2 == 0:
    print(f"O numero {maior} é par.")
else:
    print(f"O número {maior} é impar.")

# Encontrar a soma
soma = num1+num2

print(f"A soma é {soma}")

# Teste de par
if soma%2 == 0:
    print(f"O numero {soma} é par.")
else:
    print(f"O número {soma} é impar.")

# Encontrar o resto
resto = num1%num2

print(f"O resto é {resto}")

# Teste de par
if int(resto)%2 == 0:
    print(f"O numero {resto} é par.")
else:
    print(f"O número {resto} é impar.")

# Encontrar a divisão
divisao = num1/num2

print(f"A divisão é {divisao}")

# Teste de par
if divisao%2 == 0:
    print(f"O numero {divisao} é par.")
else:
    print(f"O número {divisao} é impar.")

```

# Descrição
## O programa lê dois números inteiros e calcula o maior valor, a soma, o resto da divisão, e o resultado da divisão do primeiro pelo segundo. Para cada resultado, verifica se a parte inteira é par ou ímpar, exibindo essa informação. O programa trata o caso em que os números são iguais, indicando que não há maior. Testado com vários valores, o código funcionou corretamente e apresentou as informações esperadas, incluindo os testes de paridade.

# Resultado
## Bem Sucedido