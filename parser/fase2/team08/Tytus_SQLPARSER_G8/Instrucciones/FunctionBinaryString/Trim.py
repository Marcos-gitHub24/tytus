from numpy.core.defchararray import strip
from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import *
from Instrucciones.Expresiones.Aritmetica import Aritmetica

class Trim(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
            self.tipo = Tipo(Tipo_Dato.TEXT)
            return strip(str(resultado)) 
        error = Excepcion('42883',"Semántico",f"No existe la función TRIM({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error
    
    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        if isinstance(self.valor, Primitivo):
            return f"TRIM({self.valor.traducir(tabla,arbol).temporalAnterior})"
        elif isinstance(self.valor, Aritmetica):
            return f"TRIM({self.valor.concatenar(tabla,arbol)})"
        elif isinstance(self.valor, str) or isinstance(self.valor, int):
            return f"TRIM({self.valor})"
        return f"TRIM({self.valor.traducir(tabla,arbol)})"
    
