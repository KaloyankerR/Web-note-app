import json

# with open("data_file.json", "w") as write_file:
#   json.dump(data, write_file)

with open("data_file.json", "r") as f:
    data = json.load(f)

print(data)
a = {'tosho': 'peshov'}
data.update(a)
print(data)
b = {'tisho': 'kokov'}
data.update(b)
print(data)
c = {'testosho': 'test'}
data.update(c)
print(data)

with open('data_file.json', 'w') as f:
    json.dump(data, f)