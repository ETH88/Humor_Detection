import nltk
from utils import PreProcess

class Train_Fasttext(PreProcess):
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
            with open('fast_text/modelid.txt', 'r') as modelid_file:
                modelid = int(modelid_file.read())+1

            with open('fast_text/modelID_dict.json', 'r') as config_dictionary_file:
                master_dict = json.load(config_dictionary_file) #loads dictionary into master_dict 
                # ex of master_dict --> {"1": "{strid1}.pkl", "2": {strid2}.pkl}

        except Exception as e: #cold start, json file not initialized, initialize empty master_dict
            master_dict = {} #dictionary containing all key value pairs for modelID_dict.json
            modelid = 1
            pass

        with open(f'fast_text/modelid.txt', 'w') as modelid_file:
            modelid_file.write(str(modelid))

        X = [row[1] for row in data]
        y = [int(row[0]) for row in data]

        import uuid
        strid = uuid.uuid1()
        with open(f"fast_text/data/alldata_{strid}.txt", 'w') as data_file: #saving data to txt file in /data folder
            for i in range(len(X)):
                data_file.write(f'{i},{y[i]},a,{X[i]}\n')

        test_size = self._metadata['test_size']
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        with open(f'fast_text/data/testingdata_{strid}.txt', 'w') as data_file:
            for i in range(len(X_test)):
                data_file.write(f'{i},{y_test[i]},a,{X_test[i]}\n')

        lr = self._metadata['lr']
        epoch = self._metadata['epoch']
        wordNgrams = self._metadata['wordNgrams']
        loss = self._metadata['loss']
        hyper_params = {'lr': lr, 'epoch': epoch, 'wordNgrams': wordNgrams, 'loss': loss} 

        with open(f'fast_text/data/trainingdata_{strid}.txt', 'w') as humor_file:
            for i in range(len(X_train)):
                humor_file.write(f'__label__{y_train[i]} {X_train[i]}\n')

        import fasttext
        model = fasttext.train_supervised(input=f'fast_text/data/trainingdata_{strid}.txt', **hyper_params)
        
        model.save_model(f"fast_text/models/{strid}.bin")

        master_dict[modelid] = f"{strid}.bin" 

        #second file: contains dictionary w key=modelID -> value=name of pkl file
        with open('fast_text/modelID_dict.json', 'w') as config_dictionary_file: #second file=modelID_dict.pkl (overwriting file)
            json.dump(master_dict, config_dictionary_file)

        return {}
        