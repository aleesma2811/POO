
videojuegos = {
    'Epic Games':[
        {
            'Gears of War 3':{
                'genero':'FPS',
                'anio':2011,
                'calificacion':9,
                'ventas mundiales':3000000,
                'tags':['disparos','gore','violencia bien intensa'],
                'equipo':{
                    'Lead Designer':'El Cheems',
                    'Art Director':'La Cholondrina'
                }
            }
        },
        {   
            'Gears Tactics':{
                'genero':'Strategy',
                'anio':2019,
                'calificacion':9,
                'ventas mundiales':'1500000',
                'tags':('gore estrategico','gore','violencia bien intensa'),
                'equipo':{
                    'Lead Designer':'El Cheems',
                    'Art Director':'La Cholondrina'
                }
            }
        },
        {
               'Fortnite':{
                'genero':'Battle Royale',
                'anio':2017,
                'calificacion':'9',
                'ventas mundiales':30000000,
                'tags':['niños rata','microtransacciones','disparos'],
                'equipo':{
                    'Lead Designer':'El Medio Metro',
                    'Art Director':'Alfredo Adame'
                }
            }
        }
    ],
    '343 Industries':[
        {
            'Halo Infinite':{
                'genero':'FPS',
                'anio':2020,
                'calificacion':9,
                'ventas mundiales':'4000000',
                'tags':('disparos','aliens','microtransacciones'),
                'equipo':{
                    'Lead Designer':'Maestr Cheef',
                    'Art Director':'Bob Ross'
                }
            }
        },
        {
            'Halo Wars 2':{
                'genero':'Strategy',
                'anio':2017,
                'calificacion':7,
                'ventas mundiales':100000,
                'tags':('estrategia','wololo','the banished'),
                'equipo':{
                    'Lead Designer':'Gerard Pique',
                    'Art Director':'Salgado Macedonio'
                }
            }
        }
    ],
    'Ubisoft':[
        {
            'Assassins Creed: Valhalla':{
                'genero':'RPG',
                'anio':2020,
                'calificacion':9,
                'ventas mundiales':2000000,
                'tags':('vikingos','canciones de vikingos','violencia de vikingos'),
                'equipo':{
                    'Lead Designer':'Beakman',
                    'Art Director':'Pingu el Pinguino'
                }
            }
        },
        {   
            'Avatar: Frontiers of Pandora':{
                'genero':'RPG',
                'anio':2022,
                'calificacion':0,
                'ventas mundiales':0,
                'tags':('magia naturistica','aventuras espaciales','violencia de pitufos'),
                'equipo':{
                    'Lead Designer':'James Hetfield',
                    'Art Director':'Rick Roll'
                }
            }
        }
    ],
    'CD Projekt Red':[
        {
            'Cybepunk 2077':{
                'genero':'RPG',
                'anio':2020,
                'calificacion':7,
                'ventas mundiales':3000000,
                'tags':('disparos','mucho neon bling bling','violencia del futuro'),
                'equipo':{
                    'Lead Designer':'Spoderman',
                    'Art Director':'Hasbulla'
                }
            }
        },
        {
            'Red Dead Redemption II':{
                'genero':'Adventure',
                'anio':2018,
                'calificacion':9,
                'ventas mundiales':46000000,
                'tags':('disparos','vaqueros','violencia con caballos'),
                'equipo':{
                    'Lead Designer':'Abdu Rozik',
                    'Art Director':'Mamberoy'
                }
            }
        },
        {
            'The Witcher III':{
                'genero':'RPG',
                'anio':2015,
                'calificacion':9,
                'ventas mundiales':40000000,
                'tags':('magia muy magica','violencia','fantasia'),
                'equipo':{
                    'Lead Designer':'Warren Buffet',
                    'Art Director':'El Escorpion Dorado'
                }
            }
        }
    ]
}

#INDICACIONES

#1) Obtener el promedio de calificaciones de juegos de Epic Games. Si el promedio es mayor o igual 
# a 8, imprimir "Que wen estudio ( ͡° ͜ʖ ͡°)"
prom = (videojuegos['Epic Games'][0]['Gears of War 3']['calificacion'] + videojuegos['Epic Games'][1]['Gears Tactics']['calificacion'] + int(videojuegos['Epic Games'][2]['Fortnite']['calificacion'])) / len(videojuegos['Epic Games'])
print(prom)
if (prom >= 8):
    print("Que wen estudio ( ͡° ͜ʖ ͡°)")
else:
    print("Este estudio apesta. Pésimo servicio")

#De lo contrario, imprimir "este estudio apesta"

#2) Obtener el nombre del Art Director de Assassins Creed: Valhalla
print(videojuegos['Ubisoft'][0]['Assassins Creed: Valhalla']['equipo']['Art Director'])
if (videojuegos['Ubisoft'][0]['Assassins Creed: Valhalla']['equipo']['Art Director'] == "Pingu el Pinguino"):
    print("Noot Noot")

#Si es Pingu el Pinguino, imprimir "Noot Noot"

#3) Obtener el numero de juegos de Epic Games y Ubisoft. Determinar quien tiene mas juegos usando IF
EG = int(len(videojuegos['Epic Games']))
Ubisoft = int(len(videojuegos['Ubisoft']))

if (EG >= Ubisoft):
    print("Epic Games tiene más juegos que Ubisoft")
else:
    print("Ubisoft tiene más juegos que Epic Games")


#4) Obtener el promedio de ventas y calificaciones de videojuegos de CD Projekt Red.
calif1 = videojuegos['CD Projekt Red'][0]['Cybepunk 2077']['calificacion']
calif2 = videojuegos['CD Projekt Red'][1]['Red Dead Redemption II']['calificacion']
calif3 = videojuegos['CD Projekt Red'][2]['The Witcher III']['calificacion']

venta1 = videojuegos['CD Projekt Red'][0]['Cybepunk 2077']['ventas mundiales']
venta2 = videojuegos['CD Projekt Red'][1]['Red Dead Redemption II']['ventas mundiales']
venta3 = videojuegos['CD Projekt Red'][2]['The Witcher III']['ventas mundiales']

promC = (calif1 + calif2 + calif3) / len(videojuegos['CD Projekt Red'])
promV = (venta1 + venta2 + venta3) / len(videojuegos['CD Projekt Red'])

if (promV > 20000) & (promC > 8):
    print("D Projekt Red es amor, CD Projekt Red es vida")
else:
    print(";___;")


#Si el promedio de ventas es mayor a 20000 y el promedio de calificaciones es mayor a 8, 
#imprimir "CD Projekt Red es amor, CD Projekt Red es vida", de lo contrario imprimir ";___;"

#5) Via consola, pedir al usuario que escriba un tag con el que le gustaria calificar a Fortnite.
#Si el tag ya existe dentro de los tags, indicar al usuario que dicho tag ya existe e imprimir la estructura
#correspondiente. Si el tag no existe, preguntar al usuario si desearia agregar dicho tag a la estructura.
#Si el usuario selecciona "Si" agregar el tag, si selecciona "No" imprimir "ta bueno pues"
#Imprimir la estrucutra final

tag_usuario = input(print("Ingrese cualquier tag de Fortnite: "))
tags_fortnite = videojuegos['Epic Games'][2]['Fortnite']['tags']

if tag_usuario in tags_fortnite:
    print(f"{tag_usuario} se encuentra dentro de los tags. ")
else:
    print(f"{tag_usuario} no se encuentra dentro de los tags. ¿Quieres añadirlo? ")