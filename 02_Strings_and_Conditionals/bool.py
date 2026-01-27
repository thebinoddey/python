print(bool (0.000)) #False
print(bool (1)) #true
print(bool (15)) #true
print(bool (-5)) #true
print(bool ("")) #False
print(bool ("Hello")) #True
print(bool (None)) #False
print(bool ([])) #False
print(bool ("0")) #True

is_on = True
float(is_on) #1.0
str(is_on) #"True"
int(is_on) #1

## BOOL CONVERSION
#True: Non-zero numbers, Non-empty strings, Non-empty collections (lists, tuples, sets, dictionaries)
#False: Zero (0, 0.0), Empty strings (""), None, Empty collections ([], (), {}, set())