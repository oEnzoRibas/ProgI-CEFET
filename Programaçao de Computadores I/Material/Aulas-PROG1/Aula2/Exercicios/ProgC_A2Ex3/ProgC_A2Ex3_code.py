# Função para separar o número em centena, dezena e unidade
def separar_numero(numero):
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    return centena, dezena, unidade

# Função principal

numero = int(input("Digite um número inteiro de três dígitos: "))
centena, dezena, unidade = separar_numero(numero)
print("Centena =", centena)
print("Dezena =", dezena)
print("Unidade =", unidade)