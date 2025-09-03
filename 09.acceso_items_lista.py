#Acceso a items o elementos de la lista

#Los elementos de una Lista están indexadas y se puede dar acceso a los
#elementos refiriendo el número del index.

thislist = ["manzana", "plátano", "cereza"]
print(thislist[1])
#El primer elemento tiene indice 0

#Indice Negativo
#Significa que inicia por el final
print(thislist[-1])

#Rango de índices
#Se puede especificar un rando especificando donde empieza y donde termina.
#Especificar el rango retorna los valores en una nueva lista

thislist2 = ["mango", "plátano", "cereza", "uva", "toronja", "tuna", "durazno"]
print(thislist2[2:5])
#Esta búsqueda comienza en el índice 2, incluyéndolo, y termina en el índice 5, no incluido.

#Dejando fuera el valor de inicio, el rango empieza por el primer elemento
print(thislist2[:4])
#No incluye el índice 4

#Dejando fuera el último elemento, el rango íra hasta el final de la lista
print(thislist2[2:])

#Especifica índices negativos si deseas empezar la búsqueda desde el final de la lista
print(thislist2[-4:-1])

#Checa si el item existe
#Para determinar si el elemento esta presente en una lista, se usa la keyword 'in'
if "tuna" in thislist2:
    print("yes, 'tuna' esta en la lista de frutas")