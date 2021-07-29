import keyboard
import os

mode = 0
# mode = 0:背单词模式
# mode = 1:检测模式
num = 0


def clear():
    os.system('cls')


def read_words():
    data = open(r'D:\SUMMER\GRE\words.txt')
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
    data = open(r'D:\SUMMER\GRE\meaning.txt', encoding='utf-8')
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
length = len(words)


def learn(x):
    global num
    a = keyboard.KeyboardEvent('down', 28, 'left')
    b = keyboard.KeyboardEvent('down', 28, 'right')
    d = keyboard.KeyboardEvent('down', 28, 'down')
    if x.event_type == 'down' and x.name == a.name:
        clear()
        print(words[num])
        print(meaning[num])
        num = num - 1
    if x.event_type == 'down' and x.name == b.name:
        clear()
        print(words[num])
        print(meaning[num])
        if num < len(words) - 1:
            num = num + 1
    if x.event_type == 'down' and x.name == d.name:
        clear()
        print("down键")


def test(x):
    global num
    a = keyboard.KeyboardEvent('down', 28, 'left')
    b = keyboard.KeyboardEvent('down', 28, 'right')
    c = keyboard.KeyboardEvent('down', 28, 'up')
    d = keyboard.KeyboardEvent('down', 28, 'down')
    if x.event_type == 'down' and x.name == a.name:
        clear()
        print(words[num])
        num = num - 1
    if x.event_type == 'down' and x.name == b.name:
        clear()
        print(words[num])
        if num < len(words) - 1:
            num = num + 1
    if x.event_type == 'down' and x.name == c.name:
        print(meaning[num - 1])
    if x.event_type == 'down' and x.name == d.name:
        clear()
        print("down键")


if mode == 0:
    keyboard.hook(learn)
if mode == 1:
    keyboard.hook(test)
keyboard.wait()
