# 2. Construa a descrição narrativa, pseudocódigo e teste de mesa para calculo do salário.
## Escreva um algoritmo para calcular o salário de uma arquiteta, sabendo que o salário da arquiteta é 3/4 do salário de um engenheiro.

# Descrição narrativa
```
Passo 1 - Receber o salário do engenheiro como entrada.
Passo 2 - Em seguida, o algoritmo deve calcular o salário da arquiteta, que é 3/4 do salário do engenheiro.
Passo 3 - Por fim, o algoritmo exibe o salário da arquiteta.
```

# Pseudocódigo
```
INICIO

    // Declaração de variáveis
    DECLARE
    salario_eng, salario_arq: NUMERICO

    // Entrada de dados
    ESCREVER "Digite o salário do engenheiro:"
    LER salario_eng

    // Processamento
    salario_arq <- (3/4) * salario_eng

    // Saída de dados
    ESCREVER "O salário da arquiteta é:", salario_arq
FIM
```

# Teste de mesa
| Passo | Ação realizada                         | salario_eng | salario_arq | Observação                         |
|-------|----------------------------------------|-------------|-------------|------------------------------------|
| 1     | Início do algoritmo                    | -           | -           | Declaração de variáveis            |
| 2     | Lê o valor do salário do engenheiro (4000) | 4000        | -           | Entrada do usuário                 |
| 3     | Calcula o salário da arquiteta        | 4000        | 3000        | 3/4 de 4000 é 3000                 |
| 4     | Escreve o valor do salário da arquiteta (3000) | 4000        | 3000        | Saída para o usuário               |
| 5     | Fim do algoritmo                       | -           | -           | Fim do algoritmo                   |
