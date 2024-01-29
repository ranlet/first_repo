import csv
c = input()
with open('first_repo/students.csv', encoding="utf8") as a:
    reader = list(csv.DictReader(a, delimiter=',', quotechar='"'))
    arr = list(reader)
a = {}
flag = False
for i in arr:
    f = i['titleProject_id']
    if c == f:
        flag = True
        d = {i['id']:i['score']}
        name = i['Name']
        SecName = name.split()
        second_name = SecName[0]
        fir_name = SecName[1]
        first_name = fir_name[0] + '.'
        print("Проект №" + c + " делал: " + first_name + ' ' + second_name + " он(а) получил(а) оценку - " + i['score'])
if not flag:
    print('Ничего не найдено.')
