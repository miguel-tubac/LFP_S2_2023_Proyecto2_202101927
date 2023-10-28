# LENGUAJES FORMALES Y DE PROGRAMACIÓN
## Proyecto 2
### SEGUNDO SEMESTRE 2023
```js
Universidad San Carlos de Guatemala
Programador: Miguel Adrian Tubac agustin
Carne: 202101927
Correo: mgtubac@gmail.com
```
---
## Descripción del Proyecto
El programa fue desarrollado en el lenguaje de programación Python, el mismo permite la lectura de código fuente, el cual será ingresado con extensión .bizdata, posteriormente el programa es capaz de identificar un lenguaje dado, identificando los errores léxicos, errores sintéticos y ejecutando las instrucciones correspondientes.


## Objetivos
* Objetivos
    * Implementar una solución de software implementando los conceptos vistos en clase y laboratorio.
    * Implementar un analizador sintáctico utilizando los conceptos de gramáticas independientes de contexto y árboles de derivación.
    * Introducir a la ejecución de instrucciones en un lenguaje de programación.

---
## Elaboración de la practica
En la práctica se utilizaron las siguientes clases:

Clase ScrollText() utilizada para crear la primera area de texto en donde se mostrara el texto con extencion bizdata que se ingresara en un archivo:
![ImagenesDeMarcdown](https://i.ibb.co/P1mBk7q/image.png)

La Clase ScrollText2() permite que en el area de texto del resultado de las operaciones seleccionadas:
![ObtenerLink](https://i.ibb.co/H7X2h82/image.png)

La Clase Ventana() permite que se realicen la creacion de la ventana con Tkinter y se ejecuten las funciones que permiten el desarrollo de cada peticion:
![ObtenerLink](https://i.ibb.co/j5DTXZY/image.png)

En el documento Analizador se realizan las operacione de creacion de los Tokens e igualmente la creacion de los errores: 
![ObtenerLink](https://i.ibb.co/GkK8Qj8/image.png)

La Error() permite que se almacenen los errores lexicos que se encuentran en el archivo de analisis en la carga del mismo: 
![ObtenerLink](https://i.ibb.co/v1k1RXb/image.png)

Tabla con las funciones que se encuentran dentro del sistema de BizData:
| Función                          | Especificación                                                                                                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `ScrollText(tk.Frame)`      | Permite que en area de texto se pueda navegar y con la misma actualizar los numeros de lineas.                                          |
| `ScrollText2(tk.Frame)`           | Permite la  creacion del area de texto en donde se mostraran los Tokens que se almacenen.            |
| `Ventana(tk.Tk)`| En esta clase se declaran los atributos generales de la ventana que el usuario tendra acceso  y edicion sobre el mismo.    |
| `Error()`  | La clase establece la estructura de los errores que se almacenaran en el archivo de salida.         |
| `Arbol()`  | Muestra la información ingresada. Esta clase ademas genera los nodos correspondientes a la grafica que se genera.         |
