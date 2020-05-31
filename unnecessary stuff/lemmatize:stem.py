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
    humorwords = []
    with open('nothumorwords_copy.txt', 'r') as humor_file:
        humorwords = humor_file.read().split(", ")
    
    
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    from nltk.stem import WordNetLemmatizer 

    1. Init Lemmatizer
    lemmatizer = WordNetLemmatizer()

    for i in range(len(humorwords)):
        review = set([lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in nltk.word_tokenize(humorwords[i]) if not word == ""]) #lemmatizes everything based on part-of-speech if word is not empty str
        humorwords[i] = ' '.join(review)
    '''
    from nltk.stem import PorterStemmer

    ps = PorterStemmer()
    for i in range(len(humorwords)):
        words = humorwords[i].split(" ")
        review  = []
        for word in words:
            if not word == "":
                review.append(ps.stem(word)) #stems word if it is not empty string
        review = ' '.join(review)
        humorwords[i] = review'''
    with open('humorwords_lemmatized.txt', 'w') as humor_file:
        for item in humorwords:
            humor_file.write(f'{item}, ')
    
