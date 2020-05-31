from utils import Rule

class RandomForest(Rule):
    """
    5th rule - Random Forest Classifier
    """
    def __init__(self):
        self._enabled = False
        self._weight = 0
        self._metadata = {}

    def __repr__(self):
        return self.__class__.__name__ 
    
    def execute(self, s): 
        modelid = 1
        master_dict = {}

        import json
        with open('randomforest/modelid.txt', 'r') as modelid_file:
            modelid = modelid_file.read()

        with open('randomforest/modelID_dict.json', 'r') as config_dictionary_file:
            master_dict = json.load(config_dictionary_file) #loads dictionary into master_dict 
            # ex of master_dict --> {"1": "{strid1}.pkl", "2": {strid2}.pkl}

        if 'modelID' in self._metadata.keys(): #if modelID provided test on that one, else just test on model just trained
            modelid = self._metadata['modelID']
        #print(modelid)

        X_test = []
        y_test = []
        if s._interactive == False:
            with open(f'randomforest/data/testingdata_{master_dict[modelid].replace(".pkl", ".txt")}', 'r') as data_file:
                for line in data_file:
                    currentPlace = line[:-1].split(",")
                    y_test.append(currentPlace[1])
                    X_test.append(currentPlace[3])
        else: #interactive mode
            y_test.append(s._data[0][0])
            X_test.append(s._data[0][1])
        #TODO: read y_text in report.py, not here
        

        tfidf = ""
        import pickle
        with open(f'randomforest/models/tfidf_{master_dict[modelid]}', 'rb') as f: #0 indexed
            tfidf = pickle.load(f) #clf is Random Forest Classifier model

        clf = ""
        with open(f'randomforest/models/rf_{master_dict[modelid]}', 'rb') as f: #0 indexed
            clf = pickle.load(f) #clf is Random Forest Classifier model

        X_test = tfidf.transform(X_test).toarray()

        y_pred = clf.predict(X_test)
        
        y_pred = [int(item) for item in y_pred]
        y_test = [int(item) for item in y_test]

        return [y_pred, y_test]


        ''' works with Docker Flask app - too slow, connection error
        modelID = s._modelID
        
        if 'modelID' in self._metadata.keys(): #if modelID provided test on that one, else just test on model just trained
            modelID = self._metadata['modelID']
        print(modelID)

        import requests
        #TODO: url change action to predict
        url = f'http://localhost:5000/models/{modelID}?actions=predict'
        request_data = {
            "name": "humordata",
            "data": {
                "feature_names": ["sentence"],
                "y": "humor_label",
                "rows": [] #TODO: remove
            }
        }

        x = requests.get(url, json=request_data).json()
        #print(x['actions'])  


        #TODO: time
        import time, json
        start_time = time.time()
        x = {}
        
        while True:
            try:
                #print('trying')
                x = requests.get(url, json = request_data).json()#json.loads(requests.get(url).content)
                break
            except Exception as e:
                #print(e)
                if time.time() > start_time + 10000:
                    print('timeout')
                    raise Exception('Unable to get updates after {} seconds of ConnectionErrors'.format(10000))
                else:
                    print(e)
                    print('sleeping')
                    time.sleep(10) # attempting once every second
        
        #print(x['actions']['predict'])
        return [x['actions']['predict']['predictions'], x['actions']['predict']['actual y']]
        '''

