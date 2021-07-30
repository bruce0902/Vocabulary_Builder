import keyboard
import os


def clear():
    os.system('cls')
    size = os.get_terminal_size()
    vertical = int((size[1])/2-2)
    for i in range(0, vertical):
        print()


def print_middle(x):
    size = os.get_terminal_size()
    horizontal = int((size[0])/2-7)
    for i in range(0, horizontal):
        print(" ", end='')
    print(x)


clear()
mode = input("Press l to start learn mode, press t to start test mode:")
list = input("put in the list you want to learn:")
num = 0
clear()


def read_words():
    location = "D:\SUMMER\Vocabulary_Builder\words" + list + ".txt"
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
    location = "D:\SUMMER\Vocabulary_Builder\meaning" + list + ".txt"
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
        print_middle("Press page up to go to the first word")
    if x.event_type == 'down' and x.name == 'n':
        print_middle("The number of this word is: " +
                     str(num + 1) + " / " + str(len(words)))


def test(x):
    global num
    if x.event_type == 'down' and x.name == 'left':
        clear()
        if num > 0:
            num = num - 1
        print_middle(words[num])
    if x.event_type == 'down' and x.name == 'right':
        clear()
        if num < len(words) - 1:
            num = num + 1
        print_middle(words[num])
    if x.event_type == 'down' and x.name == 'up':
        print_middle(meaning[num])
    if x.event_type == 'down' and x.name == 'down':
        clear()
        del words[num]
        del meaning[num]
        if len(words) > 0 and num < len(words):
            print_middle(words[num])
        elif 0 < len(words) == num:
            num = 0
            print_middle(words[num])
        else:
            print_middle("complete!")
    if x.event_type == 'down' and x.name == 'enter':
        clear()
        print_middle("Number of the words left:")
        print_middle(len(words))
    if x.event_type == 'down' and x.name == 'page up':
        clear()
        num = 0
        print_middle(words[num])
    if x.event_type == 'down' and x.name == 'page down':
        clear()
        num = len(words)-1
        print_middle(words[num])
    if x.event_type == 'down' and x.name == 'tab':
        clear()
        print_middle("Press page up to go to the first word")
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

# press ctrl to close
keyboard.wait('ctrl')
clear()