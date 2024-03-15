"""
Programação Estruturada
2024.1
15/03/2024

Estruturas de Decisão
AC4
"""

def ler_nome():
    """Retorna uma string com o nome do aluno."""
    return input("Informe o nome do aluno: ")

def ler_notas():
   ap1 = float(input("Nota da Ap1:"))
   ap2 = float(input("Nota da Ap2:"))
   asub = float(input("Nota da Asub:"))
   ac = float(input("Nota da Ac:"))

   return ap1, ap2, asub, ac

def notas_sao_validas(ap1, ap2, asub, ac):

    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return True
    else:
        return False

    """
    Retorna True se todas as quatro notas estão entre 0 e 10, inclusive.
    Returna False caso contrário.
    """

def selecionar_notas(ap1, ap2, asub):

    if asub < ap2 and ap2 < ap1:

        return ap1, ap2

    elif asub > ap1 and ap1 < ap2:

        return asub, ap2

    else:
        if asub > ap1 and ap1 < ap2:

            return asub, ap2



    """
    Retorna as duas maiores notas, considerando que a AS pode substituir a
    AP1 ou a AP2, aquela que tiver a menor nota. Se a AS for menor que as duas,
    retorna apenas a AP1 e a AP2.
    """

def calcular_media(nota1, nota2, ac):
    """
    Retorna a média da disciplina, arredondada em duas casas decimais.
    M = (AP1 + AP2) * 0.4 + AC * 0.2
    """
    return (nota1 + nota2) * 0.4 + 0.2 * ac

def aluno_foi_aprovado(media):
    """
    Retorna True se o aluno foi aprovado, e False caso contrário.
    A média de aprovação é 7.0.
    """
    return media >= 7

def analisar_media(media):
    """
    Exibe a média na tela.
    Exibe se o aluno foi aprovado ou reprovado.
    """
    print(media)
    if aluno_foi_aprovado(media):
        print("Aluno foi aprovado.")
    else:
        print("Aluno foi reprovado.")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            nota1, nota2 = selecionar_notas(ap1, ap2, asub)
            media = calcular_media(nota1, nota2, ac)
            analisar_media(media)

main()