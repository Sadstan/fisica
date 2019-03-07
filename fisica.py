
import os

planeta = []
p = []
i = []

def main():
    global planeta
    global p
    global i

    planet = input("Deseja calcular o seu peso em qual planeta? ").strip().capitalize()
    massa = float(input("Digite a sua massa: "))
    gravidade = float(input("Digite a gravidade do planeta: "))

    planeta.append(planet)
    p.append(massa)
    i.append(gravidade)

    calculo()

def calculo():

    lambd = lambda value1,value2: value1[0] * value2[0]

    print("O seu peso no planeta {:.2f} será de aproximadamente {:.2f} newtons ".format(planeta[0],lambd(p,i)))

    continuar = input("Deseja continuar? (S/n) ").lower().strip()

    if continuar == "s":
        planeta.clear()
        p.clear()
        i.clear()

        os.system('clear' or 'cls')
        main()
    else:
        exit()

main()