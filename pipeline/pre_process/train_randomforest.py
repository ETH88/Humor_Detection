import nltk
from utils import PreProcess

class Train_RandomForest(PreProcess):
    """
    Pre-processing rule - training random forest model
    """

    def __init__(self):
        self._enabled = False

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def apply(self, data: list):
        modelid = 1
        master_dict = {}

        import json
        try: #warm start
            with open('randomforest/modelid.txt', 'r') as modelid_file:
                modelid = int(modelid_file.read())+1

            with open('randomforest/modelID_dict.json', 'r') as config_dictionary_file:
                master_dict = json.load(config_dictionary_file) #loads dictionary into master_dict 
                # ex of master_dict --> {"1": "{strid1}.pkl", "2": {strid2}.pkl}

        except Exception as e: #cold start, json file not initialized, initialize empty master_dict
            master_dict = {} #dictionary containing all key value pairs for modelID_dict.json
            modelid = 1
            pass

        with open(f'randomforest/modelid.txt', 'w') as modelid_file:
            modelid_file.write(str(modelid))

        X = [row[1] for row in data]
        y = [int(row[0]) for row in data]

        import uuid
        strid = uuid.uuid1()
        with open(f"randomforest/data/alldata_{strid}.txt", 'w') as data_file: #saving data to txt file in /data folder
            for i in range(len(X)):
                data_file.write(f'{i},{y[i]},a,{X[i]}\n')

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        
        with open(f'randomforest/data/testingdata_{strid}.txt', 'w') as data_file:
            for i in range(len(X_test)):
                data_file.write(f'{i},{y_test[i]},a,{X_test[i]}\n')

        from sklearn.feature_extraction.text import TfidfVectorizer
        tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7)

        tfidf = tfidfconverter.fit(X_train)

        import pickle
        #dumping tfidf to pickle file - tfidf model needed when testing
        with open(f"randomforest/models/tfidf_{strid}.pkl", 'wb') as config_dictionary_file: 
            pickle.dump(tfidf, config_dictionary_file)
        
        X_train = tfidf.transform(X_train).toarray()
        print('tfidf done')

        from sklearn.ensemble import RandomForestClassifier #RANDOM FOREST TREE
        clf = RandomForestClassifier().fit(X_train, y_train)
        print('fitting done')       
        
        #first file: pkl files w models, change directory
        with open(f"randomforest/models/rf_{strid}.pkl", 'wb') as config_dictionary_file: #first files = {name}_{strid}.pkl
            pickle.dump(clf, config_dictionary_file)
        
        master_dict[modelid] = f"{strid}.pkl" 

        #second file: contains dictionary w key=modelID -> value=name of pkl file
        with open('randomforest/modelID_dict.json', 'w') as config_dictionary_file: #second file=modelID_dict.pkl (overwriting file)
            json.dump(master_dict, config_dictionary_file)

        return {}


        
        '''
        Docker connection error
        import requests
        url = 'http://localhost:5000/models?actions=train'
        request_data = {
            "name": "humordata",
            "data": {
                "feature_names": ["sentence"],
                "y": "humor_label",
                "rows": data
            }
        }
    
        output = requests.post(url, json = request_data).json() #json= makes sure request_data is sent as json not str
        
        #print(output)
        modelID = output['modelID']
        #print(modelID)

        return modelID'''