immutable_var=(1, 'three',4.0, [1,2,3,4], True)
print(immutable_var)
#immutable_var[0]=2
#TypeError: 'tuple' object does not support item assignment
# Нельзя изменить значения элементов кортежа после его создания, так как его главное свойство - неизменяемостьmu

mutable_list=[1, 'tree', 4.0, [1,2,3,4], False]
print(mutable_list)
mutable_list[0]='one'
mutable_list[1]=2
print(mutable_list)
