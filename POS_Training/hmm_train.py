corpus = dict()        # Corpus of words
tags = dict()          # Corpus of tags
pos = open('./hmm_train.txt', 'r')
tag = 0
word_tag = 0
for line in pos:
    prev_tag = '<s>'
    if prev_tag in corpus:
        corpus[prev_tag] += 1         # Storing the count of <s> tag
    else:
        corpus[prev_tag] = 1
    for words in line.split():
        word,tag = words.split('/')
        next_tag = tag
        
        emmission = prev_tag + '/' + next_tag
        if emmission in corpus:       # Storing the count of previous and next tag
            corpus[emmission] += 1
        else:
            corpus[emmission] = 1
        prev_tag = next_tag
        
        if tag in corpus:           # Storing the counts of tags
            corpus[tag] += 1
        else:
            corpus[tag] = 1
            
        combination = word + '/' + tag     # Storing the combinationination of words
        if combination in corpus:
            corpus[combination] += 1
        else:
            corpus[combination] = 1
            
pos = open('./hmm_train.txt' , 'r')
for line in pos:
    prev_tag = '<s>'
    for word in line.split():
        word,tag  = word.split('/')
        next_tag = tag
        transition = prev_tag + '/' + next_tag
        if transition in corpus:                       # Computing the trasition probabilities
            prob = corpus[transition] / corpus[prev_tag] 
            print('P(',next_tag,'|',prev_tag,')',' = ',prob)
        
        temp = word + '/' + tag
        if temp in corpus:                                # Computing the emission probabilities
            prob = corpus[temp] / corpus[prev_tag]
            print('P(',word,'|',tag,')',' = ',prob)

        prev_tag = next_tag