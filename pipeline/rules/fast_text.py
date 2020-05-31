from utils import Rule
import os

class Fasttext(Rule):
    """
    2nd rule - contains notfunny word?
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
        with open('fast_text/modelid.txt', 'r') as modelid_file:
            modelid = modelid_file.read()

        if 'modelID' in self._metadata.keys(): #if modelid provided use that one
            modelid = self._metadata['modelID']

        import json
        with open('fast_text/modelID_dict.json', 'r') as config_dictionary_file:
            master_dict = json.load(config_dictionary_file) #loads dictionary into master_dict 
            # ex of master_dict --> {"1": "{strid1}.pkl", "2": {strid2}.pkl}

        X_test = []
        y_test = []
        if s._interactive == False:
            with open(f'fast_text/data/testingdata_{master_dict[modelid].replace(".bin",".txt")}', 'r') as data_file:
                for line in data_file:
                    entiredata = line[:-1].split(",")
                    y_test.append(int(entiredata[1]))
                    X_test.append(entiredata[3])
        else: #interactive mode
            y_test.append(int(s._data[0][0]))
            X_test.append(s._data[0][1]) #s._rawdata

        import fasttext
        import os
        owd = os.getcwd()
        os.chdir("fast_text/models")
        model = fasttext.load_model(f"{master_dict[modelid]}")
        os.chdir(owd)

        #get predictions
        y_pred = []
        for index, sentence in enumerate(X_test):
            x = model.predict(sentence)
            y_pred.append(int(str(x[0])[-4])) #gets prediction
            #prob = float(x[1]) #TODO: use prob!!!!
                
        return [y_pred, y_test]