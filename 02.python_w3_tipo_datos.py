##Tipo de Datos

# Las variables pueden almacenar datos de diferentes tipos
# y diferentes tipos pueden hacer diferentes cosas

#Tipo de Dato
#Texto = str
#Numeros = int,float,complex
#Secuencias = list,tuple,range
#Mapping = dict
#Set = set,frozenset
#Booleano = bool
#Binario = bytes,bytearray,memoryview
#None = NoneType

#Obtener el tipo de dato
#se puede obtener el tipo de dato usando la funcion type()
"""
x = 5
print(type(x))
"""
# el output seria el siguiente: <class 'int'>

#Configurando el Tipo de Dato
#En Python el tipo de dato se establece hasta que se asigna valor a la variable
"""
x = "Hello World" -> tipo de dato 'str'
x = 20 -> int
x = 20.5 -> float
x =  1j -> complex
x = ["apple","banana","cherry"] -> list
x = ("apple","banana","cherry") -> tuple
x = range(6) -> range
x = {"name":"John","age":20} -> dict
x = {"apple","banana","cherry"} -> set
x = frozenset(("apple","banana","cherry")) -> frozenset
x = True -> bool
x = b"Hello" -> bytes
x = bytearray(5) -> bytearray
x = memoryview(bytes(5)) -> memoryview
x = None -> NoneType
"""
#Configurando el Tipo de Dato especifico
#Si se quiere especificar el dato, se puede usar la siguientes funciones constructuras:
"""
x = str("hello world") data type -> str
x = int(20) data type -> int
x = float(20.5) data type -> float
x = complex(1j) data type -> complex
x = list(("apple","banana","cherry")) -> list
x = tuple(("apple","banana","cherry")) -> tuple
x = range(6) -> range
x = dict((name="John, age=36")) -> dict
x = set(("apple","banana","cherry")) -> set
x = frozenset(("apple","banana","cherry")) -> frozenset
x = bool(5) -> bool
x = bytes(5) -> bytes
x = bytearray(5) -> bytearray
x = memoryview(bytes(5)) -> memoryview
"""
## Numeros en Python
#Conversion de tipo
#Se puede convertir de un tipo a otro con los metodos int(), float() y complex().
#***Un numero complex no puede convertirse en otro tipo***
"""
x = 1 # int
y = 2.8 #float
z = 1j #complex
#convertir de int a float
a = float(x)

#convertir de float a int
b = int(y)

#convertir de int a complex
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
"""
##****No se puede convertir un numero complejo a cualquier otro tipo****
##Numeros aleatorios
#Python no tiene una funcion para generar numeros aleatorios; pero tiene un modulo incorporado
#llamado random que puede ser usado para hacer numeros aleatorios
"""
import random
print(random.randrange(1,10))
"""

