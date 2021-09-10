import os

import keyboard
import xlrd3 as xlrd


def clear():
    os.system('cls')
    size = os.get_terminal_size()
    vertical = int((size[1]) / 2 - 2)
    for i in range(vertical):
        print()


def print_middle(x):
    size = os.get_terminal_size()
    width_ori = len(x)
    width_utf = len(x.encode('utf-8'))
    width = int((width_utf - width_ori) / 2 + width_ori)
    horizontal = int((size[0] - width) / 2)
    for i in range(horizontal):
        print(" ", end='')
    print(x)


def return_num_of_lists():
    if len(all_words) % 50 == 0:
        number_of_lists = int(len(all_words) / 50)
    else:
        number_of_lists = int(1 + len(all_words) / 50)
    return number_of_lists


def show_last_group():
    clear()
    try:
        with open("./data/group.txt", "r") as r:
            last_group = r.read()
            print(" The last group you learned was group: " + last_group)
    except:
        print(" This is the first time you use this program")
    else:
        pass


def write_last_group():
    clear()
    with open("./data/group.txt", "w") as w:
        w.write(group)


def update_words():
    global words, meaning, num, mode
    keyboard.press("enter")
    keyboard.release("enter")
    clear()
    choose_group()
    return_words()
    return_meaning()
    write_last_group()
    num = 0
    clear()
    if mode == 'l':
        print_middle(words[0])
        print_middle(meaning[0])
    if mode == 't':
        print_middle(words[0])


def choose_mode():
    clear()
    mode_first = input(
        "Press \'l\' to start learn mode, press \'t\' to start test mode: ").lower()
    while mode_first != 'l' and mode_first != 't':
        clear()
        print("wrong input! please input letter \'l\' or \'t\' ")
        mode_first = input(
            "Press \'l\' to start learn mode, press \'t\' to start test mode: ").lower()
    return mode_first


def choose_group():
    global group
    group = input(" There are " + str(num_of_lists) +
                  ''' groups, put in the group you want to learn
    input 0 if you want to learn the saved files ''')
    lists = []
    for i in range(0, num_of_lists + 1):
        lists.append(str(i))
    while group not in lists:
        clear()
        if group.endswith("g"):
            group = input(" There are " + str(num_of_lists) +
                          ''' groups, put in the group you want to learn
    input 0 if you want to learn the saved files ''')
        else:
            print(" wrong input! please input number like 1, 2, 3, 11...")
            group = input(''' groups, put in the group you want to learn
            \n input 0 if you want to learn the saved files \n''')


def return_words():
    global group
    global words
    if group == "0":
        words = read_saved("data\saved_words.txt")
    else:
        words = eval("words" + group)


def return_meaning():
    global meaning
    if group == "0":
        meaning = read_saved("data\saved_meaning.txt")
    else:
        meaning = eval("meaning" + group)


def choose_vocabulary():
    with open("data/vocabulary.txt", "r") as r:
            vocabulary =  r.read()
    return vocabulary


def read_words():
    location = 'vocabulary/' + choose_vocabulary()
    book = xlrd.open_workbook(location)
    sheet = book.sheet_by_index(0)
    all_word = [str(sheet.cell_value(i, 0)) for i in range(1, sheet.nrows)]
    return all_word


def read_meaning():
    location = 'vocabulary/' + choose_vocabulary()
    book = xlrd.open_workbook(location)
    sheet = book.sheet_by_index(0)
    all_meanings = [str(sheet.cell_value(i, 1)) for i in range(1, sheet.nrows)]
    for i in range(len(all_words)):
        all_meanings[i] = all_meanings[i].replace(' ', '')
        all_meanings[i] = all_meanings[i].replace('\n', ' ').replace('\r', '')
    return all_meanings


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


