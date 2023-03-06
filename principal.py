import os

def menu():
    opcion_menu = {"P": "Perfumería",
                   "F": "Farmacia",
                   "C": "Cosméticos",
                   "S": "Salir"}
    return opcion_menu

def inicio():
    """ Turnero """
    opcion = "z"
    while opcion != "s":
        os.system("cls")
        opc_menu = menu()
        for opc, area in opc_menu.items():
            print(f"[{opc}] - {area}")
        opcion = input("Seleccione una opción: ").lower()
        if opcion == 'p':
            os.system("cls")
            print("Perfumería")
            input()
        elif opcion == 'f':
            os.system("cls")
            print("Farmacia")
            input()
        elif opcion == 'c':
            os.system("cls")
            print("Cosméticos")
            input()
        elif opcion != 's':
            os.system("cls")
            print("Opción incorrecta")
            input()



inicio()
