import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
data = []
with open("traintest_copy.txt", 'r') as data_file:
    for line in data_file:
        temp = line[:-1].split(",")
        data.append([temp[1], temp[3]])

X = [row[1] for row in data]
y = [int(row[0]) for row in data]

# Creating the bag of Word Model
from sklearn.feature_extraction.text import CountVectorizer
c_v = CountVectorizer(max_features = 5000, stop_words=stopwords.words('english'))
X = c_v.fit_transform(X).toarray()

#TODO: test below
'''
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()

from sklearn.feature_extraction.text import TfidfTransformer
tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()'''

from sklearn.ensemble import RandomForestClassifier #RANDOM FOREST TREE
clf = RandomForestClassifier()

from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

scoring = ['accuracy', 'precision', 'recall', 'f1']
scores = cross_validate(clf, X, y, scoring=scoring, cv=5) #stratified kfold, 80:20 split
#TODO: test later

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
y_pred = cross_val_predict(clf, X, y, cv=5)
cm = confusion_matrix(y, y_pred)

output = {}

output['results'] = {
    'accuracy': list(scores['test_accuracy']),
    'precision': list(scores['test_precision']),
    'recall': list(scores['test_recall']),
    'f1': list(scores['test_f1']),
    'confusion_matrix': cm,
}

print(output)