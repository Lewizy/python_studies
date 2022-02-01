def whatsMyName(name,age):
    print("my name is "+name+"age is ", age)
    
whatsMyName("Bob",45)
whatsMyName("Josh",35)
whatsMyName("Kyle",13)  


def unlimitedParameters(*lenguages):
    print(lenguages)#('js', 'java', 'python')
    print(lenguages[2])#python

unlimitedParameters("js","java","python")

def keywordArgument(pet1,pet2,pet3):
    print("my fav pet is : "+pet2)

keywordArgument(pet2="tiger",pet1="monkey",pet3="eagle")

def arbitrary_keywordArguments(**sodas): #double asteriks 
    print(sodas["redCan"])#coke

arbitrary_keywordArguments(blackSoda="pepsi", redCan="coke", greenType="ginger" )   

def defaultParameter(year = 2020):
    print("current year is", year)

defaultParameter(2008)
defaultParameter(1501)
defaultParameter()

def multiplication(number):
    print(number*5)

multiplication(5)#25
multiplication(28)#140

def passStatement():
    pass

def factorial_recursive(n):
  if n == 1:#until n is equal to 1
    return 1
  return n * factorial_recursive(n - 1)
# n * factorial_recursive(4)
# n * factorial_recursive(3)
# n * factorial_recursive(2)
# n * factorial_recursive(1)
print(factorial_recursive(5)) #1203

def fact(n):
	if n > 1:
		result = n + fact(n - 1)
		print(result)
	else:
		result = 0
	return result

#print("\n\nRecursion Example Results")
fact(6)