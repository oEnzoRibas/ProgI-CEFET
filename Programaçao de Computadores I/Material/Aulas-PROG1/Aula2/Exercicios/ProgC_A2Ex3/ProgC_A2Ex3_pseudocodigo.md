# 3. Faça um algoritmo, teste de mesa e código em Python para:
## Um programa que receba um número inteiro de três dígitos e o imprima no formato Centena = x, Dezena = y e Unidade = z. Exemplo: número = 123, centena = 1, dezena = 2 e unidade = 3.

## Pseudocódigo
```
INÍCIO
    // Definição de variáveis
    DECLARE numero, centena, dezena, unidade COMO INTEIRO

    ESCREVER "Digite um número inteiro de três dígitos:"
    LER numero

    centena <- numero DIV 100
    dezena <- (numero MOD 100) DIV 10
    unidade <- numero MOD 10

    ESCREVER "Centena =", centena
    ESCREVER "Dezena =", dezena
    ESCREVER "Unidade =", unidade

FIM
```

## Código em Python
```python
# Função para separar o número em centena, dezena e unidade
def separar_numero(numero):
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    return centena, dezena, unidade

numero = int(input("Digite um número inteiro de três dígitos: "))
centena, dezena, unidade = separar_numero(numero)
print("Centena =", centena)
print("Dezena =", dezena)
print("Unidade =", unidade)
```