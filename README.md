# Vocabulary_Builder
A program on terminal helping me to build my vocabulary.  
If want to see the key-binding of this program, press tab during using this script.


# 中文版教程：
这个脚本是用来在电脑上用终端和键盘快速记单词。  
分为两个模式：learn-mode和test-mode。learn-mode每次显示一个单词以及它的意思。用方向键左右来控制前一个和后一个。enter键可显示所有单词，n键显示当前单词是第几个以及一共有多少单词。按ctrl键来返回。page up和page down可以直接跳到第一个和最后一个单词。 按Tab键来获取提示。
test-mode初始只显示单词，需要按方向键上键才能显示意思，按下键可以删除当前单词，表示已经记住，其他键与learn-mode相同。通过不断删除单词，可以把注意力集中在难记的单词上，提高效率。  

使用说明：  
下载code.py及words和meaning文件。其中words和meaning是从OneNote中的一列复制来的，每两个词之间空了一行，以此分隔单词。可自己定义words和meaning文件。  
这个程序用到了os和keyboard库，可通过pip install keyboard进行下载。  
之后根据自己的电脑改变代码中的读取words和meaning的地址。如果名字不是两位数字结尾，可自行调整。  
在vscode的终端中，或者windows powershell里打开文件，按提示输入想选择的模式，以及需要背哪一个文件中的单词，之后方向键进行操作。


## 注意  
- 如果出现修改完路径后出现“SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes”的问题，**把路径中的反斜杠改成正斜杠**。
- 如果无法安装keyboard库，可从此处下载：https://pypi.org/project/keyboard/。 之后可以放在运行的文件夹中或者interpreter的site_package里。
