humorwords = []
nothumorwords = []
negators = []
with open('humorwords.txt', 'r') as humor_file:
    humorwords = humor_file.read().split(" ")
with open('nothumorwords.txt', 'r') as nothumor_file:
    nothumorwords = nothumor_file.read().split(" ")
with open('negators.txt', 'r') as negators_file:
    negators = negators_file.read().split(" ")

output = {}
#1: 1st rule - contains funny word?
#2: 2nd rule - contains not funny word?
#3: 3rd rule - contains funny word + negator?
#4: 4th rule - contains not funny word + negator?
#5: 5th rule - weighted average of first 4

#makes sure negator only applies to funny/not funny word right after it

#0 is neutral
#-1 if not funny
#1 is funny

def rules(rule1 = False, rule2 = False, rule3 = False, rule4 = False, rule5 = False):
    output = {}
    isfunny = False
    isnotfunny = False
    isnegator = False
    if rule1:
        for word in sentence:
            if word in humorwords and not isfunny: #funny word
                output['Rule 1'] = 1 
                isfunny = True
        if not isfunny: #no funny words
            output['Rule 1'] = -1
    if rule2:
        for word in sentence:
            if word in nothumorwords and not isnotfunny: #funny word
                output['Rule 2'] = -1
                isnotfunny = True
        if not isnotfunny: #no funny words
            output['Rule 2'] = 1
    if rule3:
        if rule1:
            isfunny = False
            isnegator = False
            for word in sentence:
                if word in humorwords and not isfunny: #funny word
                    output['Rule 1'] = 1 
                    isfunny = True
                    if isnegator:
                        output['Rule 3'] = opposite(output['Rule 1'])
                        isnegator = False #could be more negators
                elif word in negators and not isnegator: #negator
                    isnegator = True
            if not isfunny: #no funny words
                output['Rule 1'] = -1

            #if no negator should be same as before
            if 'Rule 3' not in output.keys():
                output['Rule 3'] = output['Rule 1']
        else:
            output['Rule 3'] = 'error: rule 1 needs to be true'

    if rule4:
        if rule2:
            isnotfunny = False
            isnegator = False
            for word in sentence:
                if word in nothumorwords and not isnotfunny: #not funny word
                    output['Rule 2'] = -1
                    isnotfunny = True
                    if isnegator:
                        output['Rule 4'] = opposite(output['Rule 2'])
                        isnegator = False
                elif word in negators and not isnegator: #negator
                    isnegator = True
            if not isnotfunny: #no not funny words
                output['Rule 2'] = 1

            #if no negator should be same as before
            if 'Rule 4' not in output.keys():
                output['Rule 4'] = output['Rule 2']
        else:
            output['Rule 4'] = 'error: rule 2 needs to be true'

    if rule5:
        if rule1 and rule2 and rule3 and rule4:
            sum = 0
            for i in range(1,len(output)+1):
                sum += output[f'Rule {i}']
            output['Rule 5'] = sum/(len(output))
        else:
            output['Rule 5'] = 'error: rule 1-4 need to be true'

    return output


def opposite(funny: int):
    if (funny == 1):
        return -1
    else:
        return 1

if __name__ == '__main__':
    while True:
        sentence = input("Type a sentence: ").split(" ")
        if (sentence[0] == 'exit'):
            break
        else:
            print(rules(True, True, False, False, False))
   #app.run(debug = True, host='0.0.0.0')
