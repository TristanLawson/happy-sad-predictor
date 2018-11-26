# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:51:35 2018

@author: trist
"""

from sklearn import tree

#criteria : attractive/9 : funny/9 : teases/9 : inShape/9 : adventurous/9 : interests/9
andeeC =    [4,6,9,5,7,8]
micheC =    [8,5,2,9,8,6]
oliviaC =   [6,8,9,6,7,7]
halleC =    [9,4,1,8,9,8]
katieC =    [9,7,5,7,6,6]
lexiC =     [7,5,8,8,5,0]

kaitlynC =  [7,3,0,8,4,3]
mathieC =   [6,8,8,6,7,7]

#score : date : one-night-stand
andeeS =   [0,0]
micheS =   [1,1]
oliviaS =  [1,0]
halleS =   [1,1]
katieS =   [0,1]
lexiS =    [0,1]



criteria =      [andeeC,micheC,oliviaC,halleC,katieC,lexiC]
date =          [andeeS[0],micheS[0],oliviaS[0],halleS[0],katieS[0],lexiS[0]]
oneNightStand = [andeeS[1],micheS[1],oliviaS[1],halleS[1],katieS[1],lexiS[1]]

onscheck = tree.DecisionTreeClassifier()
onscheck = onscheck.fit(criteria,oneNightStand)

datecheck = tree.DecisionTreeClassifier()
datecheck = datecheck.fit(criteria,date)

kaitlynONS = onscheck.predict([kaitlynC])
kaitlynDATE = datecheck.predict([kaitlynC])

mathieONS = onscheck.predict([mathieC])
mathieDATE = datecheck.predict([mathieC])


print('Kaitlyn')
print(kaitlynONS)
print(kaitlynDATE)
print('Mathie')
print(mathieONS)
print(mathieDATE)

