##Slicing Strings
#Se puede retornar una rango de caracteres usando la sintaxis "slice"
#Se especifica el indice de inicio y fin, separado por ":", y se retorna
#una parte del string
#b = "parangaricutirimicuaro"
#print(len(b))

#print(b[0:14]) #Slice syntax
#El primer caracter tiene indice 0

#Si quitamos el indice de inicio, el rango iniciara en el primer caracter
#print(b[:12])

#Si quitamos el indice final, el rago se imprimira hasta el final
#print(b[12:])

#Indice negativo
#Usar indice negativo, se inicia el slice desde el final del string
#print(b[-14:-2])

##Modificando Strings
#Python tiene un set de metodos incorporados que puede usar en strings
#Upper Case
#El metodo upper() retorna un string en upper case.
a =  "A la grande le puse Cuca"
print(a.upper())

#El metodo lower() retorna un string en lower case.
print(a.lower())

#Remover espacio en blanco
#El metodo strip() remueve espacios en blanco antes y despues del texto
b = " Trabajo muy duro, como un esclavo "
#print(b)
print(b.strip())

#El metodo replace() reemplaza un string con otro string
print(a.replace("C","K"))

#El metodo split() retorna una lista donde el texto entre un separador especifico conviernte
#en una lista de items

print(a.split(" , "))
