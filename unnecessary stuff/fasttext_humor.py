import nltk

data = []

with open("traintest_labels_preprocessed.txt", 'r') as data_file: #getting data
    for line in data_file:
        temp = line[:-1]
        data.append([temp[0:10], temp[11:]])

X = [row[1] for row in data]
y = [row[0] for row in data]
print(X[0])
print('preprocess done')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42) #random_state=42
print('split done')

with open('humordata_train.txt', 'w') as humor_file:
    for i in range(len(X_train)):
        humor_file.write(f'{y_train[i]} {X_train[i]}\n')

with open('humordata_test.txt', 'w') as humor_file:
    for i in range(len(X_test)):
        humor_file.write(f'{y_test[i]} {X_test[i]}\n')
print('writing to files done')




hyper_params = {'lr': 0.75, 'epoch': 20, 'wordNgrams': 2, 'loss': 'hs'} #'loss':'hs', 'dim':20, 'wordNgrams':2


import fasttext

model = fasttext.train_supervised(input='humordata_train.txt', **hyper_params)

#model = fasttext.train_supervised(input='humordata_train.txt', lr=1.0, epoch=25, loss='hs')
print("Model trained with the hyperparameter \n {}".format(hyper_params))

#save model
#model.save_model("humorclassifier.bin")
#load_model to use

#get predictions
y_pred = []
for index, sentence in enumerate(X_test):
    x = model.predict(sentence)
    y_pred.append(int(str(x[0])[-4]))
    prob = float(x[1])

y_test = [int(label[-1]) for label in y_test]
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred) 
from sklearn.metrics import precision_score
precision = precision_score(y_test, y_pred)
from sklearn.metrics import recall_score
recall = recall_score(y_test, y_pred)
from sklearn.metrics import f1_score
f1 = f1_score(y_test, y_pred)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred, labels=[1,0]) 

output = {}
output['results'] = {
    'accuracy': accuracy,
    'precision': precision,
    'recall': recall,
    'f1': f1,
    'confusion_matrix': cm,
}
print(output)

#x = model.predict('this is funny awful sentence') #returns tuple
#ex: (('__label__1',), array([0.99385709]))
# pred = int(str(x[0])[11:12])
# prob = float(x[1])
# print(pred)
# print(prob)



# CHECK PERFORMANCE      

result = model.test("humordata_test.txt")
print(result)

