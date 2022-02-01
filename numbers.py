int_x = 6
float_x = 2.8
complex_x = 1j

if type(complex_x) == complex:
 	print('its complex')

#convert from one type to another
if type(float_x) == float:
	float_x = complex(float_x)
	print(float_x)# 2.8+0j

thePowerOf30 = 10e30
print(thePowerOf30)

range_method = range(0,10,2)
for range_i in range_method:
		print(range_i,"increase by 2 up to 10")

range_method2 = range(0,6)
range_method3 = range(7)

import random
print(random.randrange(0,11),"<----  random")

print(int("54"))

