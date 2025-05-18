
import math

cateto1 = float(input("Digite o valor do cateto 1: "))
cateto2 = float(input("Digite o valor do cateto 2: "))
hipotenusa = math.hypot(cateto1, cateto2)
print("A hipotenusa do triângulo é:", hipotenusa)
