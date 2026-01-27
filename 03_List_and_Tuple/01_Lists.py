marks = [95.4, 94.4, 68.6, 88.9, 76.5]
print(marks)
print(type(marks))
print(len(marks))

print(marks[2]) #indexing
print(marks[1:4]) #slicing
print(marks[0:5:2]) #slicing with step
print(marks[-1]) #last element

marks[4] = 43.5 #updating value
marks.append(99.9) #adding value
print(marks)

marks.reverse() #reversing list
print(marks)

marks.sort() #sorting list
print(marks)


marks.sort(reverse=True) #sorting in descending order
print(marks)

student = ("Binod", 21, 5.8) #tuple
print(student)