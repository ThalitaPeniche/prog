"""
Desenvolda duas funções em Python:

eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de
uma equação de segundo grau no formato ax² + bx + c = 0, supondo as raízes
sempre reais;

bissexto(ano), que recebe um valor inteiro e retorna um valor booleano,
informando se o ano é bissexto ou não.

"""

def eq_seg_grau(a,b,c):
   delta = (b**2) - (4*a*c)
   x1 = (-b - delta**0.5)/(2*a)
   x2 = (-b + delta**0.5)/(2*a)

   return x1,x2

eq_seg_grau(2,4,-6)



def bissexto(ano):
   if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
      return True

   else:
      return False

bissexto(1996)

"""
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe
dois parâmetros posicionais reais, valor_hora e num_horas, que correspondem ao
valor do salário por hora e o número de horas trabalhadas no mês, respectivamente.
Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda
a ser deduzido, cujo valor padrão é 0.275. . A função retorna o salário líquido
de um funcionário, calculado como o produto do valor por hora pelo número de horas,
reduzido o percentual do imposto de renda dado.

"""

def calcula_salario(valor_hora, num_hora):
    salario = (valor_hora * num_hora)-((valor_hora * num_hora)*0.275)
    return salario

calcula_salario(50,40)
