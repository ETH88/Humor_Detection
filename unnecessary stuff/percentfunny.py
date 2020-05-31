if __name__ == '__main__':
    data = []
    humordata = []
    nothumordata = []
    y = []
    with open('traintest_copy.txt', 'r') as data_file: #traintest_copy.txt
        for line in data_file:
            entiredata = line[:-1].split(",")
            y.append(entiredata[1])
            data.append(entiredata[3])
            if entiredata[1] == '1':
                humordata.append(entiredata[3])
            else:
                nothumordata.append(entiredata[3])

    ##NOISE REMOVAL###
    import re
    for i in range(len(humordata)):
        words = humordata[i].split(" ")
        humordata[i] = "" 
        for word in words:
            if not word == "": #ignores double spaces
                temp = re.sub('[^a-zA-Z]','',word) 
                if not temp == "":
                    temp = temp.lower() #lowercase
                    humordata[i]+=f'{temp} '

    
    for i in range(len(nothumordata)):
        words = nothumordata[i].split(" ")
        nothumordata[i] = "" 
        for word in words:
            if not word == "": #ignores double spaces
                temp = re.sub('[^a-zA-Z]','',word) 
                if not temp == "":
                    temp = temp.lower() #lowercase
                    nothumordata[i]+=f'{temp} '

    funnyphraseDict = {}
    import nltk
    from nltk.util import ngrams
    for line in humordata: #humordata
        tokens = nltk.word_tokenize(line)
        tokens = list(ngrams(tokens, 2)) #phrases length 2
        #print(tokens)
        
        for token in tokens:
            temp = f'{token[0]} {token[1]}' 
            if temp in funnyphraseDict: 
                funnyphraseDict[temp] += 1
            else: 
                funnyphraseDict[temp] = 1

    notfunnyphraseDict = {}
    for line in nothumordata: #nothumordata
        tokens = nltk.word_tokenize(line)
        tokens = ngrams(tokens, 2)
        
        for token in tokens:
            temp = f'{token[0]} {token[1]}'
            if temp in notfunnyphraseDict: 
                notfunnyphraseDict[temp] += 1
            else: 
                notfunnyphraseDict[temp] = 1

    import collections
    word_counter = collections.Counter(funnyphraseDict)
    output = []

    index = 0
    for phrase, count in word_counter.most_common(5000):
        if phrase in notfunnyphraseDict.keys():
            percentfunny = count/(count+notfunnyphraseDict[phrase])
        else:
            percentfunny = 1
        
        d = {'phrase': phrase, 'funny count': count, 'percent funny': percentfunny}
        output.append(d)

    #print(output)
    from operator import itemgetter
    sorted_output = sorted(output, key=itemgetter('percent funny'), reverse = True)

    import pandas as pd
    df = pd.DataFrame.from_dict(sorted_output)

    df.to_csv(f'funnyphrases2.csv', index = True, header=True) #saves as datafile_timestamp-report.csv
    

