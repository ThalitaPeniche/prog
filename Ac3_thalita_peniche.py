"""
Exercício 1: triângulos
Desenvolva uma função determina_tipo_triangulo que recebe três lados de um
triângulo e retorna uma string, "Escaleno", "Isósceles" ou "Equilátero",
conforme o tipo do triângulo. A função deve retornar "Não é um triângulo"
se os três lados não formarem um triângulo. Use a função abaixo como teste:
"""
def determina_tipo_triangulo(a,b,c):

    if a == b == c:
        return "Equilátero"

    elif a == b or b == c or a == c:
        return "isóceles"

    elif a != b != c:
        return "Escaleno"

    else:
        return "Não é um triângulo"

def testa_triangulo():

    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))

testa_triangulo()

"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que recebe um número inteiro e retorna uma
string indicando o dia da semana equivalente, considerando que o dia da semana
igual a 1 é o domingo, 2 é segunda-feira, etc. A função deve retornar uma
string vazia caso o número seja inválido. Use a função abaixo como teste:

"""
def dia_semana(dia):

    if dia == 1:
        return "domingo"

    elif dia == 2:
        return "segunda-feira"

    elif dia == 3:
        return "terça-feira"

    elif dia == 4:
        return "quarta-feira"

    elif dia == 5:
        return "quinta-feira"

    elif dia == 6:
        return "sexta-feira"

    elif dia == 7:
        return "sábado"

    else:
        return ""

def testa_dia_semana():
    print(dia_semana(2))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(9))

testa_dia_semana()

"""
Exercício 3: calculadora simples
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e
divisao, que recebem dois números cada uma e retornam o resultado da operação
indicada. Em seguida, crie uma função que elabora uma interface por linha de
comando (CLI), que lê dois números e uma operação e exibe na tela o valor do
resultado, ou exibe "operação inválida" se o usuário inserir uma mensagem
diferente das quatro operações.

"""

def operacao_aritmetica(a,b,operacao):

    if operacao == 'soma':
        return a + b

    elif operacao == 'subtracao':
        return a - b

    elif operacao == 'multiplicacao':
        return a * b

    elif operacao == 'divisao':
        if b != 0:
            return a / b
    else:
        return "Operação inválida"

def calculadora():

    a = float(input("Informe um número: "))
    b = float(input("Informe outro número: "))

    operacao_desejada = input("Informe a operação: ")

    resultado = operacao_aritmetica(a,b,operacao_desejada)
    print("Resultado: ",resultado)

calculadora()

