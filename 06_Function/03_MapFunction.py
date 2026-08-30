

# map(function, iterable)
numbers = [1, 2, 3, 4, 5]
def square(nums):
    return nums ** 2

#-----------------------------------------

#map with function
map(square, numbers) #takes each num in number and applies the function
result = list(map(square, numbers))
print(result)

#-----------------------------------------

#map with lambda function
map(lambda x: x * 2, numbers) #takes each num in number and applies the function
result1 = list(map(lambda x: x ** 2, numbers))
print(result1) # [1, 4, 9, 16, 25]

#-----------------------------------------

#map with multiple iterators
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
''' desired output is result = [5, 7, 9] -> 1+4, 2+5, 3+6 '''
result = list(map(lambda x, y: x + y, nums1, nums2))
print(result) # [5, 7, 9]

#------------------------------------------

#Q1.
words = ['hello', 'world', 'python', 'programming']
upper_word = list(map(str.upper, words))
length = list(map(len, words))
