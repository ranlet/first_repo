import csv
with open('first_repo/students.csv', encoding="utf8") as a:
    reader = list(csv.DictReader(a, delimiter=',', quotechar='"'))
    arr = list(reader)
    print(arr)
a = {}
for i in arr:
    f = i['class']
    if '10' in f:
        d = {i['id']:i['score']}
        print(d)
        a