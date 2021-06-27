import re

### dic ###

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
punc_dic={'.':'end',',':'punc','!':'exclamation mark','?':'question','...':'etc'}

emoji_dic = {'\U0001F44F':'clap'}
#---------------------------------------------------------------------------------------

### tokenization ###

word_sign = re.compile(r'\S+')
word_w_punc = re.compile(r'\S+[.]|\S+[!]|\S+[,]|\S+[?]')

def slice(word):
    for i in range(len(word)):
        if word[len(word)-1-i] in punc:
            continue
        else:
            ind = len(word)-1-i
            break
    return [word[:ind+1], word[ind+1:]]

input_sent = input('Enter a sentence:')

# result1 = word_sign.findall('I am sorry you are not feeling well. :(')
# result2 = word_w_punc.findall('I am sorry you are not feeling well. :(')

# result1 = word_sign.findall('I am sorry you are not feeling well... :(')
# result2 = word_w_punc.findall('I am sorry you are not feeling well... :(')

result1 = word_sign.findall(input_sent)
result2 = word_w_punc.findall(input_sent)

for i in result2:
    if i in result1:
        location = result1.index(i)
        a = len(slice(result1[location]))
        chaged = slice(result1[location])
        result1[location:location+1] = chaged
    else:
        continue

#----------------------------------------------------------------------------------------

##### start analyse #####

anayl=[]

for element in result1:
    try:
        if eng_dic[element]:
            anayl.append(eng_dic[element])
    except KeyError:
        try:
            if emo_dic[element]:
                anayl.append(emo_dic[element])
        except KeyError:
            try:
                if punc_dic[element]:
                    anayl.append(punc_dic[element])
            except KeyError:
                try:
                    if emoji_dic[element]:
                        anayl.append(emoji_dic[element])
                except KeyError:
                    anayl.append('not found')

#-----------------------------------------------------------------------------------

print(result1)
print(result2)
print(anayl)
