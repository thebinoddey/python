# is -> exact location of object in memory
# == -> value 

a = 4
b = 4

print(a is b) #True
print(a == b) #True

# Jab bhi immutable object banaya jata h to uske liye ek hi bar memory allocate hoti ha.
# Yani 4 ek hi bar memory me jayega bas 2 variables usko point karenge


lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2) #True
print(lst1 is lst2) #False