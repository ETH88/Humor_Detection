from utils import PostProcess, Rule
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Visualize(PostProcess): 
    """
    Return how well rules do
    """
    def __init__(self):
        self._enabled = False
        self._metadata = {}
        self._normalize = False
        self._save = False

    def __repr__(self):
        return self.__class__.__name__ 
    
    def apply(self, s):
        data = s._data
        d = s._pred
        rules = s._rules
        datafile = s._datafile

        self._normalize = self._metadata['normalize']
        self._save = self._metadata['save']

        y = [int(row[0]) for row in data]

        str_rules = [f'{item}' for item in rules]

        for rule in d:
            if rule == 'RandomForest' or rule == 'Fasttext': #TODO: make sure code works
                pred = [int(item) for item in d[rule][0]]
                y = [int(item) for item in d[rule][1]]
            else:
                pred = d[rule] 
            self.cm(y, pred, rules, str_rules, rule, datafile)

        return {'visualize': 'success'}

                
    def cm(self, y: list, pred: list, rules: list, str_rules: list, rule: Rule, datafile: str):
        from sklearn.metrics import confusion_matrix

        np.set_printoptions(precision=2)

        class_names = ['funny', 'not funny']
        # Plot non-normalized confusion matrix

        y = list([int(item) for item in y])
        pred = list([int(item) for item in pred])

        import time
        ts = time.gmtime()

        if self._normalize:
            # Plot normalized confusion matrix
            plot_confusion_matrix(y, pred, classes=class_names, normalize=self._normalize,title=f'Normalized confusion matrix for {rule}')
            if self._save:
                plt.savefig(f'report/{datafile}_{time.strftime("%Y-%m-%d %H:%M:%S", ts)}-cm-{rule}-normalized.png', index = True, header=True) #saves as datafile_timestamp-cm-rule-normalized.png
        
        else: #no normalize 
            plot_confusion_matrix(y, pred, classes=class_names, normalize=self._normalize,title=f'Confusion matrix for {rule} without normalization')
            if self._save:
                plt.savefig(f'report/{datafile}_{time.strftime("%Y-%m-%d %H:%M:%S", ts)}-cm-{rule}-not_normalized.png', index = True, header=True) #saves as datafile_timestamp-cm-rule-not_normalized.png


def plot_confusion_matrix(y_true, y_pred, classes, normalize=False, title=None, cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    from sklearn.utils.multiclass import unique_labels
    from sklearn.metrics import confusion_matrix

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=[1,0])
    # Only use the labels that appear in the data
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        # ... and label them with the respective list entries
        xticklabels=classes, yticklabels=classes,
        title=title,
        ylabel='True label',
        xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax
