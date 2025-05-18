```
INÍCIO
    // Definição de variáveis
    DECLARE nota1, nota2, nota3, notaatv, conceito COMO REAL
    DECLARE notaFinal COMO REAL
    DECLARE conceitoFinal COMO CARACTERE

    ESCREVER "Digite a nota 1:"
    LER nota1
    ESCREVER "Digite a nota 2:"
    LER nota2
    ESCREVER "Digite a nota 3:"
    LER nota3
    ESCREVER "Digite a nota da atividade:"
    LER notaatv

    notaFinal <- nota1 + nota2 + nota3 + notaatv

    SE notaFinal >= 90 ENTÃO
        conceitoFinal <- "A"
    SENÃO SE notaFinal >= 80 E notaFinal <= 89 ENTÃO
        conceitoFinal <- "B"
    SENÃO SE notaFinal >= 70 E notaFinal <= 79 ENTÃO
        conceitoFinal <- "C"
    SENÃO SE notaFinal >= 60 E notaFinal <= 69 ENTÃO
        conceitoFinal <- "D"
    SENÃO
        conceitoFinal <- "F"
    FIMSE

    ESCREVER "A nota do aluno é", conceitoFinal
FIM
```

# Código em Python
```python
"""
CEFET-MG - Laboratorio de Programação de Computadores 1
Prática 2 da Aula 2 - Estrutura Sequencial e Condicional
Grupo - Alunos: Sofia Guimarães, Enzo Ribas, Rafael Aquino, Alexandre Silva
Turma Mecânica T13 de Quinta-Feira de 10:40 às 12:20.
Código em Python para o exemplo 1.

3.  Desenvolva  um  algoritmo  para  verificar  qual  vai  ser  o  conceito  acadêmico  de 
um aluno no final do semestre. O algoritmo deve receber 3 notas de provas e 1 nota de 
exercício,  calcular  a  nota  final  e  informar  o  valor  dessa  nota  e  conceito  obtidos. A  nota 
final é a soma das notas das provas e exercício. 
Para ficar com A, o aluno deve ficar com uma nota entre 100 a 90. 
Para o conceito B, o aluno deve ficar com uma nota entre 89 a 80.  
Já  para  o  conceito  C,  o  aluno  deve  ficar  com  uma  nota  final  entre  79  a  70.
Para  o conceito D, o aluno deve ficar com uma nota entre 69 e 60.
Por fim, para o conceito F, o aluno deve ficar com uma nota igual ou inferior a 59.
"""

nota1 = float(input("Digite a nota 1\n"))
nota2 = float(input("Digite a nota 2\n"))
nota3 = float(input("Digite a nota 3\n"))
notaatv = float(input("Digite a nota da atividade\n"))

nota = ""

conceito = nota1+nota2+nota3+notaatv
if conceito >= 90:
    nota="A"
elif conceito >= 80 and conceito <= 89:
    nota="B"
elif conceito >= 70 and conceito <= 79:
    nota="C"
elif conceito >= 60 and conceito <= 69:
    nota="D"
elif conceito <= 59:
    nota="F"

print(f"A nota do aluno é {nota}")
```


# Descrição
## O programa solicita ao usuário quatro notas: três de provas e uma de atividade. Ele soma essas notas para obter a nota final. A partir dessa nota, o algoritmo determina um conceito acadêmico de acordo com a tabela fornecida (de A a F). Cada faixa de nota é verificada com estruturas condicionais. O valor do conceito é impresso ao final. O código foi executado e validado com diversos valores, funcionando corretamente.

# Resultado
## Bem Sucedido