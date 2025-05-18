# 3. Desenvolva um algoritmo para a média ponderada.
## Receber três notas, números inteiros (int), e seus respectivos pesos, números de ponto flutuante (float), calcular e mostrar a média ponderada dessas notas, numero de ponto flutuante (float). Mostre o resultado na tela como uma mensagem de texto (string). A formula da média ponderada que deve ser utilizada é: Media = (nota1 * peso1 + nota2 * peso2...)/(peso1 +peso2…).
### Descrição narrativa

O algoritmo solicita ao usuário três notas (valores inteiros) e seus respectivos pesos (valores de ponto flutuante). Em seguida, calcula a média ponderada utilizando a fórmula fornecida e exibe o resultado como uma mensagem de texto.

### Fluxograma

```mermaid
flowchart TD
    A[Início] --> B[Receber nota1, nota2, nota3 (int)]
    B --> C[Receber peso1, peso2, peso3 (float)]
    C --> D[Calcular média ponderada: (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)]
    D --> E[Exibir resultado]
    E --> F[Fim]
```

### Pseudocódigo

```
Início
    Leia nota1, nota2, nota3 (inteiros)
    Leia peso1, peso2, peso3 (floats)
    media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)
    Escreva "A média ponderada é: ", media
Fim
```

### Teste de mesa

| nota1 | peso1 | nota2 | peso2 | nota3 | peso3 | Cálculo                                      | Resultado |
|-------|-------|-------|-------|-------|-------|-----------------------------------------------|-----------|
| 7     | 2.0   | 8     | 3.0   | 6     | 1.0   | (7*2.0 + 8*3.0 + 6*1.0) / (2.0+3.0+1.0) = 44/6 | 7.33      |

### Implementação em Python

```python
# Recebe as notas (inteiros)
nota1 = int(input("Digite a primeira nota (int): "))
nota2 = int(input("Digite a segunda nota (int): "))
nota3 = int(input("Digite a terceira nota (int): "))

# Recebe os pesos (floats)
peso1 = float(input("Digite o peso da primeira nota (float): "))
peso2 = float(input("Digite o peso da segunda nota (float): "))
peso3 = float(input("Digite o peso da terceira nota (float): "))

# Calcula a média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Mostra o resultado
print(f"A média ponderada é: {media:.2f}")
```
