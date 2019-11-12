from flask import Flask, render_template, request, jsonify, url_for, redirect
app = Flask(__name__)
import json
import operator
fp = open("cleandata.txt","r")
dictionary = [i.rstrip("\n") for i in fp.readlines()]
fp.close()
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
    return (dp[m][n],dp)

def jaccard_similarity(word1,word2):
    return len(set(word1).intersection(set(word2))) / len(set(word1).union(set(word2)))

def strcmp(word1,word2):
    if word1[0]==word2[0]:
        return 0
    return 1

def min_edit_wrapper(word):

    main_list = [i for i in list(dictionary) if (not i[0].isupper() and jaccard_similarity(i,word)>=0.5 and (len(i)==len(word) or (i[0]==word[0] and (len(i)-1==len(word) or len(i)+1==len(word)))))]
    l1=[]

    for i in main_list:
        edit_dist = editDistDP(i,word,len(i),len(word))
        l1.append((edit_dist[0],1-jaccard_similarity(i,word),strcmp(i,word),edit_dist[1],i,word))
    return sorted(l1,key = operator.itemgetter(0,1,2))

@app.route('/checkword')
def compareword():
    arr = min_edit_wrapper(request.args.get('word').lower())
    print("\n\n\n",arr,"\n\n\n") 
    return json.dumps([[i[3],i[4]] for i in arr][:5:])

@app.route('/')
def minedit():
    return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)