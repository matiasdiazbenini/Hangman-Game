import random
import time
import os

def run():

# LLAMADAS AL SISTEMA. SHORTCUTS DE FUNCTIONS

    cls = lambda: os.system("cls")
    sleep1 = lambda: time.sleep(1)
    sleep2 = lambda: time.sleep(2)
    sleep3 = lambda: time.sleep(3)
    sleep4 = lambda: time.sleep(4)
    sleep5 = lambda: time.sleep(5)
    
    final = ""
    lista = []
    acierto = 0

    with open("./archivos/data.txt", "r", encoding="utf=8") as f:
        for i in f:
            lista.append(i.rstrip("\n"))
    
    palabra_escondida = random.choice(lista)
    adivina = ["_" for i in palabra_escondida]
    # print(palabra_escondida)

    vidas = (input("Con cuantas vidas te gustaria jugar?: "))
    x = int(vidas)
    if(len(vidas)!=1) or vidas.isalpha==True:
        print("Error. Ingrese un numero")
    sleep1()
    cls()

    print("Bienvenido al juego del ahorcado\n")
    sleep1
    print("Tenes que adivinar una palabra de: " + "_ "*len(palabra_escondida) + " letras") 
    sleep3
    cls()

    while True:
        letra = input("Ingresa una letra: ").lower()

        if(len(letra)!=1) or letra.isnumeric() or letra.isalpha==False:
            print("Mal ingresada la letra. Solo se puede una letra.")

        for count, i in enumerate(palabra_escondida):
            if letra == i:
                adivina[count]=letra
                acierto += 1
        print("\n Acertaste " + str(acierto) + " veces la letra: " + letra + "\n")
        acierto = 0

        if letra not in palabra_escondida:
            x -= 1
            print("\n Error. Te quedan: " + str(x) + " vidas.")

        for i in adivina:
            print(i, end=" ")
            final +=i
        sleep2()
        cls()

        if final == palabra_escondida:
            print(" \n \n Ganaste. \n La palabra era: " + palabra_escondida)
            break

        if x == 0:
            print(" \n \n Perdiste. Te quedaste sin vidas. \n \n La palabra era: " + palabra_escondida)
            break

        final=""

if __name__ == "__main__":
    run()




    # usar archivo data.txt
    # usar funcion enumerate
    # usar metodo get
    # usar sentencia os.system("cls")
    # buscar y copiar el codigo de adivina_el_numero.py