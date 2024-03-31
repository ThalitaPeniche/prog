import random

def main():

    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10,20)
    defesa_aventureiro = random.randint(1,5)
    vida_monstro = random.randint(60,80)
    ataque_monstro = random.randint(20,30)

    print("Aventureiro: vida", vida_aventureiro, "Ataque:", ataque_aventureiro, "Defesa:", defesa_aventureiro)
    print("Monstro: vida ", vida_monstro, "Ataque:", ataque_monstro)

    rodada = 1

    while True:
        print("Rodada: ", rodada)

        dano_monstro = random.randint(1, ataque_aventureiro)
        vida_monstro = vida_monstro - dano_monstro


        if vida_monstro > 0:
            print("Aventureiro ataca o monstro causando: ", dano_monstro, "de dano.")

        if vida_monstro <= 0:
            print("O monstro morreu!")
            break

        dano_aventureiro = random.randint(1,ataque_monstro)  # Corrigido para usar random.randint()
        vida_aventureiro = vida_aventureiro - dano_aventureiro

        if vida_aventureiro > 0:
            print("Monstro ataca o aventureiro causando: ",dano_aventureiro,"de dano.")

        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break

        print("Aventureiro: vida", vida_aventureiro, "Ataque:", ataque_aventureiro, "Defesa:", defesa_aventureiro)
        print("Monstro: vida ", vida_monstro, "Ataque:", ataque_monstro)

        rodada += 1

main()