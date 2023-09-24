from Abstract.abstract import Expression

global lista_nodos
global temporal
lista_nodos = []
temporal = ''

def listaNodos():
    global lista_nodos
    lista_nodos.clear()
    for i in range(400):
        lista_nodos.append('nodo'+str(i))

class Aritmetica(Expression):
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        global temporal
        leftValue = ''
        rightValue = ''
        resultado = ''
        leftState = False
        rightState = False
        resultadoI = ''
        resultadoD = ''
        temporal = ''

        if self.left != None:
            leftValue, resultadoI, leftState, data_left, nodo_left = self.left.operar(arbol)
            temporal = ''
        if self.right != None:
            rightValue, resultadoD, rightState, data_right, nodo_right = self.right.operar(arbol)
            temporal = ''
        
        if self.tipo.operar(arbol) == 'suma':
            if leftState is False  and rightState is False:
                resultado = 'Suma = '+str(leftValue)+' + '+str(rightValue)+' = '+ str(leftValue + rightValue)
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue + rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Suma: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Suma = ('+str(resultadoI)+') + '+str(rightValue)+' = '+ str(leftValue + rightValue)
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue + rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Suma: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Suma = '+str(leftValue)+' + ('+str(resultadoD)+') = '+ str(leftValue + rightValue)
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue + rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Suma: {fomateado}"]\n'
                temporal += data_right 
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Suma = ('+str(resultadoI)+') + ('+str(resultadoD)+') = '+ str(leftValue + rightValue)
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue + rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Suma: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            return leftValue + rightValue, resultado, True, temporal, finalNodo
        if self.tipo.operar(arbol) == 'resta':
            if leftState is False  and rightState is False:
                resultado = 'Resta = '+str(leftValue)+' - '+str(rightValue)+' = '+ str(leftValue - rightValue)
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue - rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Resta: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Resta = ('+str(resultadoI)+') - '+str(rightValue)+' = '+ str(leftValue - rightValue)
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue - rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Resta: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Resta = '+str(leftValue)+' - ('+str(resultadoD)+') = '+ str(leftValue - rightValue)
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue - rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Resta: {fomateado}"]\n'
                temporal += data_right
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Resta = ('+str(resultadoI)+') - ('+str(resultadoD)+') = '+ str(leftValue - rightValue)
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue - rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Resta: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'
                

            return leftValue - rightValue, resultado, True, temporal, finalNodo
        if self.tipo.operar(arbol) == 'multiplicacion':
            if leftState is False  and rightState is False:
                resultado = 'Multiplicacion = '+str(leftValue)+' * '+str(rightValue)+' = '+ str(leftValue * rightValue)
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue * rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Multiplicacion: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Multiplicacion = ('+str(resultadoI)+') * '+str(rightValue)+' = '+ str(leftValue * rightValue)
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue * rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Multiplicacion: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Multiplicacion = '+str(leftValue)+' * ('+str(resultadoD)+') = '+ str(leftValue * rightValue)
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue * rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Multiplicacion: {fomateado}"]\n'
                temporal += data_right
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Multiplicacion = ('+str(resultadoI)+') * ('+str(resultadoD)+') = '+ str(leftValue * rightValue)
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue * rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Multiplicacion: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            return leftValue * rightValue, resultado, True, temporal, finalNodo
        if self.tipo.operar(arbol) == 'division':
            if leftState is False  and rightState is False:
                resultado = 'Division = '+str(leftValue)+' / '+str(rightValue)+' = '+ str(leftValue / rightValue)
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue / rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Division: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Division = ('+str(resultadoI)+') / '+str(rightValue)+' = '+ str(leftValue / rightValue)
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue / rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Division: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Division = '+str(leftValue)+' / ('+str(resultadoD)+') = '+ str(leftValue / rightValue)
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue / rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Division: {fomateado}"]\n'
                temporal += data_right
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Division = ('+str(resultadoI)+') / ('+str(resultadoD)+') = '+ str(leftValue / rightValue)
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue / rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Division: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            return leftValue / rightValue, resultado, True, temporal, finalNodo
        if self.tipo.operar(arbol) == 'mod':
            if leftState is False  and rightState is False:
                resultado = 'Modulo = '+str(leftValue)+' % '+str(rightValue)+' = '+ str(leftValue % rightValue)
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue % rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Modulo: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Modulo = ('+str(resultadoI)+') % '+str(rightValue)+' = '+ str(leftValue % rightValue)
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue % rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Modulo: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Modulo = '+str(leftValue)+' % ('+str(resultadoD)+') = '+ str(leftValue % rightValue)
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue % rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Modulo: {fomateado}"]\n'
                temporal += data_right
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Modulo = ('+str(resultadoI)+') % ('+str(resultadoD)+') = '+ str(leftValue % rightValue)
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue % rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Modulo: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            return leftValue % rightValue, resultado, True, temporal, finalNodo
        if self.tipo.operar(arbol) == 'potencia':
            if leftState is False  and rightState is False:
                resultado = 'Potencia = '+str(leftValue)+' ^ '+str(rightValue)+' = '+ str(leftValue ** rightValue)
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Potencia: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Potencia = ('+str(resultadoI)+') ^ '+str(rightValue)+' = '+ str(leftValue ** rightValue)
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Potencia: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Potencia = '+str(leftValue)+' ^ ('+str(resultadoD)+') = '+ str(leftValue ** rightValue)
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Potencia: {fomateado}"]\n'
                temporal += data_right
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Potencia = ('+str(resultadoI)+') ^ ('+str(resultadoD)+') = '+ str(leftValue ** rightValue)
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** rightValue
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Potencia: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            return leftValue ** rightValue, resultado, True, temporal, finalNodo
        if self.tipo.operar(arbol) == 'raiz':
            if leftState is False  and rightState is False:
                resultado = 'Raiz = '+str(leftValue)+' ^ 1/'+str(rightValue)+' = '+ str(leftValue ** (1/rightValue))
                temporal += data_left
                temporal += data_right
                nodoIzquierdo = lista_nodos.pop(0)
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** (1/rightValue)
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Raiz: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is True and rightState is False:
                resultado = 'Raiz = ('+str(resultadoI)+') ^ 1/'+str(rightValue)+' = '+ str(leftValue ** (1/rightValue))
                temporal += data_left
                temporal += data_right
                nodoDerecho = lista_nodos.pop(0)
                temporal += f'{nodoDerecho}[label = "{rightValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** (1/rightValue)
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Raiz: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodoDerecho}\n'

            elif leftState is False and rightState is True:
                resultado = 'Raiz = '+str(leftValue)+' ^ 1/('+str(resultadoD)+') = '+ str(leftValue ** (1/rightValue))
                temporal += data_left
                nodoIzquierdo = lista_nodos.pop(0)
                temporal += f'{nodoIzquierdo}[label = "{leftValue}"]\n'
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** (1/rightValue)
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Raiz: {fomateado}"]\n'
                temporal += data_right
                temporal += f'{finalNodo}->{nodoIzquierdo}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            elif leftState is True and rightState is True:
                resultado = 'Raiz = ('+str(resultadoI)+') ^ 1/('+str(resultadoD)+') = '+ str(leftValue ** (1/rightValue))
                temporal += data_left
                temporal += data_right
                finalNodo = lista_nodos.pop(0)
                operacion = leftValue ** (1/rightValue)
                fomateado = '{:.2f}'.format(operacion)
                temporal += f'{finalNodo}[label = "Raiz: {fomateado}"]\n'
                temporal += f'{finalNodo}->{nodo_left}\n'
                temporal += f'{finalNodo}->{nodo_right}\n'

            return leftValue ** (1/rightValue), resultado, True, temporal, finalNodo
        else:
            return None, None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()