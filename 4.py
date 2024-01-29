import csv
with open('first_repo/students.csv', encoding="utf8") as a:
    reader = list(csv.DictReader(a, delimiter=',', quotechar='"'))
    arr = list(reader)
a = {}
print ('id,Name,titleProject_id,class,score')
for i in arr:
    print(i['id'] + " " + i['Name'] + ' ' + i['titleProject_id'] + " " + i['class'] + " " + i['score'])
