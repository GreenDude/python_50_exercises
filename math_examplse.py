import math

num_1 = 2.4
num_2 = 2.7
num_3 = -3.4

print(math.floor(num_1))
print(math.ceil(num_2))

print(math.ceil(num_3))
print(math.floor(num_3))

print(math.trunc(num_1))
print(math.trunc(num_3))

num_4 = -1.2

print(f"Floor subtracts the value to a whole number: {num_4} - 0.8 = {math.floor(num_4)}")
print(f"Floor adds the value to a whole number: {num_4} + 0.8 = {math.ceil(num_4)}")

mantissa = math.frexp(4)
print(f"Mantissa: {mantissa}")