# Funciones y Código en Tkinter para una Aplicación de Edición y Análisis de Texto

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

## `info()`

Esta función muestra una ventana de mensaje con información sobre el nombre del curso, el nombre del estudiante y el carné del estudiante.

El código completo se basa en la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI) que permite abrir, editar y analizar archivos de texto, así como generar informes y gráficos a partir de los datos analizados. Las funciones y menús proporcionan funcionalidad y opciones para interactuar con el programa de manera efectiva.
