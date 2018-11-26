# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:56:16 2018

@author: trist
"""


import csv
from sklearn import tree
from spotify_api_client import search, search_all, get
#functions
#creates new list with all happy songs (index 1) or sad songs (index 0)
def sortList(in_list,index):
    out_list = []
    for i in range(len(in_list)):
        if in_list[i][20] == 1:
            out_list.append(in_list[i])
    return out_list

    

with open('song_list.csv','r') as csv_file:
    feat_list = list(csv.reader(csv_file))
    
#initializing lists   
    length = len(feat_list)-101
    
    feat_names = [None]*11
    for i in range(11):
        feat_names[i] = feat_list[0][i+2]
    
    fl_train = [[None]*11 for i in range(length)]
    fl_HS = [None]*(length)
    
    fl_test = [[None]*11 for i in range(100)]
    fl_ans = [None]*100

#copying data to training list, testing list, happy/sad lists    
    for i in range(length):
        for j in range(11):
            fl_train[i][j] = feat_list[i+1][j+2]
        fl_HS[i] = feat_list[i+1][20]
    
    for i in range(100):
        for j in range(11):
            fl_test[i][j] = feat_list[i+length+1][j+2]
        fl_ans[i] = feat_list[i+length+1][20]
   

#training decision tree    
    clf = tree.DecisionTreeClassifier()
    clf.fit(fl_train,fl_HS)

#run decision tree through test data
#calculating score, writing song names that were wrong
    score = 0 #out of 100
    
    for i in range(100):
        if clf.predict([fl_test[i]]) == fl_ans[i]:
            score = score+1
        else:
            print(feat_list[i+length+1][1], end=' ')
            if feat_list[i+length+1][20] == 1:
                print('happy')
            else:
                print('sad')
                
    print(f'Score : {score}/100')

#print graph that doesn't work yet
'''
    from sklearn.externals.six import StringIO
    import pydot
    
    dot_data = StringIO()
    tree.export_graphviz(clf,
                         out_file=dot_data,
                         feature_names=feat_names,
                         class_names=['sad','happy'],
                         filled=True, rounded=True,
                         impurity=False)

    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    graph[0].write_pdf("tree_test1.pdf")
'''

#get tracks from user
track = input("Name a song : ")

songID = search(track, 'track')
feat_csv = get(f'v1/audio-features/{songID}')


'''
# Gets the id of the first greatest hits album from the search results
songs = ['footloose','take on me','body','dancing queen','pursuit of happiness steve aoki']

for i in range(len(songs)):           
    response = search(songs[i], 'track')
    features = get(f'v1/audio-features/{response}')
    print(features)
'''        

    
    
    
#from spotify_api_client import get    
    
#response = get("v1/search", {'q':'greatest hits', 'type':'album'})
#reader = csv.reader(response)

#for line in reader:
#    print(line)
#print(reader)

