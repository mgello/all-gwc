import json
file = open("jsurvey.json", "r")
jsonData = file.read()
PyData = json.loads(jsonData)
file.close()
print(PyData)
