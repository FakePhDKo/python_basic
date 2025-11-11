import json

file = 'seoul.json'
fd = open(file, "r", encoding="utf-8")
data = json.load(fd)
fd.close()

print(data)
data["population"] = 9600000
print(data)

file2 = 'busan.json'
fd = open(file2, "w")
data["city"] = "Busan"
data["population"] = 3249975
json.dump(data, fd, indent=2, ensure_ascii=False)

fd.close()
