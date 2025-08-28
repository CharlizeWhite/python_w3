##Python Booleans
#Representan uno de dos valores: True o False
#Se puede evaluar cualquier expresion y obtener True o False
#Cuando se comparan dos valores y la expresión es evaluada
#se retorna una respuesta Booleana

"""print(10>9)
print ("8" == 8)
print(10<9)"""

#Cuando se realiza una exprexion en una declaracion "if"
#Python retorna True o False

"""a = 125
b = 99
if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")"""

#Evaluando Valores y Variables
#La funcion bool() permite evaluar cualquier valor
#y dar un retorno True o False
#Evaluando un valor
"""print(bool("Hello"))
print(bool(15))"""

#evaluando una variable
"""x = "Distant"
y = 14
print(bool(x))
print(bool(y))"""

#La mayoria de los valores son True
#Cualquier string es True, excepto stings vacios
#Cualquier numero es True, excepto 0.
#Cualquier lista, tulpa, set y dict son True, excepto los vacios.
"""bool("abc")
bool(123)
bool(["apple","banana","cherry"])"""

#Algunos valores son False
#No hay muchos valores evaluados como False, excepto valores vacios
#como (),[],{},"", el numero 0 y el valor "None"
# y claro el valor False se evalua como False
"""bool(False)
bool(None)
bool(0)
bool("")
bool({})
bool([])
bool(())"""

#Una clase con la función _len_ que retorne 0 tambien sera evaluada como False
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

#Las funciones pueden retornar un Booleano
#Se puede crear una función que retorne un valor booleano
def myfunc():
    return True
print(myfunc())

#Se puedo ejecutar codigo basado en una respuesta booleana de una función
def myfunc2():
    return True
if myfunc2():
    print("YES!")
else:
    print("NO!")

#Python también funciones incorporadas que devuelven un valor booleano,
#como la función isinstance(), que se puede utilizar para determinar
#si un objeto es de cierto tipo de datos:
x = 200
print(isinstance(x, int))