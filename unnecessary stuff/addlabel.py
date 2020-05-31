data = []
with open("traintest_copy.txt", 'r') as data_file:
    for line in data_file:
        temp = line[:-1].split(",")
        label = '__label__'
        data.append(f'{label+temp[1]} {temp[3]}')
with open("traintest_labels.txt", 'w') as data_file:
    for item in data:
        data_file.write('%s\n' % item)
'''
data = []
with open("traintest_labels_preprocessed.txt", 'r') as data_file:
    for line in data_file:
        temp = line[:-1]
        data.append(f'{temp[0:10]} {temp[13:-2]}')
print(data[0])

with open("traintest_labels_preprocessed_new.txt", 'w') as data_file:
    for line in data:
        data_file.write(f'{line[0:10]} {line[11:]}\n')


data = []
with open('traintest_copy.txt', 'r') as data_file:
    for line in data_file:
        temp = line[:-1].split(",")
        data.append([temp[1], temp[3]])

with open('traintestt.txt', 'w') as data_file:
    for line in data:
        data_file.write(f'{line[0]},{line[1]}\n')
'''