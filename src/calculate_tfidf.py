import os
os.chdir("../bbcsport")
file_list = os.listdir()
for i in file_list:
    if os.path.isdir(i):
        file_list = file_list + [ i + '/' + x for x in os.listdir(i) ]
        file_list.remove(i)
file_list.remove(".DS_Store")
universal_word_list = []
word_list_by_document = []
for file in file_list:
            text = open(file,'r').read()
            for char in range(len(text)):
                if not ('a'<=text[char]<='z' or 'A'<=text[char]<='Z' or (text[char]=='\'' and (('a'<=text[char-1]<='z' or 'A'<=text[char-1]<='Z') and ('a'<=text[char+1]<='z' or 'A'<=text[char+1]<='Z')))):
                    text = text[:char] + ' ' + text[char+1:]
            clean_word_list = [x for x in text.split(' ') if x != '']
            word_list_by_document.append(clean_word_list)
            for word in clean_word_list:
                if word not in universal_word_list:
                    universal_word_list.append(word)
