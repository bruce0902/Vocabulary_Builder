import keyboard
import os

num = 0
mode = 1
#change mode here 
# mode = 0:learn mode
# mode = 1:test mode


def clear():
    os.system('cls')
clear()

def read_words():
    #the source of the words,change location here
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
    #the source of the meaning,change location here
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
    global num,mode
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
        if num > 0:
            num = num - 1
        print(words[num])
    if x.event_type == 'down' and x.name == 'right':
        clear()
        if num < len(words) - 1:
            num = num + 1
        print(words[num])
    if x.event_type == 'down' and x.name == 'up':
        print(meaning[num])
    if x.event_type == 'down' and x.name == 'down':
        del words[num]
        del meaning[num]
        clear()
        if len(words) > 0 and num < len(words):
            print(words[num])
        elif 0 < len(words) == num:
            num = 0
            print(words[num])
        else:
            print("complete!")
    if x.event_type == 'down' and x.name == 'shift':
        clear()
        print("Number of the words left:" )
        print(len(words))


if mode == 0:
    print(words[num])
    print(meaning[num])
    keyboard.hook(learn)
    
if mode == 1:
    print(words[num])
    keyboard.hook(test)
    
#press ctrl to close
keyboard.wait('ctrl')
clear()
