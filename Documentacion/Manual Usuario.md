# LENGUAJES FORMALES Y DE PROGRAMACIÓN
## Manual De Usuario, Proyecto 2 
### SEGUNDO SEMESTRE 2023
```js
Universidad San Carlos de Guatemala
Programador: Miguel Adrian Tubac agustin
Carne: 202101927
Correo: mgtubac@gmail.com
```
---
## Descripción del Proyecto
El programa permite la lectura de código fuente, el cual tendrá un formato bizdata, posteriormente el programa es capaz de identificar un lenguaje dado, identificando los errores léxicos, sintáctico y ejecutando las instrucciones correspondientes. 


## Objetivos
* Objetivos
    * Implementar una solución de software implementando los conceptos vistos en clase y laboratorio.
    * Implementar un analizador sintáctico utilizando los conceptos de gramáticas independientes de contexto y árboles de derivación.
    * Introducir a la ejecución de instrucciones en un lenguaje de programación. 

---
## Utilización de la interfaz 
En la ejecucion de la aplicaion seran visibles y accedibles los siguientes objetos graficos:

La ventana principal cuanta con la siguiente apariencia:
![ImagenesDeMarcdown](https://i.ibb.co/DKmcmnN/image.png)
Las funciones de cada boton son las siguientes:
* Salir: Con esta opción se cerrará la aplicación
* Abrir: Permite seleccionar los archivos que se analizaran en la entrada.
* Analizar: Permite el analisis del texto ingresado en el area de texto y la creacion de los Tokens.
* Reportes:
    * Rep. Tokens: Permite mostrar en el area de texto del lado derecho los Tokens ingresados e igualmente analizados.
    * Rep. Errores: Permite mostrar en el area de texto del lado derecho los Tokens  de errores analizados.
    * Árbol de derivación: Muestra la creacion de del arbol de cada operacion que se realizo a partir del archivo analizado.
    

Al ingresar un archivo bizdata, este se mostrara en el area de texto:
![ObtenerLink](https://i.ibb.co/xCYg9kr/image.png)

Al presionar el boton de `Analizar` este producira un mensaje indicando que se anilizo el texto exitosamente:
![ObtenerLink](https://i.ibb.co/Cw3LNr9/image.png)

Al seleciona el boton de `Rep. Tokens` se mostraran los Tokens analizados y cargados en el sistema:
![ObtenerLink](https://i.ibb.co/pzp6k0v/image.png)

Al seleciona el boton de `Rep. Errores` se mostraran los Tokens de errores analizados y cargados en el sistema:
![ObtenerLink](https://i.ibb.co/8PK739V/image.png)



Posteriormente al seleccionar el boton `salir` el programa terminara si ejecucion y se cerrara.
