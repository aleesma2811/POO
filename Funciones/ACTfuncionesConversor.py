#Crear una funcion que convierta grados C a grados F.
#F = (°C * 9/5) + 32

#Crear una funcion que reciba n nombres. 
#El primer nombre será el nombre del usuario, el segundo el nombre de su beffo, y el resto serán sus amigos.

'''
Argumento posicional y variable???
'''

def conversorGrados(gradosC):
    gradosF = (gradosC * 9/5) + 32
    return gradosF
#conversorGrados(26)

def nombres(nombre, bff, *amigos): #VARIABLE: Meter tantos valores
    print('''
    Hola {nombre}
    Tu mejor amigo es {bff}
    Tus amigos son: 
    ''')
    for amigo in amigos:
        print(amigo)
print(nombres('Ale', 'Perla', 'C', 'Y'))
        
