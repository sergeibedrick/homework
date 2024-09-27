# dictionary
my_dict ={
    'Anna' : 2020,
    'Boris' : 1989,
    'Alex' : 1999,
    'Bill' : 2011
}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('July'))
my_dict.update({'July' : 2001,'Jone' : 2002,})
print(my_dict)
a = my_dict.pop('Anna')
print(my_dict)
print(a)

# set
my_set = {1,2,3,4,1,2,3,4,(1,2,3,1,2,3),'string','string',
          12.6,12.6,False,False}
print(my_set)
my_set.add(5)
my_set.add('apple')
print(my_set)
my_set.remove('string')
print(my_set)
