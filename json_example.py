import json
from xml.etree.ElementTree import indent

json_data = '{"name": "Дмитрий", "age": 100, "is_student": true}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))

data = {
    'name': "Dmitriy",
     'age': 100,
     'is_student': True
}

json_string = json.dumps(data, indent=2)
print(json_string, type(json_string))

with open('json_example.json', encoding='utf-8') as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)