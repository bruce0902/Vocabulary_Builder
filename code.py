import keyboard
import os


def clear():
    os.system('cls')
    size = os.get_terminal_size()
    vertical = int((size[1])/2-3)
    for i in range(0, vertical):
        print()


def print_middle(x):
    size = os.get_terminal_size()
    horizontal = int((size[0])/2-5)
    for i in range(0, horizontal):
        print(" ", end='')
    print(x)


clear()

mode = input("Press \'l\' to start learn mode, press \'t\' to start test mode:")
while (mode != 'l' and mode != 't'):
    clear()
    print("wrong input! please input letter \'l\' or \'t\' in lower case")
    mode = input(
        "Press \'l\' to start learn mode, press \'t\' to start test mode:")

clear()
try:
    with open("./column.json","r") as r:
        last_column = r.read()
        print("The last column you learnt was column: " + last_column)
except:
    print("This is the first time you use this program")

column = input("put in the column you want to learn:")
while len(column) != 2 or not column.isdigit():
    clear()
    print("wrong input! please input number like 01, 03, 11...")
    column = input("put in the column you want to learn:")

num = 0
clear()

with open("./column.json","w") as w:
    w.write(column)


def read_words():
    location = "./words/words" + column + ".txt"
    data = open(location, "r")
    cab = []
    for line in data.readlines():
        cab.append(line.strip().split(','))
    cab_f = []
    for i in range(len(cab)):
        for j in range(len(cab[i])):
            if cab[i][j] != '':
                cab_f.append(cab[i][j].strip())
    cab_final = []
    for i in cab_f:
        for j in i.split(' '):
            cab_final.append(j)
    return cab_final


def read_meaning():
    location = "./meaning/meaning" + column + ".txt"
    data = open(location, "r", encoding='utf-8')
    cab = []
    for line in data.readlines():
        cab.append(line.strip().split(','))
    cab_f = []
    for i in range(len(cab)):
        for j in range(len(cab[i])):
            if cab[i][j] != '':
                cab_f.append(cab[i][j].strip())
    cab_final = []
    for i in cab_f:
        for j in i.split(' '):
            cab_final.append(j)
    return cab_final


words = read_words()
meaning = read_meaning()


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
            " Press page up to go to the first word \n Press page down to go to the last \n Press enter to show all the words \n Press n to show the number of the current word \n Press ctrl to exit")
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
        print(" Press page up to go to the first word \n Press page down to go to the last \n Press enter to show all the words \n Press n to show the number of the current word \n Press ctrl to exit")
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
