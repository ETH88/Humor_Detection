# def get_wordnet_pos(word: str):
#     """Map POS tag to first character lemmatize() accepts"""
#     from nltk.corpus import wordnet
#     tag = nltk.pos_tag([word])[0][1][0].upper()
#     tag_dict = {"J": wordnet.ADJ,
#                 "N": wordnet.NOUN,
#                 "V": wordnet.VERB,
#                 "R": wordnet.ADV}

#     return tag_dict.get(tag, wordnet.NOUN)

# if __name__ == '__main__':
#     data = []
#     humordata = []
#     nothumordata = []
#     y = []
#     with open('traintest_copy.txt', 'r') as data_file:
#         for line in data_file:
#             remove linebreak which is the last character of the string
#             entiredata = line[:-1].split(",")
#             y.append(entiredata[1])
#             data.append(entiredata[3])
#             if entiredata[1] == '1':
#                 humordata.append(entiredata[3])
#             else:
#                 nothumordata.append(entiredata[3])

#     import nltk
#     nltk.download('stopwords')
#     from nltk.corpus import stopwords

#     ##NOISE REMOVAL###
#     import re
#     for i in range(len(humordata)):
#         words = humordata[i].split(" ")
#         humordata[i] = "" 
#         for word in words:
#             if not word == "": #ignores double spaces
#                 temp = re.sub('[^a-zA-Z]','',word) 
#                 if not temp == "":
#                     Removes everything thats not letter
#                     temp = temp.lower() #lowercase
#                     humordata[i]+=f'{temp} '

    
#     for i in range(len(nothumordata)):
#         words = nothumordata[i].split(" ")
#         nothumordata[i] = "" 
#         for word in words:
#             if not word == "": #ignores double spaces
#                 temp = re.sub('[^a-zA-Z]','',word) 
#                 if not temp == "":
#                     Removes everything thats not letter
#                     temp = temp.lower() #lowercase
#                     nothumordata[i]+=f'{temp} '

#     ##LEMMATIZING###
#     nltk.download('averaged_perceptron_tagger')
#     nltk.download('punkt')
#     from nltk.stem import WordNetLemmatizer 

#     1. Init Lemmatizer
#     lemmatizer = WordNetLemmatizer()

#     for i in range(len(humordata)):
#         review = set([lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in nltk.word_tokenize(humordata[i]) if not word == ""]) #lemmatizes everything based on part-of-speech if word is not empty str
#         humordata[i] = ' '.join(review)
#     for i in range(len(nothumordata)):
#         review2 = set([lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in nltk.word_tokenize(nothumordata[i]) if not word == ""]) #lemmatizes everything based on part-of-speech if word is not empty str
#         nothumordata[i] = ' '.join(review2)

    
#     wordDict = {}
#     for line in humordata: #humordata
#         words = line.split(" ")
#         for word in words:
#             if not word in set(stopwords.words('english')):
#                 if word in wordDict: 
#                     wordDict[word] += 1
#                 else: 
#                     wordDict[word] = 1

#     wordDict2 = {}
#     for line in nothumordata: #nothumordata
#         words = line.split(" ")
#         for word in words:
#             if not word in set(stopwords.words('english')):
#                 if word in wordDict2: 
#                     wordDict2[word] += 1
#                 else: 
#                     wordDict2[word] = 1

#     import collections
#     word_counter = collections.Counter(wordDict)
#     output = []

#     fart = []
#     index = 0
#     for word, count in word_counter.most_common(50000):
#         if word in wordDict2.keys():
#             percentfunny = count/(count+wordDict2[word])
#         else:
#             percentfunny = 1
        
#         d = {'word': word, 'funny count': count, 'percent funny': percentfunny}
#         output.append(d)
#         print(output)

#     print(output)
#     from operator import itemgetter
#     sorted_output = sorted(output, key=itemgetter('percent funny'), reverse = True)

#     import pandas as pd
#     df = pd.DataFrame.from_dict(sorted_output)

#     df.to_csv(f'funnywords.csv', index = True, header=True) #saves as datafile_timestamp-report.csv
    
#     print(fart)


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
        tokens = list(ngrams(tokens, 2))
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
    

