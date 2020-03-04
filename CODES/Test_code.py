test_string = "Natural Language Processing is an aspect of Artificial Intelligence that involves how to program computers to efficiently process Natural Language data, providing a platform for exchanging useful information with humans.In achieving globalization and satisfying the need to communicateinternationally, challenges involving the NLP process have evolved from being extremely difficult to becoming more tractable due to the rapid growth in computing power and the advancement made in language processing algorithms (Ahmed, Cha and Tappert, 2004). Dealing with these challenges (involving speech recognition, speech translation and text-to-speech synthesis) have led to the successful performance of tasks such as sentiments analysis, question answering, part-of-speech tagging and information retrieval generally."
short_string = "Natural Language, is an aspect of Artificial Intelligence."

pos = 0
language_nab = ""
while pos < len(short_string):
    if short_string[pos] == "<":
        temp = "<"
        while short_string[pos] <> ">":
            temp += short_string[pos]
            pos += 1
    else:
        language_nab +=  short_string[pos]
        pos += 1



split_language = language_nab.split()
import string
wordlist = []
for word in split_language:
    '''if word.isdigit() = True:
        Yoruba_small.remove(word)'''
    #leaveout = [".",",",":",chr(34)]
    for char in word:
        if char in string.punctuation:  #to remove punctuation marks
        #if char == chr(34):  
            word = word.replace(char, '')
            
    word = word.decode("utf-8").lower()
    wordlist.append(word)
    #print word

    
'''testlist = []
for word in wordlist:
    if len(word) == 1 or len(word) == 2:
        testlist.append(word)
    else:    
        for i in range(0,len(word)-2):
            trigram = word[i:i+3]
            testlist.append(trigram)
for tri in testlist:
    print tri'''



trigfreq = {}
for word in wordlist:
        if len(word)==1 or len(word)==2:
            if word not in trigfreq:
                trigfreq[word] = 1
            else:
                trigfreq[word] += 1
        else:
            for i in range(0,len(word)-2):
                trigram = word[i:i+3]
                if trigram not in trigfreq:
                    trigfreq[trigram] = 1
                else:
                    trigfreq[trigram] += 1
for tri in trigfreq:
    print tri, trigfreq[tri]

'''def new_ab(a,b):
    print a
    print b
    new_b = []
    for ngram,prob in a:
        for ng,pb in b:
            if ng == ngram:
                new_b.append((ng,pb))
                b.remove((ng,pb))
                break
            elif (ngram,pb) not in new_b:
                new_b.append((ngram,0))

    for ngram,prob in b:
        new_b.append((ngram,prob))
        a.append((ngram,0))
    for i in new_b:
        print i
    for i in a:
        print i


train= [('abc', 0.001),('bcd', 0.003), ('ilk', 0.025), ('mof', 0.008), ('for', 0.006)]
test=[('ilk', 0.065), ('mar', 0.0005), ('abc', 0.004), ('ghf', 0.09), ('ifr', 0.007)]

new_ab(train,test)'''
