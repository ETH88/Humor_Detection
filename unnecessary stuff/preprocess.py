def get_wordnet_pos(word: str):
    """Map POS tag to first character lemmatize() accepts"""
    from nltk.corpus import wordnet
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

if __name__ == '__main__':
    import nltk
    
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    data = []
    with open("traintest_stopwords_removed_copy.txt", 'r') as data_file: #getting data
        for line in data_file:
            temp = line[:-1].split(",")
            data.append([temp[1], temp[3]])

    '''
    with open('traintest.txt', 'w') as data_file:
        for index, line in enumerate(data):
            data_file.write(f"{index},{line[0]},a,{line[1]}\n") #TODO: run again with just this

    import re
    #essential preprocess - lowercase,noise removal
    for i in range(len(data)):
        temp = data[i][1]
        temp = re.sub('[^a-zA-Z]',' ',temp) 
        temp = ' '.join(temp.split()) #remove extra whitespace
        words = temp.split(" ")

        review = [word.lower() for word in words if not word == ""]
        review = ' '.join(review)
        data[i][1] = review
    print('essential preprocess done')
    #print(data)

    with open('traintest_essentialpreprocessed.txt', 'w') as data_file:
        for index, line in enumerate(data):
            data_file.write(f"{index},{line[0]},a,{line[1]}\n")

    for i in range(len(data)):
        review = [word for word in data[i][1].split(" ") if not word in set(stopwords.words('english')) and not word == ""] #everythings thats not empty string or stopword
        review = ' '.join(review) #makes it a str
        data[i][1] = review
    print('stopwords done')
    #print(data)

    with open('traintest_stopwords_removed.txt', 'w') as data_file:
        for index, line in enumerate(data):
            data_file.write(f"{index},{line[0]},a,{line[1]}\n")

    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    from nltk.stem import WordNetLemmatizer 
    lemmatizer = WordNetLemmatizer()
    for i in range(len(data)): #lemmatizing
        review = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in nltk.word_tokenize(data[i][1]) if not word == ""]#lemmatizes everything based on part-of-speech if word is not empty str
        data[i][1] = ' '.join(review)
    print('lemmatizing done')
    
    #print(data)
    
    
    with open('traintest_lemmatized.txt', 'w') as data_file:
        for index, line in enumerate(data):
            data_file.write(f"{index},{line[0]},a,{line[1]}\n")
    '''

    from nltk.stem import PorterStemmer

    ps = PorterStemmer()
    for i in range(len(data)):
        words = data[i][1].split(" ")
        review  = []
        for word in words:
            if not word == "":
                review.append(ps.stem(word)) #stems word if it is not empty string
        review = ' '.join(review)
        data[i][1] = review


    with open('traintest_stemmed.txt', 'w') as data_file:
        for index, line in enumerate(data):
            data_file.write(f"{index},{line[0]},a,{line[1]}\n")
