if __name__ == '__main__':
    import nltk
    import numpy as np
    from matplotlib import pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    import forestci as fci
    from sklearn.datasets import make_classification

    data = []
    with open("traintest_lemmatized_copy.txt", 'r') as data_file: #traintest_lemmatized_copy#getting data
        for line in data_file:
            temp = line[:-1].split(",")
            data.append([temp[1], temp[3]])

    import uuid
    import pickle
    #writing original text to file 
    strid = uuid.uuid1()

    X = [row[1] for row in data]
    y = [int(row[0]) for row in data]

    with open('alldata.txt', 'w') as data_file:
        for i in range(len(X)):
            data_file.write(f'{y[i]},{X[i]}\n')

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print('split done')

    

    with open('testingdata.txt', 'w') as data_file:
        for i in range(len(X_test)):
            data_file.write(f'{y_test[i]},{X_test[i]}\n')
    
    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
    tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7) #
    #TODO: test increasing max_features
    #tfidfconverter = CountVectorizer(max_features=1500)

    tfidf = tfidfconverter.fit(X_train)
    print('tfidf done')

    #dumping tfidf to pickle file - tfidf model needed when testing
    with open(f"tfidf_{strid}.pkl", 'wb') as config_dictionary_file: #first files = {name}_{strid}.pkl
        pickle.dump(tfidf, config_dictionary_file)
    
    X_train = tfidf.transform(X_train).toarray()
    from sklearn.ensemble import RandomForestClassifier #RANDOM FOREST TREE
    clf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    print('fitting done')

    #first file: pkl files w models, change directory
    with open(f"rf_{strid}.pkl", 'wb') as config_dictionary_file: #first files = {name}_{strid}.pkl
        pickle.dump(clf, config_dictionary_file)

    X_test = tfidf.transform(X_test).toarray()
    
    pred = clf.predict(X_test)
    print('pred done')

    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y_test, pred) 
    from sklearn.metrics import precision_score
    precision = precision_score(y_test, pred)
    from sklearn.metrics import recall_score
    recall = recall_score(y_test, pred)
    from sklearn.metrics import f1_score
    f1 = f1_score(y_test, pred)
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, pred, labels=[1,0]) 

    output = {}
    output['results'] = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'confusion_matrix': cm,
    }
    print(output)