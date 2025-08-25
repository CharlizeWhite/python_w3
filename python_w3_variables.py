# print("Hola Mundo!")

##Python version

#import sys
#print(sys.version)

##Indentation
#if 5 > 2:
#    print("5 es mayour que 2!")
## La indentacion incorrecta arroja el sigueinte error en la consola: "IndentationError: expected an indented block after 'if' statement on line 9"
## El número minímo de espacios de identación es 1, el estandar son 4 espacios.
## Se deben usar el mismo numero de espacios de indentacion en todo el bloque de codigo.

##Comentarios
#Se usa el hastag para hacer comentario linea por linea, no hay un simbolo para comentario multilinea
#pero de ser necesario, se usa triple-comillas-dobles para multiples lineas comentadas.
"""
Esto seria un
ejemplo de multiples
lineas comentadas
El interprete las ignora
"""

##Variables
##El tipo de variable se define cuando se crea.
#x=(type(4))
#y=(type("podcast CREATIVO"))

#print(x,y)

##Variables, continua
#Si se quiere especificar el tipo de dato de una variable, se puede hacer haciendo casting
"""
x=str(3) # x sera "3"
y=int(3) # y sera 3
z=float(3) # z sera 3.0
print(x,y,z)
"""
#Case-Sensitive
#Esto creara 2 variables
#a = 4
#A = "Leo"
#En este caso "A" no sobreecribe a "a"

#Nombrar Variables
#no admite iniciar con un numerl
#no admite guion medio  como mi-mama (esto seria incorrecto)
#no admite espacio estre palabra como my home (esto seria incorrecto)

#si adminte guion bajo (underscore)
#si adminte alfanumericos y guion bajo
#los nombres son case-sensitive age Age y AGE son tres variables diferentes

#variables declaradas con mas de una palabra (multi words)
#Existen tecnicas para hacerlo mas leibles:

#Camel case myVariableName
#Pascal case MyVariableName
#Snake case my_variable_name

#Asignando multiples valores

#varios valores para multiples variables
"""
x,y,z="manzana","platano","cereza"
print(x)
print(y)
print(z)
"""
#el numero de valores debe coincidir con el numero de variables o arrojara Error

#un valor para multiples variables
"""
x=y=z="Naranja"
print(x)
print(y)
print(z)
"""

#Desempacar una coleccion
#unpacking es extraer valores en variables de una lista o tupla
"""
frutas =["manzana","platano","cereza"]
x, y, z = frutas
print(x)
print(y)
print(z)
"""
#Salida de Variables (Output Variables)
#la función print() es la más usada para salida de variables
"""
x = "Python is a programming language"
print(x)
"""
#Se puede dar salida a multiples variables separadas por una coma (,)
"""
x = "Python is a"
y = "programming"
z = "language"
print(x, y, z)
"""
#Se puede usar '+' para concatenar multiples variables
"""
x = "Python is a "
y = "programming "
z = "language"
print(x + y + z)
"""
#Notece que hay un espacion en "Python is a " y "programming ", de lo contrario la concatenacion seria "Python is aprogramminglanguage"
# Para numeros, el operador '+' trabaja como operador matematico
"""
x = 10
y = 66
print(x + y)
"""
# si se declara una variable tipo INT y se concatena con una variable STR, producira un Error
# la mejor manera de imprimir las variables, seria imprimir las variables separadas por comas como print(x, y)

#Variables Globales
#Las variables fuera de una funcion son variables globales, y pueden ser usadas por una funcion
#Las funciones dentro de la funcion son variables locales, y solo son usadas por la funcion
#Una variable global con el mismo nombre que una variable local, permanecera con su valor original
"""
x = "awesome" #variable global

def myfunc():
    x = "fantastic" #variable local
    print("Python is " + x)
myfunc()

print("Python is " + x)
"""
# global keyword o palabra clave global
# Para crear una variable global dentro de una funcion se utiliza la palabra clave "global"
# al usar la palabra clave "global", la variable pertenece al alcance global
"""
def myfunc():
    global x
    x = "fantastic"
    
myfunc()
print("Python is " + x)
"""
#Para cambiar el valor de una variable global dentro de una funcion, refiere la funcion
# usando la palabra clave global
"""
x = "awesome" #variable global definida fuera de la funcion
def myfunc():
    global x
    x = "fantastic" #Nuevo valor de la variable globla dentro de la funcion
myfunc()
print("Python is " + x)
"""
