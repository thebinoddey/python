#readlines() method

f = open('example.txt', 'r')
while True:
    line = f.readline()
    if not line:
        # print(line, type(line))
        break
    print(line)
    
#writeline() method

f = open('writeline.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()


#seek() fn
with open('example.txt', 'r') as f:
    f.seek(10) #move to 10th byte in the file
    data = f.read(5) #read next 5 bytes
    print(data)
    
#tell() fn
