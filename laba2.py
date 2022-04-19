import re
buffer_len = 1
work_buffer = ""
str = ""
flag = 0
flag_2 = False
flag_3 = False
try:
    with open("laba.txt", 'r+', encoding='utf-8') as file: #открытие файла
        print("\n Результат работы программы")
        buffer = file.read(buffer_len) #чтение буфера
        if not buffer: #если буфер пустой
            print("\n Рабочий файл пустой")
        while buffer: #если буфер не пустой
            work_buffer += buffer #заполнение рабочего буфера символами из файла
            if re.findall(r'[?]', buffer): #если найдет ? знак
                flag_2 = True
                if len(work_buffer) == 1: #для случая когда перевд вопросительным знаком стоит еще один знак препинания (!?)
                    work_buffer = ""
                    work_buffer += str + "?"
                print(work_buffer) #вывод буфера
            if re.findall(r'[.!]', work_buffer): #если нашкась . или ! знак
                str += work_buffer
                flag += 1
                work_buffer = ""
                flag_3 = True
            buffer = file.read(buffer_len) #чтение буфера
            if buffer != "?" and flag_3: #условие если 2 знака препинаня подряд
                str = ""
        if not flag_2: #если нет вопросительных предложений
            print("В файле нет вопросительных предложений")
        if flag == 0:  # Если нет окончания предложения
            print("\nФайл не содержит знаков окончания предложения.")
except FileNotFoundError: # если файл не найдет в директории
    print("\n Файл проекта не обнаружен в директории.")