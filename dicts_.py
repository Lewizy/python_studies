 ########################################dictionaries###################################################

dictionary1 = {}
dictionary1["hi"] = "salute"
print(dictionary1)

my_nested_dictionary_favMovies = {
    "Dark Knight": {
        "favCharacter": "The joker",
        "favLine": "Wanna see this pencil dissapear",
    },
    "Transformers": {
        "favCharacter": "Optimus Prime",
    },
    "Rick & Morty": {
        "favCharacter": "Mr.poopy Butthole",
    },
}

the_dict_constructor = dict(person="James", gender="male", dob="02/03/1999")

dictionaries_person = {
    "name": "Ballerino",
    "nick name": "Jamaiquino",
    "age": "33",
    "race": "Bomboclatian",
    "favoriteFood": "lemons",
    "favorite_tv_show": "the kardashians",
    "petOwned": "cat",
    "favorite tv line": "how bowt them grapples",
}

the_clear_method = dictionary1.clear()


addingValuesTo_dictionaries = dictionaries_person["hair color"] = "pink"
#adding values

updating_values_inDict = dictionaries_person["race"] = "celestial"
#updated

the_pop_method = dictionaries_person.pop("petOwned")
#removing values

the_popItem_method = dictionaries_person.popitem()
#removes last item, some versions only

del dictionaries_person["favoriteFood"]  #removes specified
#del dictionaries_person  #deletes whole dicts

the_update_method = dictionaries_person.update({"address":"tree-a-dem"})

the_copy_method = dictionaries_person.copy()  #copy dicts
the_copy_method2 = dict(dictionaries_person)  #copy dicts 2

fromKeys_dict = ("key1","key2","key3")
fromkeys_value = 0
the_from_keys_method = dict.fromkeys(fromKeys_dict,fromkeys_value)
print(the_from_keys_method) # this method gives the same value to all keys

print_dict_keys = dictionaries_person["age"] #33

the_get_method = dictionaries_person.get("Hair color")# pink

for print_all_keys in dictionaries_person:
    print(print_all_keys+"<<<<<<<<<<<<")

for print_all_values in dictionaries_person:
    print(dictionaries_person[print_all_values])

for use_values_method in dictionaries_person.values():
    print(use_values_method)

for keys_items, values_items in dictionaries_person.items():
    print(keys_items, values_items)

if "age" in dictionaries_person:
    print("age exist in dictionaries_person")

the_length_method = len(dictionaries_person)
print("The length is-->>>>>>>><<<", the_length_method)

print(the_dict_constructor)



