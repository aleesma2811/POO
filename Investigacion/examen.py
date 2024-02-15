musica = {
    'The Black Keys':{
        'El Camino':{
            'Lonely Boy':{
                'liked':False,
                'reproducciones':'397810130',
                'duracion_ms':187800,
                'tags':('Rock','Catchy Tunes')
            },
            'Little Black Submarines':{
                'liked':True,
                'reproducciones':'89206240',
                'duracion_ms':246600,
                'tags':('Rock & Roll','Classics','Blues','Ballad',
                        'Rock','Ballad','Blues','Classics','Classics',
                        'Ballad','Rock & Roll','Classics','Blues',
                        'Rock & Roll','Classics','Rock & Roll','Blues')
            },
            'Hell of a Season':{
                'liked':True,
                'reproducciones':10425570,
                'duracion_ms':207000,
                'tags':('Rock')
            }
        }
    },
    'Greta Van Fleet':{
        'From the Fires':{
            'Safari Song':{
                'liked':True,
                'reproducciones':104450524,
                'duracion_ms':'212400',
                'tags':('Rock','Classics')
            },
            'Edge of Darkness':{
                'liked':False,
                'reproducciones':'47756093',
                'duracion_ms':256800,
                'tags':('Rock')
            },
            'Highway Tune':{
                'liked':True,
                'reproducciones':'181238080',
                'duracion_ms':180000,
                'tags':('Hard Rock')
            },
            'Black Smoke Rising':{
                'liked':True,
                'reproducciones':119129373,
                'duracion_ms':251400,
                'tags':('Rock','Classics')
            }
        },
        'The Battle at Gardens Gate':{
            'Heat Above':{
                'liked':True,
                'reproducciones':67071430,
                'duracion_ms':324600,
                'tags':('Rock','Ballad')
            },
            'Age of Machine':{
                'liked':False,
                'reproducciones':'23667326',
                'duracion_ms':391800,
                'tags':('Rock')
            },
            'Stardust Chords':{
                'liked':False,
                'reproducciones':16001476,
                'duracion_ms':274200,
                'tags':('Ballad')
            },
        }
    },
    'Stromae':{
        'Racine Carree':{
            'Ta Fete':{
                'liked':False,
                'reproducciones':75156132,
                'duracion_ms':'153000',
                'tags':('French Pop','Electro')
            },
            'Tous le Memes':{
                'liked':True,
                'reproducciones':194588900,
                'duracion_ms':198000,
                'tags':('French Pop','Electro')
            },
            'Ave Cesaria':{
                'liked':True,
                'reproducciones':'50747834',
                'duracion_ms':245400,
                'tags':('French Pop','Electro','Ethnic')
            }
        },
        'Multitude':{
            'Invaincu':{
                'liked':True,
                'reproducciones':'16732216',
                'duracion_ms':123000,
                'tags':('French Pop','Electro')
            },
            'Sante':{
                'liked':True,
                'reproducciones':'92011201',
                'duracion_ms':'186600',
                'tags':('Ethnic')
            },
            'Fils de Joie':{
                'liked':False,
                'reproducciones':'34948659',
                'duracion_ms':189000,
                'tags':('French Pop')
            },
        }
    },
}

#INDICACIONES
#NOTA:
'''
El diccionario provisto sigue la siguiente estructura
'Artista':{
        'Disco':{
            'Cancion':{
                'Si la Cancion nos gusta o no':False,
                'Cuantas reproducciones tiene':'397810130',
                'Cuanto Dura en milisegundos':187800,
                'Tags asociados':('Rock','Catchy Tunes')
            },
        }
    } 
'''
#1--- Imprimir el numero de reproducciones de la cancion "Highway Tune"
print(f"1) {musica['Greta Van Fleet']['From the Fires']['Highway Tune']['reproducciones']}")

#2--- Imprimir el numero de reproducciones de la cancion "Heat Above"
print(f"2) {musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['reproducciones']}")

#3--- Imprimir la duracion de la cancion "Sante"
print(f"3) {musica['Stromae']['Multitude']['Sante']['duracion_ms']}")

#4--- Imprimir el segundo tag de la cancion "Lonely Boy"
print(f"4) {musica['The Black Keys']['El Camino']['Lonely Boy']['tags'][1]} ")

