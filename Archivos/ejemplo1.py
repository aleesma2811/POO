#mascotas = ['lia','rocky', 'tacho','cuca','balu','max','nala']
mascotas = [1,2,3,4,5]
#mascotas = ['Lia']
with open('mascotas.txt','a') as file:
    for mascota in mascotas:
        file.write(f"{mascota} \n")