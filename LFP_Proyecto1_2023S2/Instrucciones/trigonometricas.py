from Abstract.abstract import Expression
from Instrucciones.aritmeticas import *
from math import *

class Trigonometrica(Expression):
    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        resultado = ''
        leftState = False

        if self.left != None:
            leftValue, resultado, leftState, data_left, nodo_left = self.left.operar(arbol)
            nodoIzquierdo = lista_nodos.pop(0)
            fomateado = '{:.2f}'.format(leftValue)
            data_left += f'{nodoIzquierdo}[label = "{fomateado}"]\n'

        if self.tipo.operar(arbol) == 'seno':
            if leftState is True:
                resultado = 'Seno = ('+str(resultado)+') = '+ str(sin(leftValue))
                finalNodo = lista_nodos.pop(0)
                operacion = sin(leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Seno: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'
                data_left += f'{nodoIzquierdo}->{nodo_left}\n'

            else:
                resultado = 'Seno = '+str(leftValue)+' = '+ str(sin(leftValue))   
                finalNodo = lista_nodos.pop(0)
                operacion = sin(leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Seno: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'

            return sin(leftValue), resultado, True, data_left, finalNodo
        elif self.tipo.operar(arbol) == 'coseno':
            if leftState is True:
                resultado = 'Coseno = ('+str(resultado)+') = '+ str(cos(leftValue))
                finalNodo = lista_nodos.pop(0)
                operacion = cos(leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Coseno: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'
                data_left += f'{nodoIzquierdo}->{nodo_left}\n'

            else:
                resultado = 'Coseno = '+str(leftValue)+' = '+ str(cos(leftValue))
                finalNodo = lista_nodos.pop(0)
                operacion = cos(leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Coseno: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'

            return cos(leftValue), resultado, True, data_left, finalNodo
        elif self.tipo.operar(arbol) == 'tangente':
            if leftState is True:
                resultado = 'Tangente = ('+str(resultado)+') = '+ str(tan(leftValue))
                finalNodo = lista_nodos.pop(0)
                operacion = tan(leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Tangente: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'
                data_left += f'{nodoIzquierdo}->{nodo_left}\n'

            else:
                resultado = 'Tangente = '+str(leftValue)+' = '+ str(tan(leftValue))
                finalNodo = lista_nodos.pop(0)
                operacion = tan(leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Tangente: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'

            return tan(leftValue), resultado, True, data_left, finalNodo
        elif self.tipo.operar(arbol) == 'inverso':
            if leftState is True:
                resultado = 'Inverso = ('+str(resultado)+') = '+ str(1 / leftValue)
                finalNodo = lista_nodos.pop(0)
                operacion = (1 / leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Inverso: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'
                data_left += f'{nodoIzquierdo}->{nodo_left}\n'

            else:
                resultado = 'Inverso = '+str(leftValue)+' = '+ str(1 / leftValue)
                finalNodo = lista_nodos.pop(0)
                operacion = (1 / leftValue)
                fomateado = '{:.2f}'.format(operacion)
                data_left += f'{finalNodo}[label = "Inverso: {fomateado}"]\n'
                data_left += f'{finalNodo}->{nodoIzquierdo}\n'

            return 1 / leftValue, resultado, True, data_left, finalNodo
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()