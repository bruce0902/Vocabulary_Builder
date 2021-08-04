# Vocabulary_Builder
A program on terminal helping people to build their vocabulary.  
If you want to see the key-binding of this program, press tab during using this script.
This branch can read words and meaning from excel format(.xlsx file)

## 这个版本可以从excel格式的文件中读取单词和意思。

# 中文版教程：
这个小程序是用来在电脑上用终端和键盘快速记单词。  
分为两个模式：learn-mode和test-mode。learn-mode每次显示一个单词以及它的意思。用方向键左右来选择前一个和后一个单词。enter键可显示所有单词，n键显示当前单词是第几个以及一共有多少单词。按ctrl键来退出。page up和page down可以直接跳到第一个和最后一个单词，按Tab键来获取提示。
test-mode初始只显示单词，需要按方向键上键才能显示意思，按下键可以删除当前单词，表示已经记住，其他键与learn-mode相同。通过不断删除单词，可以把注意力集中在难记的，还没有记住的单词上，提高效率。  

# 使用方法：
这个软件用python写成，首先需要有python3的环境。  
下载整个zip文件，解压后在vscode或终端中打开。这个程序用到了keyboard库和xlrd3库，可通过pip install keyboard和pip install xlrd3进行下载。  
如果用vscode运行，打开code_excel.py文件，点击右上角在终端中运行即可。  
如果用Windows powershell，当前文件夹，点击窗口右上角的文件选项，点击“打开Windows PowerShell”，之后在命令行中输入 python code_excel.py即可。  
之后按提示输入想选择的模式，以及需要背哪一个文件中的单词，之后按方向键进行操作。  

## 优点
目前市面上大多数背单词软件都在安卓或者ios端。但是这些平台屏幕小，也不方便在课堂，图书馆，公司等场合下使用。这个软件可以在电脑上用键盘来背单词，声音小，操作更为方便。  

## 注意  
- 如果无法用pip install安装keyboard库，可将文件夹keyboard_master里的文件取出，放在code.py的路径下即可。
