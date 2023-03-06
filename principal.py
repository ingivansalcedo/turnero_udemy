from os import system
import os
from sysconfig import sys


def plataforma_sistema_operativo():
    if sys.platform.startswith('win32'):
        return 'Windows'
    elif sys.platform.startswith('linux'):
        return 'Linux'


def limpiar_pantalla():
    if plataforma_sistema_operativo() == 'Windows':
        return system('cls')
    else:
        return system('clear')


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
        limpiar_pantalla()
        opc_menu = menu()
        for opc, area in opc_menu.items():
            print(f"[{opc}] - {area}")
        opcion = input("Seleccione una opción: ").lower()
        if opcion == 'p':
            limpiar_pantalla()
            print("Perfumería")
            input()
        elif opcion == 'f':
            limpiar_pantalla()
            print("Farmacia")
            input()
        elif opcion == 'c':
            limpiar_pantalla()
            print("Cosméticos")
            input()
        elif opcion != 's':
            limpiar_pantalla()
            print("Opción incorrecta")
            input()


inicio()
