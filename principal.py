from os import system
from sysconfig import sys
import numeros


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
    sigla_turnero = list(menu().keys())
    perfumeria = numeros.TurnosFarmacia(sigla_turnero[0])
    farmacia = numeros.TurnosFarmacia(sigla_turnero[1])
    cosmeticos = numeros.TurnosFarmacia(sigla_turnero[2])
    while opcion != "s":
        limpiar_pantalla()
        opc_menu = menu()
        for opc, area in opc_menu.items():
            print(f"[{opc}] - {area}")
        opcion = input("Seleccione una opción: ").lower()
        if opcion == 'p':
            limpiar_pantalla()
            perfumeria.decorar_turno(perfumeria.generar_turno)
            input()
        elif opcion == 'f':
            limpiar_pantalla()
            farmacia.decorar_turno(farmacia.generar_turno)
            input()
        elif opcion == 'c':
            limpiar_pantalla()
            cosmeticos.decorar_turno(cosmeticos.generar_turno)
            input()
        elif opcion != 's':
            limpiar_pantalla()
            print("Opción incorrecta")
            input()


inicio()
