#Mutabilidad, tuplas no son mutables
lista = [1,2,3,4,['a','b','c','d'],'otro elemento']
lista [0]='A'
print(lista)

#Tupla no es mutable
tupla = [1,2,3,('A','B','C')]
tupla[3]='D'

password=('asdfg','hjkl',12341234)

password=list(password)
print(type(password))
#password[0] = 'Holi'

password=tuple(password)
print(type(password))
print(password)