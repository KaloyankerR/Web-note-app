# import json

# with open('data_file.json', 'r') as f:
#      data = json.load(f)

# print(data)
# del data['test']
# print(data)

# with open('data_file.json', 'w') as f:
#         json.dump(data, f)

import json


with open('static/archieve/date_da.json', 'w+') as f:
    f.write("{}")
    data = json.load(f)
    print(data)
    f.close()

# with open('static/archieve/date_da.json', 'r') as f:
#     data = json.load(f)
#     print(data)