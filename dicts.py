

########################################dictionaries###################################################
dict = {}
dict ["State"] = "Alabama"
dict ["Person"] = "Mat"
dict [2] = "Data updated"
dict ["Color"] = "Brown"
dict ["Religion"] = "Pizzianity"
dict [5] = "Number five"

print dict
print dict.keys()
print dict.values()

dictionary = {}
dictionary ["hi"] = "salute"
print (dictionary)

dictionaries_alternative = {
	"name": "Jamaiquino",
	"age" : "33",
	"race":"Bomboclatian",
}

addingValuesTo_dictionaries = dictionaries_alternative["Hair color"] = "pink"
print(dictionaries_alternative)

the_pop_method = dictionaries_alternative.pop("name")

print_dict_keys = dictionaries_alternative["age"]
print(print_dict_keys)

updating_values_inDict = dictionaries_alternative["race"] = "Celestial"
print(updating_values_inDict+"<--updated")

the_get_method = dictionaries_alternative.get("Hair color")
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
print("The length is : --->>>", the_length_method)




