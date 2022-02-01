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