import keyboard

mode = 0
# mode = 0:背单词模式
# mode = 1:检测模式

words = ["reckless", "unsparing", "belligerent", "taciturn", "plead"]
meaning = ["粗心的，鲁莽的", "无情的，苛求的，不节俭的", "好斗的", "沉默寡言的", "辩护"]
num = 0
length = len(words)


def direction(x):
    global num
    a = keyboard.KeyboardEvent('down', 28, 'left')
    b = keyboard.KeyboardEvent('down', 28, 'right')
    c = keyboard.KeyboardEvent('down', 28, 'up')
    d = keyboard.KeyboardEvent('down', 28, 'down')
    if x.event_type == 'down' and x.name == a.name:
        print(words[num])
        print(meaning[num])
        num = num - 1
    if x.event_type == 'down' and x.name == b.name:
        print(words[num])
        print(meaning[num])
        if num < len(words) - 1:
            num = num + 1
    if x.event_type == 'down' and x.name == c.name:
        print(meaning[num])
    if x.event_type == 'down' and x.name == d.name:
        print("down键")

if mode == 0:
    keyboard.hook(direction)
if mode == 1:
    keyboard.hook(direction)
keyboard.wait()
