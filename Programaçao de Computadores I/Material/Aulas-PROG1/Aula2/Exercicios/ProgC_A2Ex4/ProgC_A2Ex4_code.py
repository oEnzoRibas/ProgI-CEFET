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