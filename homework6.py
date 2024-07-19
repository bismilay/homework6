my_dict = {'Ben':2004, 'Nastya': 1912 , 'Bull': 1965}
print(my_dict)
print('Existing value:', my_dict.get('Nastya'))
print('No existing value:' , my_dict.get('Valera'))
my_dict.update({'Alex': 1855,
'Malik': 2000})
print(my_dict)
a=my_dict.pop('Alex')
print( my_dict)
print('Deleted key: Alex')
print('Deleted value:', a)
print(my_dict)
print()
my_set= {1, 2, 3, 3, 2, 1, 'banana', 'pen','apple', 'pen','watermelon'}
print(my_set)
print(my_set.add('gun'))
print(my_set.add('Band'))
print(my_set.discard('pen'))
print(my_set.discard('banana'))
print(my_set)


