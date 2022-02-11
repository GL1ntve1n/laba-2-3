#сортировка пузырьком
from random import randint  #библиотека для рандома
x=int(input())
a=[]
for i in range (x):         #заполнение массива случайными числами
    a.append(randint(1,99))
print(a)

for i in range(x-1):        #сортировка массива
    for j in range (x-i-1):
        if a[j]>a[j+1]:
            a[j]=a[j+1]
            a[j+1]=a[j]
print(a)

