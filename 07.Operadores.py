##Operadores
#los operadores son usados para realizar operaciones en variables
#y valores

#Python divide a los operadores en los siguientes grupos

#Aritmeticos
#Asignacion
#Comparacion
#Logicos
#Identidad
#Membresia
#Operadores Bitwise

#Operadores Aritmeticos
# '+' -> suma
# '-' -> resta
# '*' -> multiplicacion
# '/' -> division
# '%' -> modulus -> retorna el residuo de una division no exacta
# '**' -> exponencia
# '//' -> floor division (Division entera ó por el suelo)
# devuelve solo numeros enteros de una division, descartando decimales.

#Operadores de Asignacion de Python
# Operador      Ejemplo     Igual que
# '='           x = 5
# '+='          x += 3      x = x + 3
# '-='          x -= 3      x = x - 3
# '*='          x *= 3      x = x * 3
# '/='          x /= 3      x = x / 3
# '%='          x %= 3      x = x % 3
# '//='         x//= 3      x = x// 3
# '**='         x**= 3      x = x** 3
# '&='          x &= 3      x = X & 3
# '|='          x |= 3      x = x | 3
# '^='          x ^= 3      x = x ^ 3
# '>>='         x>>= 3      x = x>> 3
# '<<='         x<<= 3      x = x<< 3
# ':='          print(x := 3)   x = 3
#                               print(x)

#Operadores de comparacion
# '=='      Igual
# '!='      No Igual
# '>'       Mayor que
# '<'       Menor que
# '>='      Mayor o igual a
# '<='      Menor o igual a

#Operadores Logicos
# 'and'     retorna True si ambas declaraciones son True
# 'or'      retorna True si una de las declaraciones es True
# 'not'     reversa del resultado
#           retorna False si el resultado es True

#Operadores de Identidad
# 'is'      Retorna True si ambas variables son el mismo objeto
# 'is not'  Retorna True si amboas variables no son el mismo objeto

#Operadores de Membresia
# 'in'      Retorna True si la secuencia con el valor especificado esta presente en el objeto
# 'not in'  Retorna True si la secuencia con el valor especificado no esta presente en el objeto

#Operadores Bitwise de Python
# '&'           AND             Establece cada bit a 1 si ambos bits son 1
# '|'           OR              Establece cdad bit a 1 si uno de dos bits es 1
# '^'           XOR             Establece cada bit a 1 si solo 1 de dos bits son 1
# '~'           NOT             Invierte todos los bits
# '<<'  Zero fill left shift    Desplaza todos los bits de un número hacia la izquierda una cantidad específica de posiciones. Los espacios vacíos que quedan a la derecha se rellenan con ceros, y los bits que se "salen" por la izquierda se descartan
# '>>'  Signed right shift      Desplaza todos los bits hacia la derecha, pero mantiene el signo del número

#Operador de Precedencia
#Describe el orden en el cual se realizan las operaciones.
#El orden de precedencia es decrita empezando con la precedencia más alta en el top

# '()'              parentesis
# '**'              exponentes
# '+x -x ~x'        unary plus, unary minus, bitwise NOT
# '* / // %'        multiplicacion, division, floor division, modulus
# '+ -'             suma resta
# '<< >>'           bitwise left and right shifts
# '&'               bitwise AND
# '^'               bitwise XOR
# '|'               bitwise OR
# '== != > >='      Comparasion, identidad y membresia
# '< <= is is not'
# 'in not int'
# 'not'             Logical NOT
# 'and'             AND
# 'or'              OR