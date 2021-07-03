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
    'Well':['RB'], #interjection
    'know':['VBP'],
    'what':['WP'], 
    'i':['NN', '1st', 'name that call myself'], 
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
    'your':['PRP$'], 
    'lesson':['NN'],

    ##6th sentence
    'survived':['VBD'],
    'everything':['NN'], 
    'hurting':['VBG'],
    'now':['RB'], 
    'It':['PRP'],
    'over':['IN'],
    '4':['CD'], 
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
    'will':['MD'], 
    'a':['DT'],
    'better':['JJR'], 
    'day':['NN'],
    
    }

emo_dic={
    ':(':['EMOTI','sad'],
    ';)':['EMOTI','twinkle'] 
    } 

punc=['.',',','!','?']
punc_dic={
    '.':['.','end'],
    ',':[',','punc'],
    '!':['!','exclamation mark'],
    '?':['?','question'],
    '...':['...','etc']
    }

emoji_dic = {
    '\U0001F44F':['EMOJI','clap'],
    '\U0001F648':['EMOJI','see-no-evil monkey'], 
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

### Penn treebank ###

phrase_dic={
    'NP':[('JJR','NN'),('WP','VP'),('DT','NP'),('EMOJI','NN'),('PRP$','NP')],
    'VP':[
        ('VBP','JJ'),('VBG','RB'),('VBP','NP'),('VP','VP'),('NN','VP'),('RB','VP'),('RB','VBN'),('MD','VB'),
        ('PRP','VBP'),('PRP','VP'),('VP','VBN'),('NP','VBN'),('VBP','NN')
        ],
    'PP':[('IN','NP')],
    'S':[('UH','!'),('VP','!')]
    }

def phrase(tags):
    anal =[]
    ref_tags = tags[:]
    for i in range(len(ref_tags)):
        try:
            now = ref_tags[i]
            nxt = ref_tags[i+1]
    
            if (now,nxt) in phrase_dic['VP']:
                anal.insert(i,'VP')
                ref_tags.pop(i)
            elif (now,nxt) in phrase_dic['NP']:
                anal.insert(i,'NP')
                ref_tags.pop(i)
            elif now != '!' and now != '.' and (now,nxt) == (now,'VP'):
                anal.insert(i,'VP')
                ref_tags.pop(i)
            else:
                anal.insert(i,now)
    
        except IndexError:
            anal.insert(i,now)
            break
    
    return anal

def semi_fini(tagg):
    anal =[]
    ref_tags = tagg[:]
    for i in range(len(tagg)):
        try: 
            now = ref_tags[i]
            nxt = ref_tags[i+1]

            if (now,nxt) == ('VP','.'):
                anal.insert(i,'S')
                ref_tags.pop(i)
            elif (now,nxt) == ('VP','!'):
                anal.insert(i,'S')
                ref_tags.pop(i)
            elif (now,nxt) == ('UH','!'):
                anal.insert(i,'S')
                ref_tags.pop(i)
            elif (now,nxt) == ('VP','?'):
                anal.insert(i,'S')
                ref_tags.pop(i)
        except IndexError:
            anal.insert(i,now)
            break
    
    return anal

def fini(semi):
    fin_result = True
    try:
        while semi:
            if semi.pop() == 'S':
                continue
            elif semi.pop() == 'EMOTI':
                continue
            elif semi.pop() == 'EMOJI':
                continue
            else:
                fin_result = False
                break
    except IndexError:
        return fin_result
            
    return fin_result

def re_phra(list):
    aaa = phrase(list)
    bbb = phrase(aaa)
    resulta = True
    if aaa == bbb:
        smi = semi_fini(bbb)
        resulta = fini(smi)        

    elif aaa != bbb:
        re_phra(bbb)
        
    return resulta

h = re_phra(tag)
#----------------------------------------------------------------------------------
print('Tokenization:',result1)
print('Tagging: ',tag)
if h == True:
    print('No Syntactic Error')
else:
    print('There is Syntactic Error')