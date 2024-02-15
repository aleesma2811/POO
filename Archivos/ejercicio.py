import datetime
mascotas = ['lia','rocky', 'tacho','cuca','balu','max','nala']

with open('logueomascota.txt','w') as file:
    for mascota in mascotas:
        fecha = datetime.datetime.now()
        file.write(f"{mascota} se dio de alta a las {fecha} \n")
