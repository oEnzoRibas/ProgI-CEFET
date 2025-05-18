# 4. Sejam as seguintes declarações e atribuições:
```
Declarações:

a=12; b=4; c=5; x=6.0; y=3.0

Qual o valor das seguintes expressões em Python? 

Observação: A função abs retorna o “valor absoluto” (“módulo”), ou seja abs(-2) = 2 e abs(2) = 2.

A) a/b+a%b

B) x/y+b%c

C) a/x*c/y

D) abs(c – a) – abs(b – c) * abs(b – c)
```

# Resposta:
```python
# Declarações
a = 12
b = 4   
c = 5
x = 6.0
y = 3.0     

# A) a/b+a%b
resultado_a = a / b + a % b
print("A) a/b + a%b =", resultado_a)
# B) x/y+b%c
resultado_b = x / y + b % c
print("B) x/y + b%c =", resultado_b)
# C) a/x*c/y
resultado_c = a / x * c / y
print("C) a/x * c/y =", resultado_c)
# D) abs(c – a) – abs(b – c) * abs(b – c)
resultado_d = abs(c - a) - abs(b - c) * abs(b - c)
print("D) abs(c - a) - abs(b - c) * abs(b - c) =", resultado_d)

# Saídas
A) a/b + a%b = 3.0
B) x/y + b%c = 6.0
C) a/x * c/y = 3.3333333333333335
D) abs(c - a) - abs(b - c) * abs(b - c) = 6
```
