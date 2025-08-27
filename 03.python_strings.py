##Python Strings
#Comillas dentro de comillas
#Se puede usar comillas simples dentro de comillas dobles y viceversa
"""
print("It's a beautiful day")
print('He said "Hello" to me')
"""
#Si se usan las mismas comillas, se debe usar el caracter de escape \
"""
print('It\'s a beautiful day')
print("He said \"Hello\" to me")
"""
#Multilineas
#Se pueden usar triples comillas simples o dobles para crear strings de multiples lineas
#a = """
#Lorem ipsum dolor sit amet, consectetur adipiscing elit,
#sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
#Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
#"""
#print(a)

#Los strings son arreglos
#Cada caracter en un string tiene una posicion (indice) que empieza en 0
#Se puede acceder a un caracter usando corchetes []
#b = "Hello, World!"
#print(b[1])

#Looping a traves de un string
#Como los string son arrays, se puede hacer un bucle con las letras del string con for()
"""for x in "parangaricutirimicuaro":
    print(x)"""

#Largo del string
#Para obtener la longitud o largo del string usamos la función len()
"""a = "parangaricutirimicuaro"
print(len(a))"""

#Chequeo del String
#Para checar si cierta frase o caracter esta presente en el string, podemos usar el keyword "in"
txt = "parangaricutirimicuaro"
print("a" in txt)

#usando una declaración con "if"
if "a" in txt:
    print("Si, 'a' esta presente")

#Checando si NO
#Para checar que una cierta frase o caracter NO esta presente en un string usamos la keyword "not_in"
print("x" not in txt)

#Usado en una declaracion "if":
if "x" not in txt:
    print("No, 'X' no esta presente")