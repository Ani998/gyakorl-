# converting to integer
'''float_number = 7.456
integer_number = int(float_number)
print(type(float_number))
print(integer_number)
print(type(integer_number))'''

#convert to string
'''stringn = '555'
print(type(stringn))
float_to_str = int(stringn)
print(float_to_str)
print(type(float_to_str))'''

#convert string to float
'''string2 = '555'
string_to_float = float(string2)
print(f'Típus: {type(string_to_float)}')
print(string_to_float)'''

# int és float to str
'''a = 80
b = 67.678

print(type(a))
print(type(b))
print(type(str(a)))
print(type(str(b)))
print(str(a))
print(str(b))'''


numbers = [43, 23, 2, 5, 645]
numbers.sort()
print(numbers[1:3])

a = 3
b = 3

if a != b:
    print("not equal")
elif a == b:
    print("It is equal")
else:
    print("We don't know")

numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers[::2]:
    print(num, end='-')
