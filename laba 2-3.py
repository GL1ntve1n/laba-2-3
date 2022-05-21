import os
import time
import re
buffer_len = 1
work_buffer = ""
stg = ""
flag_2 = False
flag_3 = False
try:
    while 1:
        k = input('Введите число k:')                     #ввод значения переменной
        if k >= '0' and k <= '9':
            digit = int(k)
            break
        else:                                             #если число выходит за промежутки
            print('Введите число, не букву')
    start = time.time()
    print("\n-----Результат работы программы-----\n-----Локальное время", time.ctime(), "-----")
    print()
    with open("laba.txt", 'r+', encoding='utf-8') as file: #открытие файла
        buffer = file.read(buffer_len)                     #чтение буфера
        if not buffer:                                     #если буфер пустой
            print("\nФайл пустой")
            exit()
        while buffer:                                      #если буфер не пустой
            work_buffer += buffer                          #заполнение рабочего буфера символами из файла
            if re.findall(r'[?]', buffer):                 #если найдет ? знак
                flag_2 = True
                if len(work_buffer) == 1:                  #для случая когда перевд вопросительным знаком стоит еще один знак препинания (!?)
                    work_buffer = ""
                    work_buffer += stg + "!?"
                if digit != 0:
                    g = re.split(r'\W', work_buffer)       #разбиение строки на слова и цифры
                    g = g[:len(g) - 1]                     #удаление не нужного элемента списка
                    if len(g) - 1 > digit:                 #проверка на выполнение условие на кол-во слов
                        print(work_buffer)                 #вывод буфера
                    g = ""
                if digit == 0:                             #если вводится 0
                    print(work_buffer)                     #вывод буфера
                    flag_4 = True
                work_buffer = ""
            if re.findall(r'[.!]', work_buffer):           #если нашкась . или ! знак
                stg += work_buffer
                stg = stg[:len(stg) - 1]                   #удаление воскл. знака при двух знаках препинания (!?)
                work_buffer = ""
                flag_3 = True
            buffer = file.read(buffer_len)                 #чтение буфера
            if buffer != "?" and flag_3:                   #условие если 2 знака препинаня подряд
                stg = ""

        if not flag_2:                                     #если нет вопросительных предложений
            print("\nВ файле нет вопросительных предложений")

    finish = time.time()
    result = finish - start  # определяем время и память работы программы
    print("\nProgram time: " + str(result) + " seconds.")
    print("Program size: " + str(os.path.getsize('main.py')) + " bytes.")

except FileNotFoundError:                                  #если файл не найдет в директории
    print("\nФайл проекта не обнаружен в директории.")
except ValueError:                                         #если ввели не целое число
    print("\nВведите целое число")