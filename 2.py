
num10 = 10
stringNum = "5"

print int(stringNum) * num10 
#does not work in python3 output: 50
print float(stringNum) * num10
#does not work in python3

str = "December"
print str[0]
print str[0:5]
print str[4]

arraysAreCalledList = ["Letter_a","Theon",5566,False,"Shampow",633]

print(arraysAreCalledList)
print arraysAreCalledList[1:3]
print arraysAreCalledList[2:5]
arraysAreCalledList[1] = "TreeOn"; #lists can be updated, tuples cannot
print(arraysAreCalledList)

myTuple_readOnly_list = ("someVal",56,45,23,"pizza")# tuples cannot be scoped/updated read only
print myTuple_readOnly_list[3]


########################################dictionaries###################################################
dict = {}
dict ["Alabama"] = "State"
dict ["Person"] = "Mat"
dict [2] = "Data updated"
dict ["Color"] = "Brown"
dict ["Religion"] = "Pizzianity"
dict [5] = 5

print dict
print dict.keys()
print dict.values()

dictionary = {}
dictionary ["hi"] = "salute"
print (dictionary)

dictionaries_alternative = {
	"name": "Kamaro",
	"age" : "33",
	"race":"Bomboclatian"
}

dictionaries_alternative["56"] = "Genders"
print(dictionaries_alternative)
print(dictionaries_alternative["age"])

dict_keys_race = dictionaries_alternative["race"]
print(dict_keys_race)

scoping_var = dictionaries_alternative["race"] = "Celestial"
print(scoping_var+"<--scoping_var")

the_get_method = dictionaries_alternative.get("race")
print(the_get_method)

for print_all_keys in dictionaries_alternative:
    print(print_all_keys)

for print_all_values in dictionaries_alternative:
		print(dictionaries_alternative[print_all_values])	

for value_x in dictionaries_alternative.values():
		print(value_x)

for keys_items , values_items in dictionaries_alternative.items(): 
		print(keys_items , values_items)
 
if "age" in dictionaries_alternative:
		print("age exist in dictionaries_alternative")

the_length_method = len(dictionaries_alternative)
print(the_length_method)

