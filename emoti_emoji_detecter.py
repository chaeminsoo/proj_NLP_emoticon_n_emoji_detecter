import re

eng_dic={
    'I':['NN', '1st', 'name that call myself'],
    'am':['VBP', '1st', 'be verb for I'],
    'sorry':['JJ'],
    'you':[1],
    'are':[1],
    'not':[1],
    'feeling':[1],
    'well':[1]
    }
emo_dic={':(':'sad'}
punc=['.',',','!','?']
anayl=[]

word_sign = re.compile(r'\S+')
word_w_punc = re.compile(r'\S+[.]')

result1 = word_sign.findall('I am sorry you are not feeling well. :(')
result2 = word_w_punc.findall('I am sorry you are not feeling well. :(')

def slice(word):
    for i in range(len(word)):
        if word[len(word)-1-i] in punc:
            continue
        else:
            ind = len(word)-1-i
            break
    return [word[:ind+1], word[ind+1:]]

        

# result1 = word_sign.findall('I am sorry you are not feeling well... :(')
# result2 = word_w_punc.findall('I am sorry you are not feeling well... :(')

if result2[0] in result1:
    result1[result1.index(result2[0])] 

for element in result1:
    try:
        if eng_dic[element]:
            anayl.append(eng_dic[element])
    except KeyError:
        try:
            if emo_dic[element]:
                anayl.append(emo_dic[element])
        except KeyError:
            anayl.append('not found')

print(result1)
print(result2)
print(anayl)