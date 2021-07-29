import keyboard
import os

mode = 0
# mode = 0:背单词模式
# mode = 1:检测模式
num = 0


def clear():
    os.system('cls')
clear()

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


def learn(x):
    global num
    if x.event_type == 'down' and x.name == 'left':
        clear()
        if num > 0:
            num = num - 1
        print(words[num])
        print(meaning[num])
    if x.event_type == 'down' and x.name == 'right':
        clear()
        if num < len(words) - 1:
            num = num + 1
        print(words[num])
        print(meaning[num])
    if x.event_type == 'down' and x.name == 'down':
        del words[num]
        del meaning[num]
        clear()
        if len(words)>0 and num < len(words):
            print(words[num])
            print(meaning[num])
        else:
            print("complete!")


def test(x):
    global num
    if x.event_type == 'down' and x.name == 'left':
        clear()
        print(words[num])
        if num > 0:
            num = num - 1
    if x.event_type == 'down' and x.name == 'right':
        clear()
        print(words[num])
        if num < len(words) - 1:
            num = num + 1
    if x.event_type == 'down' and x.name == 'up':
        print(meaning[num - 1])
    if x.event_type == 'down' and x.name == 'down':
        if len(words) > 0:
            del words[num - 1]
            del meaning[num - 1]
            clear()

print(words[num])
print(meaning[num])
if mode == 0:
    keyboard.hook(learn)
    
if mode == 1:
    keyboard.hook(test)
    
keyboard.wait('esc')
