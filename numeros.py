class TurnosFarmacia:
    def __init__(self,sigla):
        self.turno = 0
        self.sigla = sigla

    def generar_turno(self):

        if self.turno < 10:
            self.turno += 1
            yield self.turno
        else:
            self.turno = 1
            yield self.turno

    def decorar_turno(self, funcion):
        def imprimir_turno():
            print("Su turno es el:")
            print(f"{self.sigla}-{next(funcion())}")
            print("Aguarde y será atendido")
        return imprimir_turno()


# farmacia = TurnosFarmacia("C")
# farmacia.decorar_turno(farmacia.generar_turno)
# farmacia.decorar_turno(farmacia.generar_turno)
#
#
# perfumeria = TurnosFarmacia("P")
# perfumeria.decorar_turno(perfumeria.generar_turno)
# perfumeria.decorar_turno(perfumeria.generar_turno)
