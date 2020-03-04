import Project_code
import math

yoruba_data = Project_code.normalstring(Project_code.lang_model("yoruba.txt"))
igbo_data = Project_code.normalstring(Project_code.lang_model("igbo.txt"))
hausa_data = Project_code.normalstring(Project_code.lang_model("hausa.txt"))

Language_Lists = [yoruba_data, igbo_data, hausa_data]
# print Language_Lists

def compare(test_file):
    #test_data = Project_code.lang_model(test_file)
    # print("CURRENT_LOG",test_file)
    test_data = Project_code.normalstring(test_file)
    #for element in test_data:
        #print element
    # print test_data

    result = [0,0,0]
    for index,language in enumerate(Language_Lists):
        for ngram,prob in language:
            for ng,pb in test_data:
                if ngram == ng:
                    sim = float((prob * float(math.log(pb))) + (pb * float(math.log(prob))))
                    result[index]+=sim        

                    # print sim
                    print ngram
                    print pb   
                    # print prob      
                    # print ng
                    print result


    if result[0] < result[1] and result[0] < result[2]:
        print "Language is Yoruba"
    elif result[1] < result[0] and result[1] < result[2]:
        print "Language is Igbo"
    elif result[2] < result[0] and result[2] < result[1]:
        print "Language is Hausa"
    else:
        print "Not in database"

# compare("Mo n lo si oko")
compare("Gini ka i chere Ojiugo kwesiri ime ugbu a nwatakiri nwoke")
# compare("Yadda muke wa mutane magana yana da muhimmanci sosai")

    
        
            

