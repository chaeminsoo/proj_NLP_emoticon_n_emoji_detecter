import re

### dic ###

eng_dic={
    'I':['PRP', '1st', 'name that call myself'],
    'am':['VBP', '1st', 'be verb for I'],
    'sorry':['JJ'],
    'you':['NN', '2nd'],
    'are':['VBP','2nd','be verb for you'],
    'not':['JJ'],
    'feeling':['VBG'],
    'well':['RB'],

    ##2nd sentence
    'Well':['UH'], #interjection으로 사용
    'know':['VBP'],
    'what':['WP'], #관계대명사 이게 맞는 지 의문
    'i':['NN', '1st', 'name that call myself'], #소문자
    'mean':['VBP'],

    ##3rd sentence
    'Congratulations':['UH'],
    'done':['VBN'],

    ##4th sentence
    'for':['IN'],
    'really':['RB'],
    'have':['VBP'],
    'Have':['VBP'],

    ##5th sentence
    'fun':['NN'],
    'during':['IN'],
    'your':['PRP$'], #프린터에 이렇게 적혀있다.
    'lesson':['NN'],

    ##6th sentence
    'survived':['VBD'],
    'everything':['NN'], #원래는 total pronoun인데 프린터에는 NN으로 되어있다.
    'hurting':['VBG'],
    'now':['RB'], 
    'It':['PRP'],
    'over':['IN'],
    '4':['CD'], ## 이 부분은 따로 정리할 필요가 있을 듯 합니다.
    'hours':["NNS"],
    'but':['CC'],
    'is':['VBZ'],
    'took':['VBD'],

    ##7th sentence
    'Auts':['UH'],
    'be':['VB'],
    'bet':['VBP'],
    'that':['IN'],
    'tomorrow':['RB'],
    'will':['MD'], #조동사
    'a':['DT'],
    'better':['JJR'], #저는 JJ보다는 JJR이라고 생각합니다.
    'day':['NN'],
    #'...':['PUNC'] ##이것은 나중에 PUNC으로 넣어야 할 것 같습니다.

    ##위에 있는 것들을 아직 어떻게 분류해야할 지 정하지 않아서, 일단은 문장별로 분류했습니다. 
    ## 1)나중에 이것들을 아래와 같이 pos별로 분류할 지 정해야 할 것 같고,
    ## 2)pos말고도 어떤 feature를 넣어야 할 지 정해야 할 것 같습니다.

    }

emo_dic={
    ':(':['EMOTI','sad'],
    ';)':['EMOTI','twinkle'] ##unicode 나와 있는 내용을 따랐습니다.
    } 

punc=['.',',','!','?']
punc_dic={
    '.':['PUNC','end'],
    ',':['PUNC','punc'],
    '!':['PUNC','exclamation mark'],
    '?':['PUNC','question'],
    '...':['PUNC','etc']
    }

emoji_dic = {
    '\U0001F44F':['EMOJI','clap'],
    '\U0001F648':['EMOJI','see-no-evil monkey'], ##unicode 나와 있는 내용을 따랐습니다.
    '\U0001F3B7':['EMOJI','saxophone'],
    '\U0001F631':['EMOJI','face screaming in fear'],
    '\U0001F62B':['EMOJI','tired face'],
    '\U0001F60D':['EMOJI','smiling face with heart-shaped eyes']
}
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

tag=[]

for element in result1:
    try:
        if eng_dic[element]:
            tag.append(eng_dic[element][0])
    except KeyError:
        try:
            if emo_dic[element]:
                tag.append(emo_dic[element][0])
        except KeyError:
            try:
                if punc_dic[element]:
                    tag.append(punc_dic[element][0])
            except KeyError:
                try:
                    if emoji_dic[element]:
                        tag.append(emoji_dic[element][0])
                except KeyError:
                    tag.append('not found')

#-----------------------------------------------------------------------------------

print('Tokenization:',result1)
#print(result2)
print('Tagging: ',tag)
