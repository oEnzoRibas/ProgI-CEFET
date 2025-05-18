# 5. Verifique e apresente os resultados:
Seja três variáveis do tipo bool: a = False; b = True, e c = True. Qual é o retorno das proposições:
```
a) a && b                                                                                    

b) a && c                                

c) a || b                                     

d) !b 

e) a && (b || c)

f) (a && b) || c
```

# Resposta:
```python
# Declarações
a = False
b = True
c = True

# A) a && b
resultado_a = a and b
print("A) a && b =", resultado_a)
# B) a && c
resultado_b = a and c
print("B) a && c =", resultado_b)
# C) a || b
resultado_c = a or b
print("C) a || b =", resultado_c)
# D) !b
resultado_d = not b
print("D) !b =", resultado_d)
# E) a && (b || c)
resultado_e = a and (b or c)
print("E) a && (b || c) =", resultado_e)
# F) (a && b) || c
resultado_f = (a and b) or c
print("F) (a && b) || c =", resultado_f)

# Saídas
A) a && b = False
B) a && c = False
C) a || b = True
D) !b = False
E) a && (b || c) = False
F) (a && b) || c = True
```
