"""
CEFET-MG - Laboratorio de Programação de Computadores 1
Prática 2 da Aula 2 - Estrutura Sequencial e Condicional
Grupo - Alunos: Sofia Guimarães, Enzo Ribas, Rafael Aquino, Alexandre Silva
Turma Mecânica T13 de Quinta-Feira de 10:40 às 12:20.
Código em Python para o exemplo 1.

1. Faça um algoritmo que receba o salário de um funcionário, 
calcule e mostre o novo  salário  sabendo-se  que  este  
sofreu  um  aumento  de  25%  neste  mês.  Mostre  o
resultado na tela.
"""
salario = float(input("salario atual:\n"))
novo_salario = salario * 1.25
print(f"O novo salario com aumento é {novo_salario}")