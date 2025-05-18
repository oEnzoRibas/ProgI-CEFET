# 1. Construa a descrição narrativa, pseudocódigo e teste de mesa.

## Faça um algoritmo para somar dois (2) números quaisquer e multiplicar o resultado pelo primeiro número.

# Descrição narrativa
Passo 1 - Receber dois números quaisquer como entrada. 
Passo 2 - Em seguida, ele deve somar esses dois números e multiplicar o resultado da soma pelo primeiro número fornecido.
Passo 3 - Por fim, o algoritmo exibe o resultado dessa operação.

# Pseudocódigo
```
INICIO
    
    // Declaração de variáveis
    DECLARE
    num1, num2, soma, resultado: NUMERICO

    // Entrada de dados
    ESCREVER "Digite o primeiro número:"
    LER num1
    ESCREVER "Digite o segundo número:"
    LER num2
    
    // Processamento
    // Soma os dois números
    soma <- num1 + num2
    resultado <- soma * num1

    // Saída de dados
    ESCREVER resultado
FIM
```

# Teste de mesa

| Passo | Ação realizada                         | num1 | num2 | soma | resultado | Observação                         |
|-------|----------------------------------------|------|------|------|-----------|------------------------------------|
| 1     | Início do algoritmo                    | -    | -    | -    | -         | Declaração de variáveis            |
| 2     | Lê o valor do primeiro número (4)      | 4    | -    | -    | -         | Entrada do usuário                 |
| 3     | Lê o valor do segundo número (6)       | 4    | 6    | -    | -         | Entrada do usuário                 |
| 4     | soma ← num1 + num2                     | 4    | 6    | 10   | -         | Soma de 4 + 6                      |
| 5     | resultado ← soma * num1                | 4    | 6    | 10   | 40        | Multiplicação: 10 * 4             |
| 6     | Escreve o valor de resultado (40)      | 4    | 6    | 10   | 40        | Saída para o usuário               |
| 7     | Fim do algoritmo                       | -    | -    | -    | -         | Fim do algoritmo                   |