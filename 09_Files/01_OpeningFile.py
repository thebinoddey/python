# Opening a File
f = open('example.txt', 'r')
# print(f) --> <_io.TextIOWrapper name='example.txt' mode='r' encoding='cp1252'>
text = f.read()
print(text)
f.close()

'''Arguments of open()
1. File name
2. File Mode
    a. r (Read) -> to read file
    b. w (Write)-> to write file/create if not exists
    c. x (Create)-> creates file
    d. a (Append) -> opens the file for appending only
    e. t (text) -> text handling
    f. b (binary) -> handle images, pdf, etc.

'''