#5--- Imprimir la duracion de la cancion "Little Black Submarines"
print(f"5) {musica['The Black Keys']['El Camino']['Little Black Submarines']['duracion_ms']}")

#6--- Obtener la duracion total del disco "Multitude"
print(f"6) {musica['Stromae']['Multitude']['Invaincu']['duracion_ms'] + int(musica['Stromae']['Multitude']['Sante']['duracion_ms']) + musica['Stromae']['Multitude']['Fils de Joie']['duracion_ms']}")

#7--- Obtener el promedio de reproducciones del disco "The Battle at Gardens Gate"
prom = musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['reproducciones'] + int(musica['Greta Van Fleet']['The Battle at Gardens Gate']['Age of Machine']['reproducciones']) + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Stardust Chords']['reproducciones']
print(f"7) {prom/len(musica['Greta Van Fleet']['The Battle at Gardens Gate'])}")

#8--- Obtener el numero de discos de The Black Keys y de Greta Van Fleet. Determinar quien tiene mas discos
TheBlackKeys = len(musica['The Black Keys'])
fleet = len(musica['Greta Van Fleet'])
print(f"8) Número de discos de The Black Keys: {TheBlackKeys}")
print(f"Número de discos de Greta Van Fleet: {fleet}")

if (TheBlackKeys > fleet):
    print("The Black Keys tiene más discos que Greta Van Fleet.")
else:
    print("Greta Van Fleet tiene más discos que The Black Keys")

#9--- Sustituir los tags de la cancion 'Little Black Submarines' por una tupla que contenga 
#     los valores unicos de la estructura original. Es decir, eliminar duplicados
tags = set(musica['The Black Keys']['El Camino']['Little Black Submarines']['tags'])
tags = tuple(tags)
print(f"9) {tags}")

#10--- Obtener la duracion promedio de las canciones del disco "Racine Carree"
duracion = int(musica['Stromae']['Racine Carree']['Ta Fete']['duracion_ms']) + musica['Stromae']['Racine Carree']['Tous le Memes']['duracion_ms'] + musica['Stromae']['Racine Carree']['Ave Cesaria']['duracion_ms']
print(f"10) {duracion/len(musica['Stromae']['Racine Carree'])}")

#11--- Imprimir el nombre del disco con mas Likes de Greta Van Fleet
fires = int(True)
garden = int(True)
fires = musica['Greta Van Fleet']['From the Fires']['Safari Song']['liked'] + musica['Greta Van Fleet']['From the Fires']['Edge of Darkness']['liked'] + musica['Greta Van Fleet']['From the Fires']['Highway Tune']['liked'] + musica['Greta Van Fleet']['From the Fires']['Black Smoke Rising']['liked']
garden = musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['liked'] + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Age of Machine']['liked'] + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Stardust Chords']['liked']

if (fires > garden):
    print(f"11) Disco de Greta Van Fleet con más likes: From the Fires con {fires} likes")
else:
    print(f"11) Disco de Greta Van Fleet con más likes: The Battle at Gardens Gate con {garden}")

#12--- Aniadir el tag "Cumbia" a la cancion "Sante"
tagCumbia = list(musica['Stromae']['Multitude']['Sante']['tags'])
tagCumbia.append("Cumbia")
tagCumbia = tuple(tagCumbia)
print(f"12) {tagCumbia}")

#13--- Agregar la cancion "Tiene Espinas el Rosal" al disco "El Camino". La informacion de dicha cancion es la siguiente:
'''
'liked':True,
'reproducciones':'92011201',
'duracion_ms':'186600',
'tags':('Cumbion bien loco', 'Lo mejor para tus bodas')
'''
musica['The Black Keys']['El Camino']['Tiene espinas el Rosal'] = {
    'liked':True,
    'reproducciones':'92011201', 
    'duracion_ms':'186600',
    'tags':('Cumbion bien loco', 'Lo mejor para tus bodas')
}
print(f"13) {musica['The Black Keys']['El Camino']['Tiene espinas el Rosal']}")

#14--- Determinar cual es el disco con mas likes de todos

#Castear likes de bool a int
liked_camino = int(True)
liked_fires = int(True)
liked_gardens = int(True)
liked_racine = int(True)
liked_multitude = int(True)

