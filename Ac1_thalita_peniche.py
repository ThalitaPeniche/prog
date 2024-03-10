# Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve ler os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
# Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.

#ax^2 + bx + c = a

a = float(input("Digite o valor do coeficiente de a:"))
b = float(input("Digite o valor do coeficiente de b:"))
c = float(input("Digite o valor do coeficiente de c:"))

# delta = b^2 - 4ac

delta = b**2 - 4*a*c

print("O valor de delta é:", delta)

# x = (-b +- raiz(delta))/2a

x1 = (-b - delta**0.5)/(2*a)
x2 = (-b + delta**0.5)/(2*a)

print( " O valor de x1 é: ", x1)
print( " O valor de x2 é: ", x2)



# Elabore um programa em Python que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.
# O programa deve utilizar apenas as funções print(), input() e int(), além dos operadores lógicos and, or ou not e de operadores aritméticos ou de comparação necessários.

ano = int(input("Que ano quer analisar? "))

bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

print(bissexto)

