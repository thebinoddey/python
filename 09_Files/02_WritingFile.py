f = open('example.txt', 'w')
f.write('hello, world!')
# f.close() '''It is commented to run with statement'''

# example.txt me jo kuch bhi tha uski jagah ye text aa gya

# With Statement
with open('example.txt', 'w') as f:
    f.write("Hello world, I am here!")