#Sumar los likes de cada disco
liked_camino = musica['The Black Keys']['El Camino']['Lonely Boy']['liked'] + musica['The Black Keys']['El Camino']['Little Black Submarines']['liked'] + musica['The Black Keys']['El Camino']['Hell of a Season']['liked']
liked_fires = musica['Greta Van Fleet']['From the Fires']['Safari Song']['liked'] + musica['Greta Van Fleet']['From the Fires']['Edge of Darkness']['liked'] + musica['Greta Van Fleet']['From the Fires']['Highway Tune']['liked'] + musica['Greta Van Fleet']['From the Fires']['Black Smoke Rising']['liked']
liked_gardens = musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['liked'] + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Age of Machine']['liked'] + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Stardust Chords']['liked']
liked_racine = musica['Stromae']['Racine Carree']['Ta Fete']['liked'] + musica['Stromae']['Racine Carree']['Tous le Memes']['liked'] + musica['Stromae']['Racine Carree']['Ave Cesaria']['liked'] 
liked_multitude = musica['Stromae']['Multitude']['Invaincu']['liked'] + musica['Stromae']['Multitude']['Sante']['liked'] + musica['Stromae']['Multitude']['Fils de Joie']['liked']

#Listas de discos y sus likes, discos coinciden con sus likes en el índice 
list_discos = ['El Camino','From the Fires','The Battle at Gardens','Racine Carree','Multitude']
list_likes = [liked_camino, liked_fires, liked_gardens, liked_racine, liked_multitude]

#Indice de los likes mayores
indice = list_likes.index(max(list_likes))

#Indice de los likes mayores en la lista de los discos 
print(f"14) Disco con más likes: {list_discos[indice]} con {max(list_likes)} likes")


#15--- Determinar cual es el disco con mayor duracion de todos

#Acceder a las duraciones y agregarlas a la lista 
duracion_camino = musica['The Black Keys']['El Camino']['Lonely Boy']['duracion_ms'] + musica['The Black Keys']['El Camino']['Little Black Submarines']['duracion_ms'] + musica['The Black Keys']['El Camino']['Hell of a Season']['duracion_ms']
duracion_fires = int(musica['Greta Van Fleet']['From the Fires']['Safari Song']['duracion_ms']) + musica['Greta Van Fleet']['From the Fires']['Edge of Darkness']['duracion_ms'] + musica['Greta Van Fleet']['From the Fires']['Highway Tune']['duracion_ms'] + musica['Greta Van Fleet']['From the Fires']['Black Smoke Rising']['duracion_ms']
duracion_gardens = musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['duracion_ms'] + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Age of Machine']['duracion_ms'] + musica['Greta Van Fleet']['The Battle at Gardens Gate']['Stardust Chords']['duracion_ms']
duracion_racine = int(musica['Stromae']['Racine Carree']['Ta Fete']['duracion_ms']) + musica['Stromae']['Racine Carree']['Tous le Memes']['duracion_ms'] + musica['Stromae']['Racine Carree']['Ave Cesaria']['duracion_ms']
duracion_multitude = musica['Stromae']['Multitude']['Invaincu']['duracion_ms'] + int(musica['Stromae']['Multitude']['Sante']['duracion_ms']) + musica['Stromae']['Multitude']['Fils de Joie']['duracion_ms']

list_discos = ['El Camino','From the Fires','The Battle at Gardens','Racine Carree','Multitude']
list_duracion = [duracion_camino, duracion_fires, duracion_gardens, duracion_racine, duracion_multitude]

indice = list_duracion.index(max(list_duracion))
print(f"15) Disco con mayor duración {list_discos[indice]} con duración de {max(list_duracion)}")

#16--- Via consola, mostrar al usuario el nombre de los discos de  Greta Van Fleet. Pedirle al usuario que seleccione uno
#      una vez seleccionado, mostrar las canciones que lo componen. Pedir al usuario que seleccione una.
#      una vez seleccionada, preguntarle al usuario si le gustaria agregar un tag a la cancion. Si dice que si, determinar si el 
#      tag ya estaba presente en los tags. Si no estaba, agregarlo. Si ya estaba, imprimir "Hijole joven, no se va a poder"
#      imprimir la estructura resultante

#Acceder a Greta Van Fleet
gvf = musica['Greta Van Fleet'].keys()

#Acceder a las canciones de cada disco
canciones_fires = musica['Greta Van Fleet']['From the Fires'].keys()
canciones_gardens = musica['Greta Van Fleet']['The Battle at Gardens Gate'].keys()

