"""
CEFET-MG - Laboratorio de Programação de Computadores 1
Prática 2 da Aula 2 - Estrutura Sequencial e Condicional
Grupo - Alunos: Sofia Guimarães, Enzo Ribas, Rafael Aquino, Alexandre Silva
Turma Mecânica T13 de Quinta-Feira de 10:40 às 12:20.
Código em Python para o exemplo 1.

2. Faça um programa que receba a altura e peso de uma pessoa, posteriormente, 
o  programa  deve  calcular  o  Índice  de  Massa  Corpórea  (IMC)  e  mostrar  o  peso  ideal, 
utilizando a seguintes fórmulas. 
IMC = peso/(altura*altura) 
OBS: Considere o IMC ideal como de 22.
"""
peso = float(input("Digite seu peso\n"))
altura = float(input("Digite sua altura\n"))
pesoideal = (altura*altura)*22
print(f"O seu peso ideal é {pesoideal}")