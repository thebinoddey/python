def print_length(list):
    return len(list)

def print_list(list):
    for i in list:
        print (i, end=' ')
    

my_list = [1, 2, 3, 4, 5]
print("Length of the list is:", print_length(my_list))
print("Elements of the list are: ") , print_list(my_list)
