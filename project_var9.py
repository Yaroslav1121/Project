import csv
import os
import sys
from PIL import Image
import json

clear = lambda : os.system('cls')
filename = "table.txt"


def main_menu():
    while (True):
        print(" . : : : : : : : : : : : : : : : : : : : . ")
        print(" . : : : : : : ГОЛОВНЕ МЕНЮ  : : : : : : .")
        print(" . : : : : : : : : : : : : : : : : : : : . ")
        x = int(
            input("Оберіть потрібну опцію: \n > 1 - Вивести вихідні файли  \n > 2 - Фільтрувати по критерію  \n > 3 - "
                  "Завершити роботу \n"))
        mode = ' '
        if x == 1:
            read()
        elif x == 2:
            filter1()
        elif x == 3:
            close()
        else:
            print("такого варіанту не існує")


def read():
    clear()
    v = int(input("Оберіть формат виводу файлу: \n > 1 - Консольна таблиця  \n > 2 - Текстовий файл \n"
                  " > 3 - Файл у форматі JSON \n > 4 - Таблиця Excel \n > 5 - Графік\n"))
    if v == 1:
        clear()
        console_p(filename)
    elif v == 2:
        clear()
        os.system('start notepad.exe table.txt')
    elif v == 3:
        clear()
        fd = open(filename, "r")
        reader = csv.reader(fd, delimiter="\t")
        for row in reader:
            print(row)
        fd.close()
        returning()
    elif v == 4:
        clear()
        os.system('start excel.exe excel.xlsx')
    elif v == 5:
        clear()
        img = Image.open('graphic.png')
        img.show()
    else:
        print("такого варіанту не існує")


def console_p(filename):
    clear()
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()
    returning()


def close():
    sys.exit()


def returning():
    p = int(input('Натисніть 1 щоб вийти, 2 щоб повернутися до головного меню\n'))
    if p == 1:
        close()
    elif p == 2:
        clear()
        main_menu()


def year_filter():
    clear()
    y = int(input("Оберіть рік: \n > 1 - 2013  \n > "
                  "2 - 2014  \n > 3 - 2015 \n"))
    if y == 1:
        f_2013()
    elif y == 2:
        f_2014()
    elif y == 3:
        f_2015()
    else:
        print("такого варіанту не існує")
        clear()
        main_menu()


def filter1():
    clear()
    f = int(input("Оберіть потрібний фільтр: \n > 1 - Фільтр за роком  \n > "
                  "2 - Фільтр за товарною групою  \n > 3 - Повернутись до головного меню \n"))
    if f == 1:
        year_filter()
    elif f == 2:
        tovar_group()
    elif f == 3:
        clear()
        main_menu()
    else:
        print("такого варіанту не існує")
        clear()
        main_menu()


def tovar_group():
    clear()
    t = int(input("Оберіть тип товарної групи: \n > 1 - Тканини  \n > "
                  "2 - Одяг та білизна  \n > 3 - Взуття \n > 4 - Трикотаж \n > 5 - Галентерея \n"))
    if t == 1:
        tkanyny()
    elif t == 2:
        odyag_ta_bylizna()
    elif t == 3:
        vzuttya()
    elif t == 4:
        trykotazh()
    elif t == 5:
        galentereya()

main_menu()

