import csv
import random
from random import choice
def generator():
    c = '0123456789'
    b = 'qwertyuiopasdfghjklzxcvbnm'
    d = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    v = c + b + d
    pas = ''
    dig_flag = False
    flag1 = False
    flag2 = False
    for i in range(8):
        m = random.choice(v)
        if m in c:
            dig_flag = True
        elif m in b:
            flag1 = True
        elif m in d:
            flag2 = True
        pas+=m
    if dig_flag and flag1 and flag2:
        return(str(pas))
    else:
        generator()
with open('first_repo/students.csv', encoding="utf8") as a:
    reader = list(csv.DictReader(a, delimiter=',', quotechar='"'))
    arr = list(reader)
a = {}
print ('id,Name,titleProject_id,class,score')
for i in arr:
    name = i['Name']
    SecName = name.split()
    second_name = SecName[0]
    fir_name = SecName[1]
    first_name = fir_name[0]
    thi_name = SecName[2]
    third_name = thi_name[0]
    full = second_name + '_' + first_name + third_name
    print(i['id'] + "," + i['Name'] + ',' + i['titleProject_id'] + "," + i['class'] + "," + i['score'] + ',', end='')
    print(full + ',', end='')
    print(generator())