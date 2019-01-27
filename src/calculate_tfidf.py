import os
import math
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
    clean_word_list_count = {}
    for word in clean_word_list:
        clean_word_list_count[word] = clean_word_list_count.get(word, 0) + 1
        if word not in universal_word_list:
            universal_word_list.append(word)
    word_list_by_document.append(clean_word_list_count)
doc_freq = {}
for word in universal_word_list:
    freq = 0
    for i in word_list_by_document:
        if word in i:
            freq+=1
    doc_freq[word] = freq
print("-----------Starting tf-idf matrix generator------------")
tfidf = []
count = 0
doc_no = len(word_list_by_document)
for word_list in word_list_by_document:
    print("Document No "+str(count)+":")
    tfidf_doc = []
    for word in universal_word_list:
        tf_value = word_list.get(word,0)/len(word_list)
        idf_value = math.log(doc_no/doc_freq[word])
        tfidf_doc.append(tf_value*idf_value)
    tfidf.append(tfidf_doc)
    count+=1
fhandler = open("tfidf.txt",'w+')
fhandler.write(str(tfidf))
fhandler.write(str(file_list))
fhandler.write(str(universal_word_list))