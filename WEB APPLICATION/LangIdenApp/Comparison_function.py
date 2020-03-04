#coding=utf-8
import Project_code
import math

yoruba_data = Project_code.normalstring(Project_code.lang_model("yoruba.txt"))
igbo_data = Project_code.normalstring(Project_code.lang_model("igbo.txt"))
hausa_data = Project_code.normalstring(Project_code.lang_model("hausa.txt"))

Language_Lists = [yoruba_data, igbo_data, hausa_data]


def compare(test_file):
    #test_data = Project_code.lang_model(test_file)
    # print("LOG:", yoruba_data, igbo_data, hausa_data)
    print("CURRENT_LOG",test_file)
    test_data = Project_code.normalstring(test_file)
    #for element in test_data:
        #print element
        
    result = [0,0,0]
    for index,language in enumerate(Language_Lists):
        for ngram,prob in language:
            for ng,pb in test_data:
                if ngram == ng:
                    sim = float((prob * float(math.log(pb))) + (pb * float(math.log(prob))))
                    result[index]+=sim                 
    
    if result[0] < result[1] and result[0] < result[2]:
        return " The Language is Yoruba"
    elif result[1] < result[0] and result[1] < result[2]:
        return "The Language is Igbo"
    elif result[2] < result[0] and result[2] < result[1]:
        return "The Language is Hausa"
    else:
        return "Not in database" 

    
        
            

