import json

# convert json to python
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# convert python to json
python_dict = {"car": "ford", "color": "black", "year": 30}#type 'dict'
convert_to_json = json.dumps(python_dict) #type 'str'
print(convert_to_json)

# Convert Python objects into JSON strings
print(type(json.dumps(True)))
print(type(json.dumps(-31.25)))
print(type(json.dumps(False)))
print(type(json.dumps([26, 56, 533, -13.32])))

person_1 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use indent to read better
print(json.dumps(person_1, indent=1))

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(person_1, indent=1, separators=(".", "=")))