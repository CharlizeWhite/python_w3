##Python Booleans
#Representan uno de dos valores: True o False
#Se puede evaluar cualquier expresion y obtener True o False
#Cuando se comparan dos valores y la expresión es evaluada
#se retorna una respuesta Booleana

print(10>9)
print ("8" == 8)
print(10<9)

#Cuando se realiza una exprexion en una declaracion "if"
#Python retorna True o False

a = 125
b = 99
if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")

#Evaluando Valores y Variables
#La funcion bool() permite evaluar cualquier valor
#y dar un retorno True o False
#Evaluando un valor
print(bool("Hello"))
print(bool(15))

#evaluando una variable
x = "Distant"
y = 14
print(bool(x))
print(bool(y))

#La mayoria de los valores son True
#Cualquier string es True, excepto stings vacios
#Cualquier numero es True, excepto 0.
#Cualquier lista, tulpa, set y dict son True, excepto los vacios.

#Algunos valores son False
#No hay muchos valores evaluados como False, excepto valores vacios
#como (),[],{},"", el numero 0 y el valor "None"
# y claro el valor False se evalua como False