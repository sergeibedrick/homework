immutable_var = (1, 2, 3, [4, 5, 'a', 'b', 'c'], {7, 6})
print(immutable_var)

#immutable_var[2] = 9
#print(immutable_var)
# кортеж не изменяемый объект поэтому выдается ошибка(TypeError: 'tuple'
# object does not support item assignment)

mutable_list = [1, 2, 3, [4, 5, 'a', 'b', 'c'], {7, 6}]
print(mutable_list)
mutable_list[3][4] = 'Modified'
print(mutable_list)


