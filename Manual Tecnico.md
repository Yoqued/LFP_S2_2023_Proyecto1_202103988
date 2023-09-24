# Funciones y Código en Tkinter para una Aplicación de Edición y Análisis de Texto del archivo 'Principal.py'

## `Abrir_Archivo()`

Esta función se encarga de abrir un archivo de texto seleccionado por el usuario utilizando el cuadro de diálogo de selección de archivo proporcionado por `filedialog.askopenfilename()`. Luego, lee el contenido del archivo y lo muestra en el área de texto `Caja_Grande` de la ventana principal de la aplicación.

## `Guardar_Archivo()`

La función `Guardar_Archivo()` se utiliza para guardar el contenido actual del área de texto `Caja_Grande` en el archivo previamente abierto. Primero, verifica si ya se ha seleccionado un archivo para guardar. Si es así, sobrescribe el archivo con el contenido actual. En caso contrario, muestra un mensaje de advertencia.

## `Guardar_Como()`

`Guardar_Como()` permite al usuario guardar el contenido del área de texto `Caja_Grande` en un nuevo archivo con un nombre especificado por el usuario. Abre una nueva ventana (`Ventana_Nombre_Arch`) donde el usuario puede ingresar el nombre del archivo y luego guarda el contenido en un archivo con ese nombre.

## `Analizar()`

Esta función realiza un análisis léxico y sintáctico del contenido en el área de texto `Caja_Grande`. Utiliza funciones importadas de módulos externos (`analizador_lexico` e `Instrucciones.aritmeticas`) para analizar y operar el contenido del texto. Los resultados del análisis se muestran en una ventana de mensaje.

## `Reporte()`

`Reporte()` se encarga de generar una gráfica con los datos resultantes del análisis y mostrar un mensaje de éxito cuando la gráfica está lista. Utiliza datos previamente analizados y almacenados en la variable `data_grafica`.

## `Errores()`

La función `Errores()` crea un archivo JSON con los errores encontrados durante el análisis y muestra un mensaje informando que el archivo ha sido generado con éxito.

# Funciones y Código para el Análisis de Texto y Generación de Informes Gráficos de archivo 'analizador_lexico.py'

## `instruccion(cadena)`

Esta función se encarga de analizar una cadena de texto y generar una lista de lexemas y errores. Recorre la cadena de entrada caracter por caracter y utiliza funciones auxiliares para identificar y clasificar lexemas, números y errores. Los lexemas válidos se almacenan en la lista `lista_lexemas`, y los errores se registran en la lista `lista_errores`. La función también se encarga de mantener un seguimiento de la línea y columna actual para rastrear la posición de los lexemas y errores.

## `armar_lexema(cadena)`

La función `armar_lexema` se utiliza para construir lexemas a partir de una cadena. Se busca el cierre de comillas dobles (`"`) en la cadena y devuelve el lexema encontrado junto con la cadena restante.

## `armar_numero(cadena)`

`armar_numero` analiza la cadena para construir números enteros o decimales. Detecta el punto (`.`) como separador decimal y devuelve el número encontrado junto con la cadena restante.

## `operar()`

Esta función es parte del proceso de análisis sintáctico y se encarga de crear instrucciones a partir de los lexemas almacenados en `lista_lexemas`. Reconoce operaciones aritméticas y trigonométricas, así como operandos, y crea objetos que representan estas instrucciones. Estos objetos se almacenan en la lista `instrucciones`.

## `operar_()`

La función `operar_()` ejecuta el análisis sintáctico y operativo de las instrucciones almacenadas en `instrucciones`. Realiza operaciones aritméticas y trigonométricas según la estructura de las instrucciones y devuelve los resultados en forma de nodos para su posterior procesamiento. También genera una representación en cadena de las operaciones realizadas.

## `Graficar(Dato)`

`Graficar()` se utiliza para generar un archivo DOT que describe un gráfico. La función extrae atributos como el color, la fuente y la forma de la lista de atributos almacenada en `lista_atributos_grafica` y los utiliza para configurar el estilo del gráfico. Luego, combina estos atributos con los datos pasados como argumento (`Dato`) y genera el archivo DOT. Finalmente, utiliza la herramienta `dot` para convertir el archivo DOT en una imagen PNG.

## `Error()`

La función `Error()` se encarga de registrar los errores léxicos encontrados durante el análisis. Si no se detectan errores, se crea un archivo JSON llamado "datos.json" con una estructura vacía. Si se encuentran errores, se generan registros de errores en formato JSON y se almacenan en el mismo archivo "datos.json". Luego, el nombre del archivo generado se devuelve como resultado.

El código completo se utiliza para analizar texto, crear gráficos, y generar informes de errores. Está diseñado para funcionar en conjunto con otras partes del programa para realizar un análisis completo de un archivo de entrada.

# Funciones y Código para el Análisis de Expresiones Aritméticas y Generación de Árboles de Expresiones

En el siguiente código, se implementa una serie de funciones y clases para realizar análisis de expresiones aritméticas y generar árboles de expresiones. El código está diseñado para ser parte de un analizador léxico y sintáctico más grande. archivo aritmeticas.py

## Clase `Aritmetica`

La clase `Aritmetica` representa una expresión aritmética. Tiene los siguientes atributos:
- `left`: El operando izquierdo de la expresión.
- `right`: El operando derecho de la expresión.
- `tipo`: El tipo de operación aritmética (suma, resta, multiplicación, división, módulo, potencia, raíz).
- `fila` y `columna`: La ubicación de la expresión en el código fuente.

La clase tiene los siguientes métodos:

### `__init__(self, left, right, tipo, fila, columna)`

El constructor de la clase `Aritmetica` inicializa los atributos de la instancia con los valores proporcionados.

### `operar(self, arbol)`

El método `operar` toma un objeto de árbol de expresiones `arbol` como argumento y realiza la operación aritmética correspondiente según el tipo de operación almacenado en `tipo`. Retorna el resultado de la operación, una representación de la operación realizada y una bandera indicando si la operación fue exitosa. También actualiza un registro temporal `temporal` que se utiliza para construir un árbol de expresiones.

### `getFila(self)`

Este método devuelve la fila en la que se encuentra la expresión en el código fuente.

### `getColumna(self)`

Este método devuelve la columna en la que se encuentra la expresión en el código fuente.

## Función `listaNodos()`

La función `listaNodos()` se encarga de inicializar una lista global `lista_nodos` con nombres de nodos para su posterior uso en la representación del árbol de expresiones.

## Uso de Nodos en la Representación del Árbol

El código utiliza una lista global `lista_nodos` para asignar nombres de nodos a medida que se construye el árbol de expresiones. Cada nodo se representa como una cadena única (por ejemplo, 'nodo0', 'nodo1', etc.). Estos nodos se utilizan para crear una representación gráfica del árbol de expresiones.

## Ejemplo de Uso

El código se puede utilizar para analizar y evaluar expresiones aritméticas, generando un árbol de expresiones y una representación gráfica de dicho árbol. Esto es útil en aplicaciones de análisis y procesamiento de lenguaje natural que involucran expresiones matemáticas.

