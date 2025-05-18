# 2. Entregue o pseudocódigo e o código em Python para a seguinte questão:
## Faça um programa que receba três notas, calcule a soma das notas e mostre na tela o resultado.

# ## Pseudocódigo
```
INÍCIO
    // Definição de variáveis
    DECLARE nota1, nota2, nota3, soma COMO REAL

    ESCREVER "Digite a primeira nota:"
    LER nota1
    ESCREVER "Digite a segunda nota:"
    LER nota2
    ESCREVER "Digite a terceira nota:"
    LER nota3

    soma <- nota1 + nota2 + nota3

    ESCREVER "A soma das notas é:", soma

FIM
```

## Código em Python
```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
soma = nota1 + nota2 + nota3
print("A soma das notas é:", soma)
```