#Alejandra Escallada

series ={
    'Disney Plus':[
        {
            'The Mandalorian':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':'8',
                        'direccion':'El Cheems',
                        'calificacion':9.2,
                        'vistas':'32000000',
                        'tags':('star wars','filoniverse','dark saber')
                    },
                    'Temporada 2':{
                        'episodios':8,
                        'direccion':'Enrique Segoviano',
                        'calificacion':9.5,
                        'vistas':40000000,
                        'tags':('baby yoda','coursant','beskar')
                    }
                }
            }
        },
        {
            'The Bad Batch':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':'16',
                        'direccion':'El Canaca',
                        'calificacion':8.9,
                        'vistas':30000000,
                        'tags':('violencia animada','relleno')
                    },
                    'Temporada 2':{
                        'episodios':16,
                        'direccion':'El Canaca',
                        'calificacion':8.0,
                        'vistas':15000000,
                        'tags':('relleno','piu piu')
                    } 
                }
            }
        }
    ],
    'Netflix':[
        {
            'Dark':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':10,
                        'direccion':'Donald Trump',
                        'calificacion':9.5,
                        'vistas':20000000,
                        'tags':('such confusion','much time travel','wow')
                    },
                    'Temporada 2':{
                        'episodios':'8.0',
                        'direccion':'Donald Trump',
                        'calificacion':9.6,
                        'vistas':25500000,
                        'tags':('canciones ochenteras','spoiler')
                    },
                    'Temporada 3':{
                        'episodios':8,
                        'direccion':'Donald Trump',
                        'calificacion':9.7,
                        'vistas':'34000000',
                        'tags':('somos los malos?','best ending ever')
                    }
                }
            }
        },
        {
            '1899':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':8,
                        'direccion':'El Cheems',
                        'calificacion':9.5,
                        'vistas':40000000,
                        'tags':('cancelacion','misterio','barquitos')
                    }
                }
            }
        },
        {
            'Squid Game':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':9,
                        'direccion':'Calamardo Tentaculos',
                        'calificacion':9.5,
                        'vistas':60000000,
                        'tags':('violencia','jpop','cachetadas')
                    }
                }
            }
        }
    ],
    'HBO':[
        {
            'House of the Dragon':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':'10',
                        'direccion':'Viserys Targaryen',
                        'calificacion':9.5,
                        'vistas':40000000,
                        'tags':('acero valirio','dragones','reds vs greens')
                    }
                }
            }
        },
        {
            'The Last of Us':{
                'temporadas':{
                    'Temporada 1':{
                        'episodios':9,
                        'direccion':'Crash Bandicoot',
                        'calificacion':9.8,
                        'vistas':45000000,
                        'tags':('pan bimbo','hongos malos','terror')
                    }
                }
            }
        }
    ]
}

#Instrucciones
#Nota: Calculen promedios sin usar ciclos for, hagan las actividades en orden

#1) Obtener el promedio de vistas de todas las temporadas de la serie Dark
print(f"\n1) Promedio de vistas de todas las temporadas de Dark; {(series['Netflix'][0]['Dark']['temporadas']['Temporada 1']['vistas'])+(series['Netflix'][0]['Dark']['temporadas']['Temporada 2']['vistas'])+(int(series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['vistas']))}")

#2) Obtener el promedio de calificacion de todas las temporadas de la serie The Mandalorian
suma = series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 1']['calificacion'] + series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 2']['calificacion']
print(f"2) Promedio de calificacion de la serie The Mandalorian: {(suma/len(series['Disney Plus'][0]['The Mandalorian']['temporadas']))}")

#3) Obtener el primer tag de la temporada 1 de The Last of Us
print(f"3) Primer tag de la temporada 1 de The Last of Us: {series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags'][0]}")

#4) Obtener el numero de series emitidas por Disney Plus
print(f"4) Número de series emitidas en Disney Plus: {len(series['Disney Plus'])}")

#5) Obtener nombre del director de la primera temporada de The Mandalorian
print(f"5) Director de la temporada 1 de The Mandalorian: {series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 1']['direccion']}")

#6) Obtener el numero de series emitidas por Netflix
print(f"6) Numero de series de Netflix: {len(series['Netflix'])}")

