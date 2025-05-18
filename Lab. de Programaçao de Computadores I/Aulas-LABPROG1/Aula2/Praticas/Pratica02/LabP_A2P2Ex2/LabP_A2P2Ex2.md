```markdown
INÍCIO
    // Definição de variáveis
    
    DECLARE peso, altura, imc, pesoIdeal COMO REAL

    ESCREVER "Digite seu peso (em kg):"
    LER peso
    ESCREVER "Digite sua altura (em metros):"
    LER altura

    SE altura > 0 ENTÃO
        imc <- peso / (altura * altura)
        pesoIdeal <- 22 * (altura * altura)
        ESCREVER "O seu peso ideal é:", pesoIdeal
    SENÃO
        ESCREVER "Altura inválida. Deve ser maior que zero."
    FIMSE
FIM
```

# ## Código em Python
```python
"""
CEFET-MG - Laboratorio de Programação de Computadores 1
Prática 2 da Aula 2 - Estrutura Sequencial e Condicional
Grupo - Alunos: Sofia Guimarães, Enzo Ribas, Rafael Aquino, Alexandre Silva
Turma Mecânica T13 de Quinta-Feira de 10:40 às 12:20.
Código em Python para o exemplo 1.

2. Faça um programa que receba a altura e peso de uma pessoa, posteriormente, 
o  programa  deve  calcular  o  Índice  de  Massa  Corpórea  (IMC)  e  mostrar  o  peso  ideal, 
utilizando a seguintes fórmulas. 
IMC = peso/(altura*altura) 
OBS: Considere o IMC ideal como de 22.
"""
peso = float(input("Digite seu peso\n"))
altura = float(input("Digite sua altura\n"))
pesoideal = (altura*altura)*22
print(f"O seu peso ideal é {pesoideal}")
```

# Descrição
O algoritmo solicita que o usuário insira seu peso e altura. Em seguida, verifica se a altura é maior que zero para evitar divisões inválidas. Se for, calcula o IMC e o peso ideal com base em um IMC de 22, exibindo o valor correspondente. Se a altura for inválida, uma mensagem de erro é mostrada. O código foi testado com diferentes valores e apresentou resultados corretos. A lógica sequencial e condicional foi aplicada com sucesso.

# Resultado
Bem Sucedido 