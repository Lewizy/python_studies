




a = lambda a: a+5
print(a(255))
b = lambda a,b: a*b
print(b(4,6))
c = lambda a,b,c: a*b*c
print(c(56,25,31)) 

'''Use a function definition to make a function 
that always doubles the number you send in:'''
def lambdaFunc(n):
	return lambda a: a*n

doubler = lambdaFunc(2)
tripler = lambdaFunc(3)
quadrupler = lambdaFunc(4)
print(doubler(11))#22
print(tripler(11))#23
print(quadrupler(11))#44