class Mode:
    def common(self, x, mode_in):
        global num
        global last_key
        if last_key != 'a':
            if x.event_type == 'down' and x.name == 'a':
                last_key = x.name
                clear()
                for i in range(0, len(words)):
                    print_middle(words[i])
                    print_middle(meaning[i])
        if last_key != 'n':
            if x.event_type == 'down' and x.name == 'n':
                last_key = x.name
                print_middle("The number of this word is: " +
                             str(num + 1) + " / " + str(len(words)))
        if x.event_type == 'down' and x.name == 'left':
            last_key = x.name
            clear()
            if num > 0:
                num = num - 1
            print_middle(words[num])
            if mode_in == 0:
                print_middle(meaning[num])
        if x.event_type == 'down' and x.name == 'right':
            last_key = x.name
            clear()
            if num < len(words) - 1:
                num = num + 1
            print_middle(words[num])
            if mode_in == 0:
                print_middle(meaning[num])
        if last_key != 'home':
            if x.event_type == 'down' and x.name == 'home':
                last_key = x.name
                clear()
                num = 0
                print_middle(words[num])
                if mode_in == 0:
                    print_middle(meaning[num])
        if last_key != 'end':
            if x.event_type == 'down' and x.name == 'end':
                last_key = x.name
                clear()
                num = len(words) - 1
                print_middle(words[num])
                if mode_in == 0:
                    print_middle(meaning[num])
        if x.event_type == 'down' and x.name == 'g':
            last_key = x.name
            update_words()

    def learn(self, x):
        global num
        global last_key
        global mode
        if last_key != 'tab':
            if x.event_type == 'down' and x.name == 'tab':
                last_key = x.name
                clear()
                print(
                    ''' Press home to go to the first word 
                    \n Press end to go to the last 
                    \n Press a to show all the words 
                    \n Press n to show the number of the current word 
                    \n Press esc to exit
                    \n Press t to go to test mode''')
        Mode.common(self, x, 0)
        if x.event_type == 'down' and x.name == 't':
            mode = 't'
            clear()
            print_middle('now is test mode')

    def test(self, x):
        global num
        global last_key
        global mode
        global deleted_word
        global deleted_meaning
        global num_of_deleted
        if last_key != 'up':
            if x.event_type == 'down' and x.name == 'up':
                last_key = x.name
                try:
                    print_middle(meaning[num])
                except:
                    clear()
                    print_middle("complete! press esc to exit")
        if x.event_type == 'down' and x.name == 'down':
            last_key = x.name
            deleted_word = words[num]
            deleted_meaning = meaning[num]
            num_of_deleted = num
            clear()
            try:
                del words[num]
                del meaning[num]
            except:
                clear()
                print_middle("complete! press esc to exit")
            if len(words) > 0 and num < len(words):
                print_middle(words[num])
            elif 0 < len(words) == num:
                num = 0
                print_middle(words[num])
            elif len(words) == 0:
                clear()
                print_middle("complete! press esc to exit")
        if last_key != 'z' and deleted_word != 'none':
            if x.event_type == 'down' and x.name == 'z':
                last_key = x.name
                clear()
                words.insert(num_of_deleted,deleted_word)
                meaning.insert(num_of_deleted,deleted_meaning)
                num = num_of_deleted
                print_middle(words[num])
        if last_key != 'tab':
            if x.event_type == 'down' and x.name == 'tab':
                last_key = x.name
                clear()
                print(''' Press home to go to the first word 
                \n Press end to go to the last 
                \n Press a to show all the words 
                \n Press n to show the number of the current word 
                \n Press esc to exit
                \n Press up to show the meaning of the word.
                \n Press down to delete the world.
                \n Press s to save the files
                \n Press l to go to learn mode
                \n Press z to withdraw the last delete''')
        if last_key != 's':
            if x.event_type == 'down' and x.name == 's':
                last_key = x.name
                words_saved = words
                meaning_saved = meaning
                words_s = open('data\saved_words.txt', 'w')
                for w in words_saved:
                    words_s.write(w)
                    words_s.write('\n')
                words_s.close()
                meaning_s = open('data\saved_meaning.txt', 'w', encoding='utf-8')
                for m in meaning_saved:
                    meaning_s.write(m)
                    meaning_s.write('\n')
                meaning_s.close()
                clear()
                print_middle("saved!")
        if x.event_type == 'down' and x.name == 'l':
            mode = 'l'
            clear()
            print_middle('now is learn mode')
        Mode.common(self, x, 1)

    def both_mode(self, x):
        global mode
        if mode == 'l':
            Mode.learn(self, x)
        if mode == 't':
            Mode.test(self, x)


def main_program():
    global mode
    if mode == "l":
        print_middle(words[0])
        print_middle(meaning[0])
        keyboard.hook(Mode().both_mode)
    if mode == "t":
        print_middle(words[0])
        keyboard.hook(Mode().both_mode)
    else:
        pass
    keyboard.wait('esc')
    clear()


if __name__ == "__main__":
    mode = choose_mode()
    all_words = read_words()
    all_meaning = read_meaning()
    num_of_lists = return_num_of_lists()

    for i in range(num_of_lists):
        exec("words%s=all_words[50*%d:50*%d+50]" % (i + 1, i, i))
        exec("meaning%s=all_meaning[50*%d:50*%d+50]" % (i + 1, i, i))

    show_last_group()
    choose_group()
    return_words()
    return_meaning()
    write_last_group()

    num = 0
    last_key = 'none'
    deleted_word = 'none'
    deleted_meaning = 'none'
    num_of_deleted = 0
    main_program()
