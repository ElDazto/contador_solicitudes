import os

def menu():
    while True:
        os.system('cls')
        eleccion = int(input("""Verificador:
1.- Pablo
2.- Kevin
3.- Valentina
4.- Cancelar\n"""))
        if eleccion == 1:
            x1, y1, x2, y2 = 520, 0, 630, 20
            break
        elif eleccion == 2:
            x1, y1, x2, y2 = 520, 0, 630, 20
            break
        elif eleccion == 3:
            x1, y1, x2, y2 = 520, 0, 630, 20
            break
        elif eleccion == 4:
            exit()
    return x1, y1, x2, y2