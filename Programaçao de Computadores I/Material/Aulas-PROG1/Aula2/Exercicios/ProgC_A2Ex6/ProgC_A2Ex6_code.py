# 6. Elabore o pseudocódigo e o código em Python para o problema descrito a seguir.
# Faça um programa que receba a base e a altura de um retângulo e mostre o seu perímetro.
#  Caso os valores dos catetos forem maiores que zero.

import math

# Função para calcular o perímetro do triângulo retângulo
def calcular_perimetro_triangulo(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return cateto1 + cateto2 + hipotenusa

# Solicitar os catetos do triângulo
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

if cateto1 > 0 and cateto2 > 0:
    perimetro = calcular_perimetro_triangulo(cateto1, cateto2)
    print("O perímetro do triângulo retângulo é:", perimetro)
else:
    print("Valores inválidos. Os catetos devem ser maiores que zero.")
