'''
Estructura de control if:
Se utiliza para tomar desiciones
basadas en expresiones condicionales
'''

#ejemplo 1: if SIMPLE
temperatura = int(input ("Ingresa la temperatura:"))
#condicional: si la temperatura es mayor o igual a 80
if temperatura > 80:
    #codigo para cuando es menor a 80
    print("Es mayor la temperatura de la maquina")
else:
        #codigo para cuando es menor de 80
    print("Es menor la temperatura, debe apagarse")
#codigo que se ejecuta siempre
print("Fin del programa")