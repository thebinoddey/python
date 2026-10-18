lst = []
for x in range(10):
    lst.append(x**2)
    
# print(lst)


#List Comprehension
print([x**2 for x in range(10)]) #same as above

'''Syntax
1. Basic: [expression for item in iterable]
2. with conditional logics: [expression for item in iterable if condition]
3. Nested LC: [expression for item1 in iterable1 for item2 in iterable2]
'''

#Basic LC
print([num+2 for num in range(10)])

#Condition LC
print([num for num in range(10) if num%2==0])

#Nested LC
lst1 = [1,2,3]
lst2 = ['a', 'b', 'c']
pair = [[i,j] for i in lst1 for j in lst2]
print(pair)