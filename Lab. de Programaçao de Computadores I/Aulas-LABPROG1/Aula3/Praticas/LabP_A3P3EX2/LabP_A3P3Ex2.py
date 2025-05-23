import math

numero = int(input("Digite um número: "))
if numero > 0:
    quadrado = numero ** 2
    cubo = numero ** 3
    raiz_quadrada = math.sqrt(numero)
    raiz_cubica = math.cbrt(numero)
    seno = math.sin(math.radians(numero))
    cosseno = math.cos(math.radians(numero))

    print(f"Quadrado: {quadrado} \n Cubo: {cubo} \n Raiz Quadrada: {raiz_quadrada} \n Raiz Cúbica: {raiz_cubica} \n Seno: {seno} \n Cosseno: {cosseno}")