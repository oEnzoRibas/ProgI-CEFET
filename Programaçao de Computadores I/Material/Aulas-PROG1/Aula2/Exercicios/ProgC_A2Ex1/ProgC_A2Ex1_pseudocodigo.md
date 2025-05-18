# 1. Elabore o pseudocódigo e o código:
## Elabore um programa que receba os catetos de um triangulo e calcule a sua hipotenusa.

# ## Pseudocódigo
```
INÍCIO
    // Definição de variáveis
    DECLARE cateto1, cateto2, hipotenusa COMO REAL

    ESCREVER "Digite o valor do cateto 1:"
    LER cateto1
    ESCREVER "Digite o valor do cateto 2:"
    LER cateto2

    hipotenusa <- RAIZ(cateto1^2 + cateto2^2)

    ESCREVER "A hipotenusa do triângulo é:", hipotenusa

FIM
```

## Código em Python
```python
import math

cateto1 = float(input("Digite o valor do cateto 1: "))
cateto2 = float(input("Digite o valor do cateto 2: "))
hipotenusa = math.hypot(cateto1, cateto2)
print("A hipotenusa do triângulo é:", hipotenusa)
```

