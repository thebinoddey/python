tup = (1,4,9,16,25,36,49,64,81,100)
print(tup)

num = int(input("Enter a number: "))
i = 1
while i < (len(tup)):
    # print(tup.index(num))
    i +=1
print(tup.index(num)+1)

#2nd method
i = 1
while(i<len(tup)):
    if(tup[i]==num):
        print(i+1)
    i+=1