#7) Obtener el tercer tag de la temporada 1 de Squid Game
print(f"7) Tercer tag de Squid Game: {series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['tags'][2]}")

#8) Obtener nombre del director de la primera temporada de Squid Game
print(f"8) Director de la temporada 1 de Squid Game: {series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['direccion']}")

#9) Obtener nombre del director de la segunda temporada de The Mandalorian
print(f"9) Director de la temporada 2 de The Mandalorian: {series['Disney Plus'][0]['The Mandalorian']['temporadas']['Temporada 2']['direccion']}")

#10) Cambiar el segundo tag de la temporada 1 de The Last of Us por "hongos buenos"
print(type(series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags'][1]))
tag2 = list(series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags'][1])
tag2 = 'Hongos buenos'
print(f"10) Segundo tag: {series['HBO'][1]['The Last of Us']['temporadas']['Temporada 1']['tags']}")

#11) Cambiar el segundo tag de la temporada 1 de Squid Game por "kpop"
tag2 = list(series['Netflix'][2]['Squid Game']['temporadas']['Temporada 1']['tags'][1])
tag2 = 'kpop'
print(f"11) Segundo tag de Squid Game: {tag2}")

#12) Cambiar la calificion de la tercr temporada de dark a 10
calif = series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['calificacion'] = 10
print(f"12) Calificación de la temporada 3 de The Dark: {calif}")

#13) Obtener el promedio de calificaciones de todas las temporadas de la serie Dark
prom = (series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['calificacion'] + series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['calificacion'] + series['Netflix'][0]['Dark']['temporadas']['Temporada 3']['calificacion']) / len(series['Netflix'][0]['Dark']['temporadas'])
print(f"13) Promedio de todas las temporadas de The Dark: {prom}")

#14) Via consola, pedir al usuario que escriba un tag con el que le gustaria calificar la primer temporada de House of the Dragon.
#Si el tag ya existe dentro de los tags, indicar al usuario que dicho tag ya existe e imprimir la estructura
#correspondiente. Si el tag no existe, preguntar al usuario si desearia agregar dicho tag a la estructura.
#Si el usuario selecciona "Si" agregar el tag, si selecciona "No" imprimir "ta bueno pues"
#Imprimir la estrucutra final
tag_usuario = input("\n14) Escriba el tag con el que calificaría la temporada 1 de The House of Dragons: ")
tags_dragon = series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags']
if tag_usuario in tags_dragon:
    print(f"El tag ingresado ya existe. Tags: {tags_dragon}")
else:
    newtag = input(f"El tag ingresado no se encuentra dentro de la lista. Te gustaría añadirlo? (si/no): ")
    if newtag == "si":
        tag = list(series['HBO'][0]['House of the Dragon']['temporadas']['Temporada 1']['tags'])
        tag.append(tag_usuario)
        print(tag)
    else:
        print("ta bueno pues")

#15 via consola, el usuario debe ingresar los campos que compondran la temporada 2 de the last of us.
#La consola debe pedir al usuario el numero de episodios, el nombre del director, la calificacion,
#las vistas y una tag. Aniadir estos datos a la estructura correspondiente. Al final, imprimir el diccionario completo
#El resultado debe verse mas  o menos asi:
#RECUERDEN COMO SE AGREGAN KEYS A UN DICCIONARIO GUINIO GUINIO

episodios = int(input("\n15) Ingrese el número de episodios: "))
director = input("Ingrese el nombre del director: ")
calif = float(input("Ingrese la calificación de la temporada: "))
vistas = int(input("Ingrese el número de vistas: "))
tag = input("Ingrese un tag de la serie: ")



'''
'The Last of Us':{
                'temporadas':{
                    'Temporada 1':{
                        **Estos datos ya estan comododados
                    },
                    'Temporada 2':{
                        **Aqui van los datos recolectados via consola
                    }
                }
'''

series['HBO'][1]['The Last of Us']['temporadas']['Temporada 2'] = {
    'episodios': episodios,
    'director': director,
    'calificacion': calif,
    'vistas':vistas,
    'tag': tag
    }

print(series['HBO'][1]['The Last of Us']['temporadas']['Temporada 2'])