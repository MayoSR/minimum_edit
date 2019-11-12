from nltk.corpus import words
word_list = words.words()
dictionary=set(word_list)


def editDistDP(str1, str2, m, n): 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0: 
                dp[i][j] = j    
            elif j == 0: 
                dp[i][j] = i    
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])    
    return dp[m][n] 

def jaccard_similarity(word1,word2):
    return len(set(word1).intersection(set(word2))) / len(set(word1).union(set(word2)))

def strcmp(word1,word2):
    return abs(len(word1) - len(word2))

def min_edit_wrapper(word):

    main_list = [i for i in list(dictionary) if (not i[0].isupper() and jaccard_similarity(i,word)>=0.5 and (len(i)==len(word) or (i[0]==word[0] and (len(i)-1==len(word) or len(i)+1==len(word)))))]
    l1=[]

    for i in main_list:
        edit_dist = editDistDP(i,word,len(i),len(word))
        if edit_dist<4:
            l1.append((strcmp(i,word),edit_dist,jaccard_similarity(i,word),i,word))
    return sorted([i for i in l1 if i[0]<3])

print(min_edit_wrapper("crankshawt"))
