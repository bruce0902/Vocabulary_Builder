import os


def clear():
    os.system('cls')
    size = os.get_terminal_size()
    vertical = int((size[1]) / 2 - 2)
    for i in range(vertical):
        print()


def print_filename():
    clear()
    print('These are the vocabulary that you can learn:')
    path = r'vocabulary'
    num = 1
    for filename in os.listdir(path):
        print(num, end='')
        print(' ', end='')
        print(os.path.join(filename))
        num += 1


def choose_vocabulary():
    print_filename()
    vocabulary = input(
        'put in the number of the vocabulary that you want to learn:')
    list = ['1', '2']
    while vocabulary not in list:
        if vocabulary == '1':
            with open("./data/vocabulary.txt", "w") as w:
                w.write('GRE佛脚词汇.xlsx')
        if vocabulary == '2':
            with open("./data/vocabulary.txt", "w") as w:
                w.write('GRE核心词汇乱序版.xlsx')
        else:
            clear()
            print_filename()
            print("wrong number!")
            vocabulary = input(
                'put in the number of the vocabulary that you want to learn:')

choose_vocabulary()
