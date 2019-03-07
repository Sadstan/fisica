
import os

planeta = [] #Nesse trecho de código defini as listas que vão armazenar as informações uteis que iremos utilizar
p = [] #Irá armazenar a massa (peso como dizemos)
i = [] #E nessa lista aqui, iremos armazenar a gravidade do planeta digitado

def main(): #Defini uma função principal para caso o usuário desejar reiniciar o programa, basta chamar novamente a função
    global planeta # Chamei as listas que estão contidas no escopo principal do programa (a lista que no caso foi nomeada como "planeta")
    global p #A lista nomeada com o nome p de "peso" que no caso é a massa digitada pelo usuário que será armazenada
    global i # E chamamos novamente a lista "i" que irá conter a gravidade

    planet = input("Deseja calcular o seu peso em qual planeta? ").strip().capitalize() # Perguntamos o nome do planeta que o usuário deseja calcular
    massa = float(input("Digite a sua massa: ")) # Perguntamos a massa (peso) do usuário
    gravidade = float(input("Digite a gravidade do planeta: ")) # E por fim... a gravidade!

    planeta.append(planet) # Chamamos a lista planeta e adicionamos dentro dela as informações digitadas pelo usuário dentro da lista com a função .append()
    p.append(massa) # Chamamos a lista "p" que irá conter a massa e com a função .append() adicionamos dentro da função as informações
    i.append(gravidade) # E por fim mandamos para a lista "i" a gravidade!

    calculo() # Pronto, tudo feito!! Agora precisamos calcular essas informações, para isso criei outra função chamada "calculo" que irá calcular as informações

def calculo():

    lambd = lambda value1,value2: value1[0] * value2[0]
    '''
    Com a função anônima 'lambda' irá conter dois valores (value1 e value2). Com dois pontos (:) adicionamos o valor1 e
    multiplicamos pelo valor2. "Mas, esses valores estão vázios..." Exatamente! Tanto o valor1 e valor2 nós vamos adicionar
    as informações que o usuário digitou e foi salva em nossas listas! Você irá entender.
    '''

    print("O seu peso no planeta {:.2f} será de aproximadamente {:.2f} newtons ".format(planeta[0],lambd(p,i)))
    
    # A linha de código acima é importante para entendermos como a função lambda irá somar nossos valores
    # Olhe apenas para essa parte do código: .format(planeta[0],lambd(p,i)
    # Lembre-se que quando o usuário digitou as informações como o peso (massa) e a gravidade (i) nós demos um append e mandamos para essas listas
    # Então como as informações já estão salvas, chamamos a váriavel "lambd" que está armazenando a soma dos valores e então passamos o que nossa função irá somar
    # Os valores que estão vázios na função lambda (value1 e value2) será preenchido pelas informações contidas na lista "p" e "i"
    # Para isso chamamos a variavel lambd e dentro dela entre parenteses () passamos a lista "p" e "i"
    # Então esses valores serão adicionados na value1 e value2 e então serão somados.
    
    #  lambd = lambda value1,value2: value1[0] * value2[0]
    
    continuar = input("Deseja continuar? (S/n) ").lower().strip() # Caso o usuário desejar continuar, o script será reiniciado

    if continuar == "s":
        planeta.clear()
        p.clear()
        i.clear()

        os.system('clear' or 'cls')
        main()
    else:
        exit()

main()
