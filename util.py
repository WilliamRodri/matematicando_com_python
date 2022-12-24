import time
import os
import math

def start():
    while True:
        print("*****************************")
        print("*****************************")
        print("********MATEMATICANDO********")
        print("*****************************")
        print("*****************************")
        print(" ")
        q = input("DE UM ENTER PRA INICIAR...")
        if q == "":
            time.sleep(1)
            options()
            break
        else:
            continue
        
def options():
    os.system('cls')
    print("*****************************")
    print("ESCOLHA UMAS DAS OPÇÕES ABAIXO")
    print("[1]CALCULADORA\n[2]TABUADA\n[3]PERMUTAÇÃO\n[4]MÉDIA DE VALORES\n[5]RAIZES\n[6]IMC\n[7]LOGARITMO")
    a = int(input(": "))
    
    if a == 1:
        calculadora()
    elif a == 2:
        tabuada()
    elif a == 3:
        permutacao()
    elif a == 4:
        media()
    elif a == 5:
        raiz()
    elif a == 6:
        imc()
    elif a == 7:
        log()
    else:
        print("ESCOLHA UMA OPÇÃO")
#calculadora
def calculadora():
    os.system('cls')
    value1 = 0
    operacao = ''
    value2 = 0


    while True:
        value1 = int(input("Digite o Primeiro Valor: "))
        operacao = input("Digite a Opração Desejada\n[+]\n[-]\n[*]\n[/]\n: ")
        value2 = int(input("Digite o Segundo Valor: "))
        time.sleep(3)

        try :
            if operacao == '+':
                calculo = value1+value2
                print(f"{value1} {operacao} {value2} = {calculo}")
                time.sleep(1)
                respot = input("Deseja Fazer outro calculo?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif operacao == '-':
                calculo = value1-value2
                print(f"{value1} {operacao} {value2} = {calculo}")
                time.sleep(1)
                respot = input("Deseja Fazer outro calculo?\n:[s/n] ").lower().strip()
                print(respot)
            if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
            elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif operacao == '*':
                calculo = value1*value2
                print(f"{value1} {operacao} {value2} = {calculo}")
                time.sleep(1)
                respot = input("Deseja Fazer outro calculo?\n:[s/n] ").lower().strip()
                print(respot)
            if respot == 's':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                continue
            elif respot == 'n':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                break
            elif operacao == '/':
                calculo = value1/value2
                print(f"{value1} {operacao} {value2} = {calculo}")
        except ValueError:
            print("Digite um valor porfavor")
            time.sleep(1)
            
#tabuada
def tabuada():
    os.system('cls')
    while True:
        tabuada = int(input("Digite o valor: "))
        n = int(input("quantidade: "))
        operacao = input("Digite a operacao da tabuda desejada!\n[+]\n[-]\n[*]\n[/]\n: ")
        time.sleep(3)
        try :
            if operacao == '+':
                for count in range(n):
                    print(f'{tabuada} + {count} = {tabuada+count}')
                time.sleep(1)
                respot = input("Deseja fazer outra tabuada?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif operacao == '-':
                for count in range(n):
                    print(f'{tabuada} - {count} = {tabuada-count}')
                time.sleep(1)
                respot = input("Deseja fazer outra tabuda?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarda...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarda...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif operacao == '*':
                for count in range(n):
                    print(f'{tabuada} * {count} = {tabuada*count}')
                time.sleep(1)
                respot = input("Deseja fazer outra tabuda?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarda...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarda...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif operacao == '/':
                #a ser configurado
                time.sleep(1)
                respot = input("Deseja fazer outra tabuda?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarda...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarda...")
                    time.sleep(2)
                    os.system('cls')
                    break
        except ValueError:
            print("Digite um valor porfavor")
            time.sleep(1)
            
#PERMUTAÇÃO
def permutacao():
    os.system('cls')
    while True:
        nn = int(input("Digite o valor: "))
        try:
            n = nn*(nn-1)*(nn-2)
            print(f"A permutação de {nn} é {n}")
            time.sleep(1)
            respot = input("Deseja saber a permutação de outro número?\n:[s/n] ").lower().strip()
            print(respot)
            if respot == 's':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                continue
            elif respot == 'n':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                break
        except ValueError:
            print("Digite um valor Inteiro")
            break

#MEDIA DE 3 VALORES
def media():
    os.system('cls')
    while True:
        value1 = float(input("Informe o valor 1: "))
        value2 = float(input("Informe o valor 2: "))
        value3 = float(input("Informe o valor 3: "))
        
        try:
            calculo = value1+value2+value3
            final = calculo/3
            print(f"A média final é de {final:.2f}")
            time.sleep(1)
            respot = input("Deseja saber a média de outros valores?\n:[s/n] ").lower().strip()
            print(respot)
            if respot == 's':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                continue
            elif respot == 'n':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                break
        except ValueError:
            print("Digite um valor Inteiro")
            break

#RAIZ QUADRADA
def raiz():
    os.system('cls')
    #options
    while True:
        try:
            print("Escolha uma opção")
            print("[1] Calcular a raiz quadrada de um numero\n[2]Cálculo da raiz cúbica ou com outro índice\n[3] Calculo inverso (calcular, com o valor da raiz (z) e do indice (y), o número para o qual ele calculou a raiz (x, radicando))")
            i = int(input(": "))
            print(i)
            
            if i == 1:
                raiz = int(input("Digite o numero (x): ").replace(",", "."))
                print(raiz)
                resultado = 0
                resultado = math.sqrt(raiz)
                calculo = math.ceil(resultado*100)/100
                print(f"A raiz quadrada de {raiz} é {calculo}")
                time.sleep(1)
                respot = input("Deseja saber a média de outros valores?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif i == 2:
                
                print("Digite o índice da raiz (y): ")
                indice = int(input(": ").replace(",", "."))
                print("Inserir o numero (x): ")
                raizIn = int(input(": ").replace(",", "."))
                
                resultado = 0
                resultado = math.pow(raizIn,1/indice)
                calculo = math.ceil(resultado*100)/100
                print(f"O resultado do calculo da raiz {raiz} é {calculo}")

                time.sleep(1)
                respot = input("Deseja saber a média de outros valores?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif i == 3:
                
                print("Índice da raiz (y): ")
                indice = int(input(": ").replace(",", "."))
                print("Valor da raiz (z): ")
                resultado = int(input(": ").replace(",", "."))
                
                raiz = 0
                raiz = math.pow(resultado,indice)
                calculo = math.ceil(raiz*100)/100
                print(f"Radicando (x): {calculo}")
                
                time.sleep(1)
                respot = input("Deseja saber a média de outros valores?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            else:
                print("Digite um valor")
        except ValueError:
            print("Digite um valor")
    
#IMC [ALTURA E PESO]
def imc():
    os.system('cls')
    while True:
        try:
            altura = float(input("Informe sua Altura: ").replace(",", "."))
            peso = float(input("Informe seu peso: ").replace(",", "."))
            
            imc = peso/(altura*altura)
            print(f"SEU IMC É {imc:.2f}")
            
            if imc < 18.5:
                print("CLASSIFICAÇÃO    |   OBESIDADE(GRAU)")
                print("MAGREZA          |           0      ")
                
                time.sleep(1)
                respot = input("Deseja saber outro IMC?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif imc >= 18.5 and imc <= 24.9:
                print("CLASSIFICAÇÃO    |   OBESIDADE(GRAU)")
                print("NORMAL           |           0      ")
                
                time.sleep(1)
                respot = input("Deseja saber outro IMC?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif imc >= 25 and imc <= 29.9:
                print("CLASSIFICAÇÃO    |   OBESIDADE(GRAU)")
                print("SOBREPESO        |           0      ")
                
                time.sleep(1)
                respot = input("Deseja saber outro IMC?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif imc >= 30 and imc <= 34.9:
                print("CLASSIFICAÇÃO    |   OBESIDADE(GRAU)")
                print("OBESIDADE        |           I      ")  
                
                time.sleep(1)
                respot = input("Deseja saber outro IMC?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break 
            elif imc >= 35 and imc <= 39.9:
                print("CLASSIFICAÇÃO    |   OBESIDADE(GRAU)")
                print("OBESIDADE        |           II     ") 
                
                time.sleep(1)
                respot = input("Deseja saber outro IMC?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            elif imc >= 40:
                print("CLASSIFICAÇÃO    |   OBESIDADE(GRAU)")
                print("OBESIDADE        |           III    ")
                
                time.sleep(1)
                respot = input("Deseja saber outro IMC?\n:[s/n] ").lower().strip()
                print(respot)
                if respot == 's':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    continue
                elif respot == 'n':
                    print("Aguarde...")
                    time.sleep(2)
                    os.system('cls')
                    break
            else:
                print("ERROR")
        except ValueError:
            print("Digite um valor")
            
#LOGARITMO
def log():
    os.system('cls')
    while True:
        value = float(input("Informe o número que deseja saber o logaritmo: "))
        
        try:
            log = math.log(value)
            print(f"O logaritmo de {value} é {log:.2f}")
            
            time.sleep(1)
            respot = input("Deseja saber o logaritmo de outros valores?\n:[s/n] ").lower().strip()
            print(respot)
            if respot == 's':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                continue
            elif respot == 'n':
                print("Aguarde...")
                time.sleep(2)
                os.system('cls')
                break
        except ValueError:
            print("Digite um valor Inteiro")
            break