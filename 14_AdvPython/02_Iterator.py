# Iterators are advanced python concepts that allow for efficient looping & memory management. It doesn't directly expose underlying structure. It uses lazy loading.

my_lst = [1,2,3,4]

iterator = iter(my_lst)
print(type(iterator)) #<class 'list_iterator'>

print(iterator) #<list_iterator object at 0x000002181E98AE00>

#Iterate through all elements
print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #4
print(next(iterator)) #StopIteration Error

