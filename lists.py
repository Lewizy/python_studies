#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

convertToList = ("Cat",False,0,25.6)
xConvertToList = list(convertToList)#['Cat', False, 0, 25.6]
print(convertToList[:2])#('Cat', False)
print(convertToList[2:])#(0, 25.6)

datatype = [True,'this is a list',2.8,2,33]
print(type(datatype),"<=====DataType")

if 33 in datatype:
	datatype.remove(33)
	print(datatype)

if "99" not in datatype:
	datatype.append("99")

insertMethod = datatype.insert(-1,"inserted")	#insert at the specified index

combine_lists = xConvertToList.extend(datatype)	

for i in range(len(datatype)):
		print(datatype[i],"<<<<<<<")

print(datatype) 

while_i = 0
while while_i < len(datatype):
	print(datatype[while_i])
	while_i += 1

[print(i) for i in xConvertToList]
print(datatype)

emtyl = []
strList = ["ask","bout","Me","A"]

for j in strList:
	if "b" in j:
		emtyl.append(j)

print(emtyl) #['bout']

manipulatedList = [i.upper() for i in strList]#['ASK', 'BOUT', 'ME']
set_all_values_to = ["inserted" for i in strList]#['inserted', 'inserted', 'inserted']

#return items that are specified
comprehensionList = [i for i in strList if "a" in i]
print(comprehensionList)#['ask'] 

#Only accept items that are NOT specified
combine_lists = [i for i in strList if i != "me"]
print(combine_lists)#['ask', 'bout']

createList_up_to_10 = [i for i in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range_with_condition = [i for i in range(10) if i < 5 ] #[0, 1, 2, 3, 4, 5]

#replace me for you
manipulate_with_conditions = [i if i != "me" else "you" for i in strList]
#['inserted', 'inserted', 'inserted']

createList_up_to_10.sort(reverse = True)#reversed sort

strList.sort(key = str.lower) #case_sensitve_sort 

print(createList_up_to_10)
print(strList)

print("/////////////////////////////////////////////////////////////////////////")


