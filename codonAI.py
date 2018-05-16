#!/usr/bin/python

#My first Python program
from sklearn import tree
import sys

#4-U; 1-A; 2-C; 3-G; is used
features = [
[3,3,3],
[3,3,1],
[3,3,4],
[3,3,2],
[3,1,3],
[3,1,1],
[3,1,4],
[3,1,2],
[3,4,3],
[3,4,1],
[3,4,4],
[3,4,2],
[3,2,3],
[3,2,1],
[3,2,4],
[3,2,2],
[1,3,3],
[1,3,1],
[1,3,4],
[1,3,2],
[1,1,3],
[1,1,1],
[1,1,4],
[1,1,2],
[1,4,3],
[1,4,1],
[1,4,4],
[1,4,2],
[1,2,3],
[1,2,1],
[1,2,4],
[1,2,2],
[4,3,3],
[4,3,1],
[4,3,4],
[4,3,2],
[4,1,3],
[4,1,1],
[4,1,4],
[4,1,2],
[4,4,3],
[4,4,1],
[4,4,4],
[4,4,2],
[4,2,3],
[4,2,1],
[4,2,4],
[4,2,2],
[2,3,3],
[2,3,1],
[2,3,4],
[2,3,2],
[2,1,3],
[2,1,1],
[2,1,4],
[2,1,2],
[2,4,3],
[2,4,1],
[2,4,4],
[2,4,2],
[2,2,3],
[2,2,1],
[2,2,4],
[2,2,2]
	   ]

labels = [
'Gly',
'Gly',
'Gly',
'Gly',
'Glu',
'Glu',
'Asp',
'Asp',
'Val',
'Val',
'Val',
'Val',
'Ala',
'Ala',
'Ala',
'Ala',
'Arg',
'Arg',
'Ser',
'Ser',
'Lys',
'Lys',
'Asn',
'Asn',
'Met',
'Ile',
'Ile',
'Ile',
'Thr',
'Thr',
'Thr',
'Thr',
'Trp',
'End',
'Cys',
'Cys',
'End',
'End',
'Tyr',
'Tyr',
'Leu',
'Leu',
'Phe',
'Phe',
'Ser',
'Ser',
'Ser',
'Ser',
'Arg',
'Arg',
'Arg',
'Arg',
'Gln',
'Gln',
'His',
'His',
'Ser',
'Leu',
'Leu',
'Leu',
'Pro',
'Pro',
'Pro',
'Pro'
	 ]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

inputVal = raw_input('Enter nucleotide letters code?\n') ; sys.stdin = sys.__stdin__ 

#print "Length of the string: ", len(inputVal)

if len(inputVal) > 3 or len(inputVal) < 3:
   print "Are you kidding me! \nPlease provide the nucleotide sequence in THREE letter only"
   sys.exit()

#print (inputVal);
#a,b,c = inputVal.split(',')
new_str = inputVal.upper()
new_str = new_str.replace('T', 'U')
new_str = new_str.replace('A', '1')
new_str = new_str.replace('C', '2')
new_str = new_str.replace('G', '3')
new_str = new_str.replace('U', '4')

val1,val2,val3 = list(new_str)
print val1,val2,val3

print clf.predict([[val1,val2,val3]])

