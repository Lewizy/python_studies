class myClass:
	classVar = 15

p1 = myClass()
print(p1.classVar)	

class car:
	def __init__(self,model,color,year):#always include self in param
		self.model = model
		self.color = color
		self.year = year

	def selfFunc(self):#parent class
		print("year: ",self.year)
		print("the model of car1 is: "+self.model)

car1 = car("Ferrari","red",1996)
car2 = car("Bugatti","grey",1998)
print(car2.model)
print(car1.year)
print("the first car model is: "+car1.model+", second is: "+car2.model)
car2.selfFunc()
car1.selfFunc()

class Person:
	def __init__(attributes,bodyType,height,skinColor):
		attributes.bodyType = bodyType
		attributes.height = height
		attributes.skinColor = skinColor

Mike = Person("Fat","5'9","brown")		
Mike.height = "change features"
del Mike.skinColor
print("What is Mikes body-type: " + Mike.bodyType )

Maria = Person("thin","6","green")
print(Maria.skinColor)