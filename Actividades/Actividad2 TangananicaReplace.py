'''
Con la canción “Tangananica Tanganana”
(https://www.letras.com/31-minutos/322150/)>
<Cambiar TODAS las instancias de tangananica por “los tacos de
chistorra” y todos los tanganana por “los tlacoyos bien
frios”>
<Mostrar en pantalla la letra modificada, así como el numero de
veces que los tacos de chistorra y los tlacoyos bien fríos
son mencionados>
'''
lyrics = '''
A mí me gusta el Tangananica
Y yo prefiero el tanganana
La mejor frase es tangananica
El mejor verso es tanganana

Tangananica nica nica nica
Tanganana

Todo lo explica, no explica na
Para alegrarme digo tangananica
Para reírme digo tanganana
Comí un rico tangananica

A mí me dieron tanganana
Tangananica nica nica nica
Tanganana
Me tienes pica pica, no pasa na
Cómo voy a perder mi palabra es tan buena
Tu palabra es tan mala, no hay nada qué hacer
Cómo vas a ganar si la mejor palabra es tanganana

Tú siempre dices tangananica
Tú siempre gritas tanganana
Ya no soporto el tangananica
Y yo detesto tu tanganana

Tangananica nica nica nica
Tanganana
Nuestra mamá nos va a retar
Oye, oye, ordenemos mejor o si no nos van a pillar
'''

lyrics_rep = lyrics.replace('tangananica','los tacos de chistorra').replace('tanganana','los tlacoyos bien fríos')
print(lyrics_rep)

chistorra = lyrics_rep.count('los tacos de chistorra')
tlacoyos = lyrics_rep.count('los tlacoyos bien fríos')

print(f'''"Los tacos de chistorra" aparece {chistorra} veces en el texto modificado
"Los tlacoyos bien fríos" aparece {tlacoyos} veces en el texto modificado
''')