import csv

with open('students.csv') as f:
    a = csv.reader(f, delimiter=    ';')
arr = list(a)
print(a)
#for i in graph:
#    r = graph[a]