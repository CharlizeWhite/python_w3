##String Concatenation
#Para concatenar, o combinar, 2 string se puede usar
#el operador "+"

#Merge(fusiona) la variable a con la variable b en la variable c
#a = "Homero"
#b = "Simpson"
#c = a + b
#print(c)

#Para agregar un espacio concatenamos un espacio " "

#c = a + " " + b
#print(c)

##String Format
#No se puede combinar stings y numeros para definir una variable;
#Pero podemos combinarlos usando f-strings o el metodo format()

#F-Strings
#Fue introducido en Python 3.6 y ahora es la manera preferida de
#formatear strings

#Para especificar un string como f-string, se coloca una "f" frente
#al strins, y se agrega unos corchetes de llave { } como
#placeholder o marcador de posicion para variables u otros operadores.

"""edad = 43
txt = f"Mi nombre es Cristina, Tengo {edad}"
print(txt)"""

#Marcadores y Modificadores
#Los marcadores de posicion {} pueden contener variables
#operaciones, funciones y modificadores de formato del valor.

#variable
"""price = 59"""
#txt = f"El precio es {price} dolares"
#puede incluir un modificardo para formatear el valor
#agregado ":" seguido de un tipo legal de formateado, como ".2f"
#lo cual agregara un punto y dos decimales
"""txt = f"El precio es {price:.2f} dolares"
print(txt)"""

#Puede contener codigo  python, como operaciones matematicas
#Podemos hacer una operacion en el placeholder y retornara el
#resultado
"""texto = f"El precio es {29 * 2} dolares"
print(texto)"""

#Caracter de Escape
#Para insertar un caracter ilegal en un string
#el caracter de escape es barra invertida o backslash "\" seguido
#del caracter que quiere insertar
#Un ejemplo son comillas dobles dentro de comillas dobles

txt = "Somo los llamados \"Vikingos\" del Norte."

#Otros caracteres usados en Python

# \' resulta en comilla simple
# \\ resulta en una barra invertida
# \n resulta en una nueva linea
# \r resulta en un retorno de carrete
# \t resulta en Tab
# \b resulta en Backspace
# \f resulta en Form Feed
# \ooo resulta en un valor octar
# \xhh resulta en un valor hexadecimal