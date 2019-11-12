from nltk.corpus import words
word_list = set(words.words())
dictionary=set(word_list)
fp = open("newdict.txt","r", encoding="utf8")
fp1 = open("cleandata.txt","w")
fullstring = fp.read()
fullstring = fullstring.split()
wordset = set()
for i in fullstring:
    if i in word_list and not i[0].isupper():
        try:
            wordset.add(i)
        except:
            pass
        
for i in wordset:
    try:
        fp1.write(i+"\n")
    except:
        pass
fp.close()
fp1.close()