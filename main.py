import csv
scores=[]
scores1=[]
uch=0
def max_num(num):
    j = 0
    for i in num:
        if j < i:
            j = i
    return j

def min_num(num):
    h = 1
    for i in num:
        if h > i:
            h = i
    return h
with open('students.csv', encoding="utf8") as r_file:
    file_reader =  csv.reader(r_file, delimiter=',')
    data = [list(map(str, ', '.join(x).split(', '))) for x in file_reader if x]
print(data)
for i in data[1:]:
    if 'Хадаров Владимир Валериевич' in i:
        print('Ты получил:', i[4] , ', за проект -' , i[2])
    if i[3][:2]=='10' and i[4]!='None':
        scores.append(int(i[4]))
    if i[4]!='None' :
        scores1.append(int(i[4]))
data1 = data
for i in range(len(data)):
    if data1[i][4]=='None':
        data1[i][4]=round(sum(scores1)/len(scores1), 3)

#with open('students.csv', 'w', newline='', encoding="utf8") as w_file:
  #  writer = csv.writer(w_file, delimiter=';')
   # writer.writerows(data1)
data2 = data
data.remove(data[0])

for i in data:
    if int(i[4])==max_num(scores) and i[3][:2]=='10':
        scores.remove(max_num(scores))
        data.remove(i)
        f, ii,o = map(str, i[1].split())
        print('1 место: ', ii[0], '. ', f, sep='')
        break
for j in data[1:]:
    if int(j[4])==max_num(scores) and j[3][:2]=='10':
        scores.remove(max_num(scores))
        data.remove(j)
        f1, ii1,o1 = map(str, j[1].split())
        print('2 место: ', ii1[0], '. ', f1, sep='')
        break
for k in data[1:]:

    if int(k[4])==max_num(scores) and k[3][:2]=='10':
        scores.remove(max_num(scores))
        data.remove(k)
        f2, ii2,o2 = map(str, k[1].split())
        print('3 место: ', ii2[0], '. ', f2, sep='')
        break

data = data2