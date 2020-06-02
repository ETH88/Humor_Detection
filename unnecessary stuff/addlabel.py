#For fasttext, data needs __label__ in front of each label. This program does that

data = []
with open("traintest_copy.txt", 'r') as data_file:
    for line in data_file:
        temp = line[:-1].split(",")
        label = '__label__'
        data.append(f'{label+temp[1]} {temp[3]}')
with open("traintest_labels.txt", 'w') as data_file:
    for item in data:
        data_file.write('%s\n' % item)
