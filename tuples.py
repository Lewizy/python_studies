#tuple items are ordered, unchangeable, and allow duplicate values.

tupleNames = ("jhon","peter","luke",40,50,60,True)
print("tuplenames length:",len(tupleNames))#7

tupleConstructor = (("notice","the","double","round_brackets"))

ranged_tups = tupleNames[1:3]

if "peter" in tupleNames:
	print("peter is in")

#updating tuples 
converter = list(tupleNames)	
converter[0] = "Pissant"
tupleNames = tuple(converter)
print(converter,"<---- converter")

#adding values
converter2 = list(tupleNames)
converter2.append("appended")
tupleNames = tuple(converter2)

#removing values
converter3 = list(tupleNames)
converter3.remove(60)
tupleNames = tuple(converter3)
# del tupleNames

#unpacking tuples
#the * symbol assigns the rest of the list
(x1,x2,*x3) = tupleNames
print(x1,x2,x3) #Pissant peter ['luke', 40, 50, True, 'appended']
(x4,*x5,x6) = tupleNames
print(x4,x5,x6) #Pissant ['peter', 'luke', 40, 50, True] appended

#looping
for i in tupleNames:
	print(i)

for i in range(len(tupleNames)):
	print(tupleNames[i],": index:", i)

ij = 0
while ij < len(tupleNames):
	print(tupleNames[ij],": index:", ij)
	ij+=1

#joing tuples 
a1 = (1,2,3)
a2 =("a","b","c")
a3 = a1+a2
print(a3)

multiplyTuples = a2 * 2
print(multiplyTuples) # ('a', 'b', 'c', 'a', 'b', 'c')

return_the_number_of_times_value_appears = multiplyTuples.count("c") #2
