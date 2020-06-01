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
        'datafile': 'traintest.txt', #'traintest.txt', IMPORTANT: if you want to use random forest or fasttext with naive rules, MUST USE 'testingdata_copy.txt'
        'interactive_mode': False, 
        'preprocess': [
            {
                'name': 'remove_stopwords',
                'enabled': False, 
                'obj': Remove_Stopwords()
            },
            {
                'name': 'normalize',
                'enabled': False, #Do not enable, not yet implemented
                'obj': Normalize()  #TODO: implement
            },
            {
                'name': 'stem',
                'enabled': False,
                'obj': Stem()
            },
            {   
                'name': 'lemmatize',
                'enabled': False,
                'obj': Lemmatize()
            },
            {
                'name': 'train_randomforest',
                'enabled': False, #IMPORTANT: training takes hours
                'obj': Train_RandomForest()
            },
            { 
                'name': 'train_fasttext',
                'enabled': True,
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
                'enabled': False,
                'dependencies': [],
                'obj': Contain_Funny(),
                'weight': 0.333,
                'metadata': {
                    'humorwords': True, 
                    'humorphrases': {
                        'enabled': True,
                        'strict': False #only specific phrases length 4&5
                    }
                }
            },
            'r2': {
                'enabled': False, 
                'dependencies': [],
                'obj': Contain_NotFunny(),
                'weight': 0
            },
            'r3': {
                'enabled': False,
                'dependencies': ['r1'],
                'obj': Contain_Funny_Negator(),
                'weight': 0
            },
            'r4': {
                'enabled': False,
                'dependencies': ['r2'],
                'obj': Contain_NotFunny_Negator(),
                'weight': 0
            },
            'r5': {
                'enabled': False,
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
                    #'modelID': '1' #IMPORTANT: This tells the model which fasttext model you want to test on (default is one just trained as a preprocessing stage). If you want to use a fasttext model you already trained, you can set modelID to the modelID of the model you want to use and thus don't have to retrain a fasttext model.
                }
            }
        },
        'postprocess': {
            'report': {
                'enabled': True,
                'obj': Report(),
                'metadata': {
                    'metrics': ['accuracy','precision', 'recall', 'f1', 'cm'], #IMPORTANT: in interactive mode, recommend setting to []
                    'return_pred': False, #IMPORTANT: in interactive mode, set to True
                    'average': False,
                    'save': False, 
                }
            }, 
            'visualize': {
                'enabled': False,
                'obj': Visualize(),
                'metadata': {
                    'normalize': False,
                    'save': False 
                }
            }

        }
    }

    #pass into Pipeline class run function
    p = Pipeline(config)
    p.run()



