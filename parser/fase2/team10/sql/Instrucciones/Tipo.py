from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Tipo(Instruccion):
    def __init__(self, id, tipo, owner, id2, valor, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = Tipo("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''