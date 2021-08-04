# Vocabulary_Builder
A program on terminal helping me to build my vocabulary.  
If you want to see the key-binding of this program, press tab during using this script.
This branch can read words and meaning from excel format(.xlsx file)

## 这个版本可以从excel格式的文件中读取单词和意思。
# 中文版教程：
这个小程序是用来在电脑上用终端和键盘快速记单词。  
分为两个模式：learn-mode和test-mode。learn-mode每次显示一个单词以及它的意思。用方向键左右来选择前一个和后一个单词。enter键可显示所有单词，n键显示当前单词是第几个以及一共有多少单词。按ctrl键来退出。page up和page down可以直接跳到第一个和最后一个单词，按Tab键来获取提示。
test-mode初始只显示单词，需要按方向键上键才能显示意思，按下键可以删除当前单词，表示已经记住，其他键与learn-mode相同。通过不断删除单词，可以把注意力集中在难记的，还没有记住的单词上，提高效率。  

这个程序用到了keyboard库和xlrd3库，可通过pip install keyboard和pip install xlrd3进行下载。  
在vscode的终端中运行，或者用windows powershell在文件的路径下输入python code.py。之后按提示输入想选择的模式，以及需要背哪一个文件中的单词，之后按方向键进行操作。

## 注意  
- 如果无法用pip install安装keyboard库，可将文件夹keyboard_master里的文件取出，放在code.py的路径下即可。
