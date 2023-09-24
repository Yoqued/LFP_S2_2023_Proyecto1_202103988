from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstract.lexema import *
from Abstract.numero import *
from Abstract.errores import *
import os
import json


global n_linea
global n_columna
global instrucciones
global lista_lexemas
global listaadddd
global lista_trigonometrica
global lista_errores
global lista_atributos_grafica
global datos

datos = {
    "errores": [

    ]
}
n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []
lista_trigonometrica = ['seno', 'coseno', 'tangente', 'inverso']
lista_atributos_grafica = []
 

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    global lista_errores
    global datos
    datos = {
        "errores": [

        ]
    }

    lexema = ''
    puntero = 0
    n_linea = 1
    n_columna = 1
    lista_lexemas.clear()
    lista_errores.clear()
    lista_atributos_grafica.clear()
    instrucciones.clear()

    while cadena:
        char = cadena[puntero]
        puntero =+ 1
        
        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)
                lista_atributos_grafica.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        elif char == '\t':
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1 
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                n = Numero(token, n_linea, n_columna)
                lista_lexemas.append(n)
                lista_atributos_grafica.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':
            c = Lexema(char, n_linea, n_columna)
            lista_lexemas.append(c)
            lista_atributos_grafica.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1 
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            e = Errores(char, n_linea, n_columna)
            lista_errores.append(e)
            cadena = cadena[1:]
            puntero = 0
            n_columna = 1
    

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True
        if char == '\"' or char == ' ' or char == '\n' or char == '\t' or char == ',':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            numero += char
    return None, None

def operar():
    global lista_lexemas
    global instrucciones

    operacion = ''
    n1 = ''
    n2 = ''

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')
        if operacion and n1 and operacion.operar(None) in lista_trigonometrica:
            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def operar_():
    global instrucciones
    nodos = ''
    resultados = ''

    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
        
    for instruccion in instrucciones:
        res, exp, _, hola, _ = instruccion.operar(None)
        nodos = nodos + hola
        resultados += exp +'\n'
    
    return nodos, resultados
    
def Graficar(Dato):
    global lista_atributos_grafica

    while lista_atributos_grafica:
        token = lista_atributos_grafica.pop(0)

        if token.operar(None) == 'texto':
            titulo = lista_atributos_grafica.pop(0)
        elif token.operar(None) == 'fondo':
            color = lista_atributos_grafica.pop(0)
        elif token.operar(None) == 'fuente':
            fuente = lista_atributos_grafica.pop(0)
        elif token.operar(None) == 'forma':
            forma = lista_atributos_grafica.pop(0)
    
    Nodo = '''digraph{\n'''

    colorsito = color.operar(None).lower()

    if colorsito == 'amarillo' or colorsito == '#ffff00':
        Nodo += f'node[fillcolor = "yellow"'
    elif colorsito == 'rojo' or colorsito == '#ff0000':
        Nodo += f'node[fillcolor = "red"'
    elif colorsito == 'azul' or colorsito == '#0000FF':
        Nodo += f'node[fillcolor = "blue"'
    elif colorsito == 'rosado' or colorsito == '#FFC0CB':
        Nodo += f'node[fillcolor = "pink"'
    elif colorsito == 'anaranjado' or colorsito == '#FFA500':
        Nodo += f'node[fillcolor = "orange"'
    elif colorsito == 'verde' or colorsito == '#008000':
        Nodo += f'node[fillcolor = "green"'
    elif colorsito == 'cafe' or colorsito == '#A52A2A':
        Nodo += f'node[fillcolor = "brown"'
    elif colorsito == 'morado' or colorsito == '#800080':
        Nodo += f'node[fillcolor = "purple"'


    fuentesita = fuente.operar(None).lower()

    if fuentesita == 'amarillo' or fuentesita == '#ffff00':
        Nodo += f' fontcolor = "yellow"'
    elif fuentesita == 'rojo' or fuentesita == '#ff0000': 
        Nodo += f' fontcolor = "red"'
    elif fuentesita == 'azul' or fuentesita == '#0000FF': 
        Nodo += f' fontcolor = "azul"'
    elif fuentesita == 'rosado' or fuentesita == '#FFC0CB': 
        Nodo += f' fontcolor = "red"'
    elif fuentesita == 'anaranjado' or fuentesita == '#FFA500': 
        Nodo += f' fontcolor = "anaranjado"'
    elif fuentesita == 'verde' or fuentesita == '#008000': 
        Nodo += f' fontcolor = "verde"'
    elif fuentesita == 'cafe' or fuentesita == '#A52A2A': 
        Nodo += f' fontcolor = "cafe"'
    elif fuentesita == 'morado' or fuentesita == '#800080': 
        Nodo += f' fontcolor = "morado"'
    elif fuentesita == 'blanco' or fuentesita == '#FFFFFF': 
        Nodo += f' fontcolor = "white"'

    formita = forma.operar(None).lower()

    if formita == "cuadrado":
        Nodo += f' shape = "square"'
    if formita == "circulo":
        Nodo += f' shape = "circle"'
    if formita == "ovalo":
        Nodo += f' shape = "oval"'
    if formita == "triangulo":
        Nodo += f' shape = "triangle"'
    if formita == "rectangulo":
        Nodo += f' shape = "rectangle"'
    if formita == "rombo":
        Nodo += f' shape = "rhombus"'
    if formita == "estrella":
        Nodo += f' shape = "star"'
    if formita == "hexagono":
        Nodo += f' shape = "hexagon"'
    
    Nodo += " style = filled]\n"

    Nodo += Dato

    Nodo += '''\n}'''

    with open('Reporte.dot', 'w') as f:
        f.write(Nodo)
    
    os.system('dot -Tpng Reporte.dot -o Reporte.png')

def Error():
    global lista_errores
    if not lista_errores:
        nombre_archivo = "datos.json"
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)

        return nombre_archivo
    else:
        i = 1
        for error in lista_errores:
            nuevo_error = {
                    "No": i,
                    "descripcion": {
                        "lexema": str(error.operar(None)),
                        "tipo": "error lexico",
                        "columna": str(error.getColumna()),
                        "fila": str(error.getFila())
                    }
                }
            datos["errores"].append(nuevo_error)
            nombre_archivo = "datos.json"
            i += 1
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)

        return nombre_archivo


'''entrada = {
  "operaciones": [
    {
      "operacion": "suma",
      "valor1": 6,
      "valor2": 6
    },
    {
      "operacion": "multiplicacion",
      "valor1": 4.5,
      "valor2": [
        { ?
          "operacion": "potencia",
          "valor1": 10,
          "valor2": 3
        }
      ]
    },
    {
      "operacion": "suma",
      "valor1": [
        {
            "operacion": "raiz",
            "valor1": 90,
	        "valor2": 5
        }
      ],
      "valor2": [
        {
            "operacion": "potencia",
            "valor1": 2,
	        "valor2": 6
        }
      ]
    },
    {
      "operacion": "multiplicacion",
      "valor1": 7,
      "valor2": 3
    },
    {
      "operacion": "tangente",
      "valor1":[
        {
          "operacion": "inverso",
          "valor1": [
        {
          "operacion": "seno",
          "valor1": 90
        }
      ]
        }
      ]
    }
  ],
  "configuraciones": [
    {
      "texto": "Operaciones",
      "fondo": "amarillo",
      "fuente": "negro",
      "forma": "estrella"
    }
  ]
}'''

'''listaNodos()
instruccion(entrada)
o = operar_()
Graficar(o)'''