#Acceder a los tags de las canciones
tags_safari = list(musica['Greta Van Fleet']['From the Fires']['Safari Song']['tags'])
tags_darkeness = list(musica['Greta Van Fleet']['From the Fires']['Edge of Darkness']['tags'])
tags_highway  = list(musica['Greta Van Fleet']['From the Fires']['Highway Tune']['tags'])
tags_smoke = list(musica['Greta Van Fleet']['From the Fires']['Black Smoke Rising']['tags'])
tags_heat = list(musica['Greta Van Fleet']['The Battle at Gardens Gate']['Heat Above']['tags'])
tags_age = list(musica['Greta Van Fleet']['The Battle at Gardens Gate']['Age of Machine']['tags'])
tags_stardust = list(musica['Greta Van Fleet']['The Battle at Gardens Gate']['Stardust Chords']['tags'])

print(f"\n16) DISCOS DE GRETA VAN FLEET {gvf}")
disc_usuario = input("-Ingrese el disco de su elección: ") 

#Si el usuario escoge disco From the Fires
if(disc_usuario == 'From the Fires'):
    print(f"CANCIONES DE FROM DE FIRES: {canciones_fires}")
    cancion_usuario = input("-Escoja una canción: ")
    #Si el usuario escoge canción Safari Song 
    if(cancion_usuario == 'Safari Song'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        #Tag del usuario se encuentra en la lista
        if(tag_usuario in tags_safari):
            print("Nambre, no se va a poder")
            print(tags_safari)
        #Tag del usuario no se encuentra y se agrega a la lista
        else:
            tags_safari.append(tag_usuario)
            print(tags_safari)
    #Usuario escoge canción
    elif(cancion_usuario == 'Edge of Darkness'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        #Tag del usuario se encuentra en la lista
        if(tag_usuario in tags_darkeness):
            print("Nambre, no se va a poder")
            print(tags_darkeness)
        #Tag del usuario no se encuentra y se agrega a la lista
        else:
            tags_darkeness.append(tag_usuario)
            print(tags_darkeness)
    elif(cancion_usuario == 'Highway Tune'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        if(tag_usuario in tags_highway):
            print("Nambre, no se va a poder")
            print(tags_highway)
        else:
            tags_highway.append(tag_usuario)
            print(tags_highway)
    elif(cancion_usuario == 'Black Smoke Rising'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        if(tag_usuario in tags_smoke):
            print("Nambre, no se va a poder")
            print(tags_smoke)
        else:
            tags_smoke.append(tag_usuario)
            print(tags_smoke)
    #Canción ingresada no se encuentra
    else:
        print("Canción inválida")

#Si el usuario escoge disco The Battle at Gardens Gate
elif(disc_usuario == "The Battle at Gardens Gate"):
    print(f"CANCIONES DE THE BATTLE AT GARDENS DATE: {canciones_gardens}")
    cancion_usuario = input("Escoja una canción: ")
    if(cancion_usuario == 'Heat Above'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        if(tag_usuario in tags_heat):
            print("Nambre, no se va a poder")
            print(tags_heat)
        else:
            tags_heat.append(tag_usuario)
            print(tags_heat)
    elif(cancion_usuario == 'Age of Machine'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        if(tag_usuario in tags_age):
            print("Nambre, no se va a poder")
            print(tags_age)
        else:
            tags_age.append(tag_usuario)
            print(tags_age)
    elif(cancion_usuario == 'Stardust Chords'):
        tag_usuario = input("-Ingrese un tag de la cancion: ")
        if(tag_usuario in tags_stardust):
            print("Nambre, no se va a poder")
            print(tags_stardust)
        else:
            tags_stardust.append(tag_usuario)
            print(tags_stardust)
    else:
        print("Canción inválida")

else:
    print("Neta?")


#EXTRA --- Estos no son a fuerza, pero si quieren un desafio y puntos extra valdria la pena intentarlo
#A--- Obtener el promedio de reproducciones del disco "The Battle at Gardens Gate" usando Ciclos For
#B--- Obtener la duracion total del disco "Multitude" usando Ciclos For
#C--- Crear e imprimir una lista con los nombres de los Discos de Stromae usando List Comprehension

disc_stromae = musica['Stromae'].keys()
newlist = [disco for disco in disc_stromae]
print(f"c) {newlist}")