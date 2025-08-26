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
a = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
"""
print(a)

#Los strings son arreglos
#Cada caracter en un string tiene una posicion (indice) que empieza en 0
#Se puede acceder a un caracter usando corchetes []
b = "Hello, World!"
print(b[1])
