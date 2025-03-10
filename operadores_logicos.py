'''
Operadores logicos

Aquellos que operan unicamente
con valores booleanos (V F)
Acorde a las tablas de Verdad 
'''
# Ejemplo 1: Operador not:
y = not True
print("El resultado de operar con not es", y)

# Ejemplo 2: Operador and:
y = False and True
print("El resultado de operar con and es", y)

# Ejemplo 3: Operador or:
y = False or False
print("El resultado de operar con or es", y)

'''
Jerarquia de presendecia de operadores
(loicos inclusive)
1.            ()
2.            **
3.            /, //, %   
4.            +, - 
5.            >, <, >=, <=, !=, ==
6.            not
7.            and
8.            or
9.            =
'''

# Ejemplo 4: Jerarquia de presendecia de operadores
y = False and not True or False
print("El resultado de operar con jerarquia de operaciones es", y)

# Ejemplo 5: Operadores relacionales y logicos
y = not 3 > 4 and 4 == 4 or 3 < 2
print("El resultado de operar con jerarquia de operaciones es", y)


