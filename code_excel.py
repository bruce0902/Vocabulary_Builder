import os

import keyboard
import xlrd3 as xlrd


def clear():
    os.system('cls')
    size = os.get_terminal_size()
    vertical = int((size[1])/2-2)
    for i in range(0, vertical):
        print()


clear()


mode = input("Press \'l\' to start learn mode, press \'t\' to start test mode: ")
while (mode != 'l' and mode != 't'):
    clear()
    print("wrong input! please input letter \'l\' or \'t\' in lower case")
    mode = input(
        "Press \'l\' to start learn mode, press \'t\' to start test mode: ")

try:
    with open("./group.json", "r") as r:
        last_group = r.read()
        print("The last group you learnt was group: " + last_group)
except:
    print("This is the first time you use this program")

book = xlrd.open_workbook("data.xlsx")
sheet = book.sheet_by_index(0)

words = [str(sheet.cell_value(i, 0)) for i in range(1, sheet.nrows)]
meaning = [str(sheet.cell_value(i, 1)) for i in range(1, sheet.nrows)]

for i in range(len(words)):
    meaning[i] = meaning[i].replace(' ', '')
    meaning[i] = meaning[i].replace('\n', ' ').replace('\r', '')

if len(words) % 50 == 0:
    number_of_lists = int(len(words)/50)
else:
    number_of_lists = int(1+len(words)/50)
for i in range(number_of_lists):
    exec("words%s=words[50*%d:50*%d+50]" % (i+1, i, i))
    exec("meaning%s=meaning[50*%d:50*%d+50]" % (i+1, i, i))
group = input("There are " + str(number_of_lists) +
              " groups, put in the group you want to learn: ")
word_chosen = "words" + group
meaning_chosen = "meaning" + group
words = eval(word_chosen)
meaning = eval(meaning_chosen)

clear()


num = 0
clear()

with open("./group.json", "w") as w:
    w.write(group)


def print_middle(x):
    size = os.get_terminal_size()
    width_ori = len(x)
    width_utf = len(x.encode('utf-8'))
    width = int((width_utf - width_ori) / 2 + width_ori)
    horizontal = int((size[0]-width)/2)
    for i in range(0, horizontal):
        print(" ", end='')
    print(x)


def learn(x):
    global num, mode
    if x.event_type == 'down' and x.name == 'left':
        clear()
        if num > 0:
            num = num - 1
        print_middle(words[num])
        print_middle(meaning[num])
    if x.event_type == 'down' and x.name == 'right':
        clear()
        if num < len(words) - 1:
            num = num + 1
        print_middle(words[num])
        print_middle(meaning[num])
    if x.event_type == 'down' and x.name == 'enter':
        clear()
        for i in range(0, len(words)):
            print_middle(words[i])
            print_middle(meaning[i])
    if x.event_type == 'down' and x.name == 'page up':
        clear()
        num = 0
        print_middle(words[num])
        print_middle(meaning[num])
    if x.event_type == 'down' and x.name == 'page down':
        clear()
        num = len(words)-1
        print_middle(words[num])
        print_middle(meaning[num])
    if x.event_type == 'down' and x.name == 'tab':
        clear()
        print(
            ''' Press page up to go to the first word \n Press page down to 
            go to the last \n Press enter to show all the words \n Press n 
            to show the number of the current word \n Press ctrl to exit''')
    if x.event_type == 'down' and x.name == 'n':
        print_middle("The number of this word is: " +
                     str(num + 1) + " / " + str(len(words)))


def test(x):
    global num
    if x.event_type == 'down' and x.name == 'left':
        clear()
        if num > 0:
            num = num - 1
        try:
            print_middle(words[num])
        except:
            clear()
            print_middle("complete! press ctrl to exit")
    if x.event_type == 'down' and x.name == 'right':
        clear()
        if num < len(words) - 1:
            num = num + 1
        try:
            print_middle(words[num])
        except:
            clear()
            print_middle("complete! press ctrl to exit")
    if x.event_type == 'down' and x.name == 'up':
        try:
            print_middle(meaning[num])
        except:
            clear()
            print_middle("complete! press ctrl to exit")
    if x.event_type == 'down' and x.name == 'down':
        clear()
        try:
            del words[num]
            del meaning[num]
        except:
            clear()
            print_middle("complete! press ctrl to exit")
        if len(words) > 0 and num < len(words):
            print_middle(words[num])
        elif 0 < len(words) == num:
            num = 0
            print_middle(words[num])
        elif len(words) == 0:
            clear()
            print_middle("complete! press ctrl to exit")

    if x.event_type == 'down' and x.name == 'enter':
        clear()
        for i in range(0, len(words)):
            print_middle(words[i])
            print_middle(meaning[i])
    if x.event_type == 'down' and x.name == 'page up':
        clear()
        num = 0
        try:
            print_middle(words[num])
        except:
            clear()
            print_middle("complete! press ctrl to exit")
    if x.event_type == 'down' and x.name == 'page down':
        clear()
        num = len(words)-1
        try:
            print_middle(words[num])
        except:
            clear()
            print_middle("complete! press ctrl to exit")
    if x.event_type == 'down' and x.name == 'tab':
        clear()
        print(''' Press page up to go to the first word \n 
        Press page down to go to the last \n Press enter to 
        show all the words \n Press n to show the number of
         the current word \n Press ctrl to exit''')
    if x.event_type == 'down' and x.name == 'n':
        print_middle("The number of this word is: " +
                     str(num + 1) + " / " + str(len(words)))


if mode == "l":
    print_middle(words[num])
    print_middle(meaning[num])
    keyboard.hook(learn)

if mode == "t":
    print_middle(words[num])
    keyboard.hook(test)
else:
    pass

keyboard.wait('ctrl')
clear()
