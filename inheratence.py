
class Person:
	def __init__(self,fname,lname):
	 self.firstname = fname
	 self.lastname = lname		

	def printname(self):
	 print(self.firstname,self.lastname)

x = Person("firtsname", "lastname")

class Child(Person):
	pass
x = Child("Mikey","Kong")
x.printname()

class Child2(Person):
	pass
x = Child2("Hailey","Kong")
x.printname()

class child3(Person):
	pass
x = child3("Bobby","Newport")
x.printname()

#///////////////////////////////////////////////////////////////////////////////

class Dad:
	def __init__(self,hair,eyes):
		self.hair = hair
		self.eyes = eyes
	def namePrint(self):#notice the indentation
		print(self.hair, self.eyes)

class Son(Dad):
	def __init__(self,hair,eyes):
		Dad.__init__(self,hair,eyes)#no spaces after .
	
y55 = Son("Charlie","Sheen")  
y55.namePrint()




