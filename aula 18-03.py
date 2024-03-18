def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1   # num = num - 1

    print("acabou")

contagem_regressiva(5)




# range([start], stop, [step])
# start - inclusive
# stop - exclusive
# step - passo


print(list(range(5)))
print(list(range(2, 5)))
print(list(range(2, 10, 3)))
print(list(range(10, -5, 2)))




def contagem_regressiva2(num):
    for cont in range(num, -1, -1):
        print(cont)

contagem_regressiva(5)



def ola_varias_vezes(n):
    for _ in range(n):
        print("olá")

ola_varias_vezes(3)




def pula_mult_3(maximo):
    for x in range(1, maximo + 1):
        print(x)

pula_mult_3(10)




def pula_mult_3(maximo):
    for x in range(1, maximo + 1):
        if x % 3 == 0:
            continue

        print(x)

pula_mult_3(10)




def para_antes_de_10(maximo):
    for x in range(1, maximo + 1):
        if x >=10:
            break
        print(x)

    print("acabou")

print("-" * 30)
para_antes_de_10(20)




def conta_pares(min,max):
    for x in range(min, max + 1):
        if x % 2 != 0:
            continue

        print(x, end = "-")

conta_pares(2, 20)




def conta_pares(min,max):
    for x in range(min, max + 1, 2):

        print(x, "-")

conta_pares(2, 20)


def fatorial(num):

fat = 1

for mult in range(1, num +1)