from utils import Pipeline, PreProcess, Rule, PostProcess

from pipeline.pre_process.remove_stopwords import Remove_Stopwords
from pipeline.pre_process.normalize import Normalize
from pipeline.pre_process.lemmatize import Lemmatize
from pipeline.pre_process.stem import Stem
from pipeline.pre_process.train_randomforest import Train_RandomForest
from pipeline.pre_process.train_fasttext import Train_Fasttext

from pipeline.rules.contain_funny import Contain_Funny
from pipeline.rules.contain_funny_negator import Contain_Funny_Negator
from pipeline.rules.contain_notfunny import Contain_NotFunny
from pipeline.rules.contain_notfunny_negator import Contain_NotFunny_Negator
from pipeline.rules.random_forest import RandomForest
from pipeline.rules.fast_text import Fasttext

from pipeline.post_process.report import Report
from pipeline.post_process.visualize import Visualize

# TEXT -----input---> PIPELINE {[RULE1] ---> [RULE2] ---> [RULE3]} ---output--->  {RULE1, RULE2, RULE3}

if __name__ == '__main__': 
    config = {
        'datafile': 'testingdata_copy.txt', #IMPORTANT: if you want to use trained random forest or fasttext with naive rules, MUST USE 'testingdata_copy.txt'. If you want to train a new random forest or fasttext model, MUST USE 'traintest.txt'
        'interactive_mode': True, 
        'preprocess': [ #IMPORTANT: essential preprocess (noise removal, lowercasing) always performed
            {
                'name': 'remove_stopwords',
                'enabled': True, 
                'obj': Remove_Stopwords(),
                'metadata': {
                    'show_effect': True #IMPORTANT: set to True ONLY in interactive mode
                }
            },
            {
                'name': 'normalize',
                'enabled': False, #Do not enable, not yet implemented
                'obj': Normalize()  #TODO: implement
            },
            {
                'name': 'stem',
                'enabled': False,
                'obj': Stem(),
                'metadata': {
                    'show_effect': False #IMPORTANT: set to True ONLY in interactive mode
                }
            },
            {   
                'name': 'lemmatize',
                'enabled': True,
                'obj': Lemmatize(),
                'metadata': {
                    'show_effect': True #IMPORTANT: set to True ONLY in interactive mode
                }
            },
            {
                'name': 'train_randomforest',
                'enabled': False, #IMPORTANT: training takes hours
                'obj': Train_RandomForest()
            },
            { 
                'name': 'train_fasttext',
                'enabled': False, #Recommend setting 'enabled' to True and training your own fasttext model. Do NOT recommend changing test_size, but feel free to play around with the other hyperparameters. If you enable train_fasttext or train_randomforest, set 'datafile' to 'traintest.txt' 
                'obj': Train_Fasttext(),
                'metadata': {
                    'test_size': 0.2,
                    'lr': 0.75,
                    'epoch': 20,
                    'wordNgrams': 2,
                    'loss': 'hs'
                }
            }
        ],
        'rules': {
            'r1': {
                'enabled': True,
                'dependencies': [],
                'obj': Contain_Funny(),
                'weight': 0.333, #feel free to change weights!
                'metadata': {
                    'humorwords': True, 
                    'humorphrases': {
                        'enabled': True,
                        'strict': False #only uses specific humor phrases of length 4&5
                    },
                    'show_humorword_or_humorphrase': True #IMPORTANT: set to False if not in interactive mode
                }
            },
            'r2': {
                'enabled': False, #Do NOT recommend enabling - poor performance
                'dependencies': [],
                'obj': Contain_NotFunny(),
                'weight': 0
            },
            'r3': {
                'enabled': False, #Do NOT recommend enabling - poor performance
                'dependencies': ['r1'],
                'obj': Contain_Funny_Negator(),
                'weight': 0
            },
            'r4': {
                'enabled': False, #Do NOT recommend enabling - poor performance
                'dependencies': ['r2'],
                'obj': Contain_NotFunny_Negator(),
                'weight': 0
            },
            'r5': {
                'enabled': True,
                'dependencies': [],
                'obj': RandomForest(),
                'weight': 0.333,
                'metadata': {
                    'modelID': '1'
                }
            },
            'r6': {
                'enabled': True,
                'dependencies': [],
                'obj': Fasttext(),
                'weight': 0.333,
                'metadata': {
                    'modelID': '1' #IMPORTANT: This tells the model which fasttext model you want to test on (default is one just trained as a preprocessing stage). If you want to use a pretrained fasttext model, you can set modelID to the modelID of the model you want to use and thus don't have to retrain a fasttext model
                }
            }
        },
        'postprocess': {
            'report': {
                'enabled': True,
                'obj': Report(),
                'metadata': {
                    'metrics': [], #IMPORTANT: if not in interactive mode, SET TO ['accuracy','precision', 'recall', 'f1', 'cm']
                    'return_pred': True, #IMPORTANT: if not in interactive mode, SET TO False
                    'average': True, #uses weights to use all enabled rules together
                    'save': False, #saves report to csv
                }
            }, 
            'visualize': {
                'enabled': False,
                'obj': Visualize(),
                'metadata': {
                    'normalize': False, #if you want a normalized confusion matrix, set to True
                    'save': False #if you enable 'visualize', recommend setting 'save' to True
                }
            }

        }
    }

    #pass into Pipeline class run function
    p = Pipeline(config)
    p.run()



