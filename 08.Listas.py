##Listas

#Las listas son usadas para almacenar multiples items en una sola variable

#Hay 4 maneras de almacenar 'Colecciones de datos' con diferentes cualidades y usos
    #Listas
    #Tuplas
    #Sets
    #Diccionarios

#Las listas son creadas usando los corchetes cuadrados

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Elementos de la Lista
#Los elementos de la lista se ordenan, cambian y permiten valores duplicados
#Los elementos son indexados,
#iniciando el primer elemento con [0], el segundo [1], etc.

#Ordenado
#Cuando se dice que las Listan están ordenadas, significa que los items
#tienen un orden definido, y ese orden no cambia

#Cuando se agregan nuevos items, el nuevo item se coloca al final de la lista
#Hay algunos metodos que pueden cambiar el orden, pero en general el orden
#no cambia

#Cambiante
#Las listas son cambiantes, significa que puenden cambiar, agregar y remover
#elementos de una lista después de ser creada

#Permite Duplicados
#Dado que las listas están indexadas, pueden tener elementos
#con los mismos valores

thislist1 = ["apple", "banana", "cherry","apple", "orange"]
print(thislist1)


#Largo de la lista
#La funcion 'len()' se utiliza para para determinar cuantos elementos hay en la lista
print(len(thislist1))

#Las listas pueden tener cualquier Tipo de Dato y pueden contener diferentes Tipos de Datos

#type()
#Desde la perspectiva de Python, las listas son definidas como un Tipo de Dato 'list'
print(type(thislist1))

#Constructor 'list()'
#Es posible usar el constructor 'list()' cuando creas una lista nueva
thislist2 = list(("Plaqueta", "Chimichurri", "Muneca", "Rocco")) #nota el doble parentesis
print(thislist2)

#Colecciones Python(Arrays)
#Hay 4 tipo de datos de colecciones en Python:
#List, coleccion ordenada, cambiable y permite valores duplicados

#Tuple, es ordenada y no-cambiable. Permite valores duplicados.

#Set, coleccion no-ordenada, no-cambiable (aunque se pueden agregar y remover items), un-indexada
# no permite items duplicados

#Dictionary es una coleccion ordenada, cambiable, no permite items duplicados.

#Al elegir un tipo de colección, es útil entender las propiedades de ese tipo.
#Elegir el tipo adecuado para un conjunto de datos en particular podría significar
#la retención de significado, y, podría significar un aumento de la eficiencia o la seguridad.