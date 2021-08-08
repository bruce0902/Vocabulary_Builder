import os

import keyboard
import xlrd3 as xlrd

num = 0
def clear():
    os.system('cls')
    size = os.get_terminal_size()
    vertical = int((size[1])/2-2)
    for i in range(0, vertical):
        print()


def read_saved(location):
    data = open(location, "r", encoding='utf-8')
    cab = []
    for line in data.readlines():
        cab.append(line.strip().split(','))
    cab_f = []
    for i in range(len(cab)):
        for j in range(len(cab[i])):
            if cab[i][j] != '':
                cab_f.append(cab[i][j].strip())
    return cab_f


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
    global num
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
    if x.event_type == 'down' and x.name == 's':
        words_saved = words
        meaning_saved = meaning
        words_s = open('saved_words.txt', 'w')
        for w in words_saved:
            words_s.write(w)
            words_s.write('\n')
        words_s.close()
        meaning_s = open('saved_meaing.txt', 'w', encoding='utf-8')
        for m in meaning_saved:
            meaning_s.write(m)
            meaning_s.write('\n')
        meaning_s.close()
        clear()
        print_middle("saved!")


def show_last_group():
    try:
        with open("./group.json", "r") as r:
            last_group = r.read()
            print("The last group you learned was group: " + last_group)
    except:
        print("This is the first time you use this program")


def choose_mode():
    clear()
    mode = input(
        "Press \'l\' to start learn mode, press \'t\' to start test mode: ").lower()
    while (mode != 'l' and mode != 't'):
        clear()
        print("wrong input! please input letter \'l\' or \'t\' ")
        mode = input(
            "Press \'l\' to start learn mode, press \'t\' to start test mode: ").lower()
    show_last_group()
    return mode


def write_last_group():
    clear()
    with open("./group.json", "w") as w:
        w.write(group)


def read_words():
    book = xlrd.open_workbook("data.xlsx")
    sheet = book.sheet_by_index(0)
    words = [str(sheet.cell_value(i, 0)) for i in range(1, sheet.nrows)]
    return words


def read_meaning():
    book = xlrd.open_workbook("data.xlsx")
    sheet = book.sheet_by_index(0)
    meaning = [str(sheet.cell_value(i, 1)) for i in range(1, sheet.nrows)]
    for i in range(len(all_words)):
        meaning[i] = meaning[i].replace(' ', '')
        meaning[i] = meaning[i].replace('\n', ' ').replace('\r', '')
    return meaning


def return_num_of_lists():
    if len(all_words) % 50 == 0:
        number_of_lists = int(len(all_words)/50)
    else:
        number_of_lists = int(1+len(all_words)/50)
        return number_of_lists


def choose_group():
    group = input("There are " + str(num_of_lists) +
                  ''' groups, put in the group you want to learn,
    input 0 if you want to learn the saved files ''')
    lists = []
    for i in range(0, num_of_lists + 1):
        lists.append(str(i))

    while group not in lists:
        clear()
        print("wrong input! please input number like 1, 2, 3, 11...")
        group = input(''' groups, put in the group you want to learn: 
    input 0 if you want to learn the saved files ''')
    return group


def main_program(mode):
    if mode == "l":
        print_middle(words[0])
        print_middle(meaning[0])
        keyboard.hook(learn)

    if mode == "t":
        print_middle(words[0])
        keyboard.hook(test)
    else:
        pass
    keyboard.wait('ctrl')
    clear()


def return_words(group):
    if group == "0":
        words = read_saved("saved_words.txt")
    else:
        words = eval("words" + group)
    return words


def return_meaning(group):
    if group == "0":
        meaning = read_saved("saved_meaing.txt")
    else:
        meaning = eval("meaning" + group)
    return meaning


if __name__ == "__main__":
    mode = choose_mode()
    all_words = read_words()
    all_meaning = read_meaning()
    num_of_lists = return_num_of_lists()

    for i in range(num_of_lists):
        exec("words%s=all_words[50*%d:50*%d+50]" % (i+1, i, i))
        exec("meaning%s=all_meaning[50*%d:50*%d+50]" % (i+1, i, i))

    group = choose_group()

    words = return_words(group)
    meaning = return_meaning(group)

    num = 0
    write_last_group()
    main_program(mode)

