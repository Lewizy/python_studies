


########################################dictionaries###################################################
dict = {}
dict ["State"] = "Alabama"
dict ["Person"] = "Mat"
dict [2] = "Data updated"
dict ["Color"] = "Brown"
dict ["Religion"] = "Pizzianity"
dict [5] = "Number five"



dictionary = {}
dictionary ["hi"] = "salute"
print (dictionary)

dictionaries_person = {
    "name":"Ballerino",
    "nick name": "Jamaiquino",
    "age" : "33",
    "race":"Bomboclatian",
    "favoriteFood": "lemons",
    "favorite_tv_show": "the kardashians",
    "petOwned": "cat",
    "favorite tv line": "how bowt them grapples",
}

the_popItem_method = dictionaries_person.popitem()
addingValuesTo_dictionaries = dictionaries_person["hair color"] = "pink"
#adding values
the_pop_method = dictionaries_person.pop("petOwned")
#removing values

the_clear_method = dict.clear()

the_copy_method = dictionaries_person.copy() #copy dicts

the_popItem_method = dictionaries_person.popitem()
#removes last item, some versions only

del dictionaries_person["favoriteFood"] #removes specified
#del dictionaries_person  #deletes whole dicts

print_dict_keys = dictionaries_person["age"]
print(print_dict_keys)

updating_values_inDict = dictionaries_person["race"] = "celestial"
print(updating_values_inDict+"<--updated")

the_get_method = dictionaries_person.get("Hair color")
print(the_get_method)

for print_all_keys in dictionaries_person:
    print(print_all_keys)

for print_all_values in dictionaries_person:
        print(dictionaries_person[print_all_values])    

for use_values_method in dictionaries_person.values():
        print(use_values_method)

for keys_items , values_items in dictionaries_person.items(): 
        print(keys_items , values_items)
 
if "age" in dictionaries_person:
        print("age exist in dictionaries_person")

the_length_method = len(dictionaries_person)
print("The length is-->>>>>>>>" , the_length_method) 

print(the_copy_method)
