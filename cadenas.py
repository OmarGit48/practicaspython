# texto_variado = "palabra 123 + - * &$%#"
# print (type(texto_variado))

# Podemos utilizar comillas triples para que el texto se muestre como la cadena que aparece aqui abajo
# print ("""
# Funcionaminto de \
# programa: (opciones)
#     -1 Para acceder a opciones
#         -2 Para salir
# """)

##############################################################
# Subscripting e Indexado

# texto = "Python"

# print (texto[0])
# print (texto[5])
# print (texto[-1])
# print (texto[-6])
# print (texto[6])  # Error! No podemos acceder a una posicion que no existe
# print (texto[-7]) # Error! No podemos acceder a una posicion que no existe

# letra = texto [0]
# print(letra)

# # texto [0] = "p" # Error! No podemo smodificar una cadena

# letra ="p"
# print (letra)

# texto_compuesto = letra + texto[1] #concatenación
# print (texto_compuesto)

#############################################################################

# Slicing o Substrining
texto ="Python"

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])
# print(texto[:])

# print(texto[-3::-1])
# print(texto[::-1])
# print(texto[1:50])
# print(texto [2:2])

########################################################################
# Cadenas y formatos      

# texto = "Hola Mundo! Buenas Tardes"
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print (texto.swapcase())

# texto = texto.upper()
# print (texto)

print("{} + {} = {}".format(2, 3, 2+3))
print("{} + {} = {}".format("hola","mundo","Hola mundo" ))
print("{:.3f} + {:.4f} = {}".format(2,3,2+3))
print ("{1} + {0} = {2}".format(2,3,2+3))
print ("{2} + {0} = {1}".format("Hola","mundo","Hola mundo"))
print ("{:d} = {:b} = {:o} = {:x}".format(15,15,15,15))
