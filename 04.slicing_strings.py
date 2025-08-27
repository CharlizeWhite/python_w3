##Slicing Strings
#Se puede retornar una rango de caracteres usando la sintaxis "slice"
#Se especifica el indice de inicio y fin, separado por ":", y se retorna
#una parte del string
b = "parangaricutirimicuaro"
print(len(b))

print(b[0:14]) #Slice syntax
#El primer caracter tiene indice 0

#Si quitamos el indice de inicio, el rango iniciara en el primer caracter
print(b[:12])

#Si quitamos el indice final, el rago se imprimira hasta el final
print(b[12:])

#Indice negativo
#Usar indice negativo, se inicia el slice desde el final del string
print(b[-14:-2])

##Modificando Strings
