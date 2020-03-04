#coding=utf-8
import os 
import string



def str_decode(text):
    return text.decode('utf-8')

def getFilePath(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return path
    
def lang_model(filepath):
    file_object = open(getFilePath(filepath),"r")
    file_document = file_object.read()
    out_file = file_document.replace('\n', ' ')
    file_object.close()
    return out_file

def normalstring(file_document):
    pos = 0
    language_nab = ""
    while pos < len(file_document):
        if file_document[pos] == "<":
            temp = "<"
            while file_document[pos] <> ">":
                temp += file_document[pos]
                pos += 1
        else:
            language_nab +=  file_document[pos]
            pos += 1



    split_language = language_nab.split()
    
    wordlist = []
    for word in split_language:
        for char in word:
            if char in string.punctuation:  #to remove punctuation marks  
                word = word.replace(char, '')
            
        word = str(word).lower()
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
                
    
    #Implementing the Dictionary
    total = 0
    for element in trigfreq:
        total += trigfreq[element]
        
    for element in trigfreq:
        trigfreq[element] = float(trigfreq[element])/float(total)
        #print element, trigfreq[element]

    #print "Number of Trigrams: " + str(len(trigfreq))
    #print "Total frequency of Trigrams: " + str(total)


    #sorting and pruning the dictionary
    sort_dict = sorted(trigfreq.iteritems(), key=lambda (k,v): (v,k), reverse= True)
    keep_sorted = sort_dict[0:1000]

    #for element in keep_sorted:
        #print element[0], element[1]
    
    return keep_sorted;

#lang_model("C:\Users\user\Documents\Language Identification Project\Training Files\igbo.txt")
        

