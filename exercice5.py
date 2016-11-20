import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb')) 	# Load in the csv file
header = csv_file_object.next() 						# Skip the fist line as it is a header
data=[] 												# Create a variable to hold the data

for row in csv_file_object: 							# Skip through each row in the csv file,
    data.append(row[0:]) 								# adding each row to the data variable
data = np.array(data) 									# Then convert from a list to an array.

#Question 1
#print(data[5][4])
modaliteNan = [0]*len(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        if(data[i][j]==""):
            modaliteNan[j]+=1
print(modaliteNan)
#[0, 0, 0, 0, 0, 177, 0, 0, 0, 0, 687, 2]

#Question 3
agepre = [None]*len(data)
for i in range(len(data)):
    if(data[i][5]!=""):
        agepre[i]=float(data[i][5])
age = []
for i in range(len(agepre)):
    if(agepre[i]!=None):
           age.append(agepre[i])
"""
plt.hist(age)
plt.title("Titanic Age Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
"""

#Question 5
#a]
survecu = [None]*len(data)
for i in range(len(data)):
    if(data[i][1]!=""):
        survecu[i]=float(data[i][1])
#print(survecu)
numsur = 0
for i in range(len(survecu)):
    if(survecu[i]==1):
        numsur+=1
print("a) La proportion de passagers ayant survecu: {0}".format(numsur/float(len(survecu))))
#b)
numsurmale = 0
nummale = 0
numsurfemale = 0
numfemale = 0
for i in range(len(data)):
    if(data[i][4]=="male"):
        nummale+=1
        if(float(data[i][1])==1):
            numsurmale+=1
    else:
        numfemale+=1
        if(float(data[i][1])==1):
            numsurfemale+=1
print("b) La proportion de femmes: {0}, la proportion de hommes: {1}").format(float(numsurfemale)/float(numfemale),float(numsurmale)/float(nummale))
#c)
"""
N = 2
ind= (0,1)
plotsur = (len(survecu)-numsur, numsur)
plotsurmale = (nummale-numsurmale, numsurmale)
plotsurfemale = (numfemale-numsurfemale, numsurfemale)
print(plotsurmale,plotsurfemale)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
#p1 = plt.barh(ind, plotsur, width, color='b')
plt.title('Survival Breakdown(1=Survived, 0=Died)')
pos = [0.25,1.25]
plt.yticks(pos, ('0', '1'))
#plt.show()

p1 = plt.barh(ind, plotsurmale, width, color='b',alpha=0.8)
p2 = plt.barh(ind, plotsurfemale, width, color='r',alpha=0.8)
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
#plt.show()
"""
#d)Non
#e)f)
def variableSur(variable):
    if(variable=="Sex"):
        numsurmale = 0
        nummale = 0
        numsurfemale = 0
        numfemale = 0
        for i in range(len(data)):
            if(data[i][4]=="male"):
                nummale+=1
                if(float(data[i][1])==1):
                    numsurmale+=1
            else:
                numfemale+=1
                if(float(data[i][1])==1):
                    numsurfemale+=1
        N = 2
        ind= (0,1)
        plotsurmale = (nummale-numsurmale, numsurmale)
        plotsurfemale = (numfemale-numsurfemale, numsurfemale)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        pos = [0.25,1.25]
        plt.yticks(pos, ('0', '1'))
        p1 = plt.barh(ind, plotsurmale, width, color='b',alpha=0.8)
        p2 = plt.barh(ind, plotsurfemale, width, color='r',alpha=0.8)
        plt.legend((p1[0], p2[0]), ('Men', 'Women'))
        plt.show()
    elif(variable=="Pclass"):
        num1sur=0
        num1=0
        num2sur=0
        num2=0
        num3sur=0
        num3=0
        for i in range(len(data)):
            if(float(data[i][2])==1):
                num1+=1
                if(float(data[i][1])==1):
                    num1sur+=1
            elif(float(data[i][2])==2):
                num2+=1
                if(float(data[i][1])==1):
                    num2sur+=1
            elif(float(data[i][2])==3):
                num3+=1
                if(float(data[i][1])==1):
                    num3sur+=1
        N = 2
        ind= (0,1)
        plot1 = (num1-num1sur, num1sur)
        plot2 = (num2-num2sur, num2sur)
        plot3 = (num3-num3sur, num3sur)
        print(plot1)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        pos = [0.25,1.25,2.25]
        plt.yticks(pos, ('1', '2', '3'))
        p1 = plt.barh(ind, plot1, width, color='y',alpha=0.5)
        p2 = plt.barh(ind, plot2, width, color='b',alpha=0.5)
        p3 = plt.barh(ind, plot3, width, color='r',alpha=0.5)
        plt.legend((p1[0], p2[0], p3[0]), ('class1', 'class2', 'class3'))
        plt.show()
    elif(variable=="Age"):
        num1sur=0
        num1=0
        num2sur=0
        num2=0
        num3sur=0
        num3=0
        for i in range(len(data)):
            if(data[i][5]!=""):
                if(float(data[i][5])<20):
                    num1+=1
                    if(float(data[i][1])==1):
                        num1sur+=1
                elif(float(data[i][5])>50):
                    num2+=1
                    if(float(data[i][1])==1):
                        num2sur+=1
                else:
                    num3+=1
                    if(float(data[i][1])==1):
                        num3sur+=1
        N = 2
        ind= (0,1)
        plot1 = (num1-num1sur, num1sur)
        plot2 = (num2-num2sur, num2sur)
        plot3 = (num3-num3sur, num3sur)
        print(plot1)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        pos = [0.25,1.25,2.25]
        plt.yticks(pos, ('1', '2', '3'))
        p1 = plt.barh(ind, plot1, width, color='y',alpha=0.5)
        p2 = plt.barh(ind, plot2, width, color='b',alpha=0.5)
        p3 = plt.barh(ind, plot3, width, color='r',alpha=0.5)
        plt.legend((p1[0], p2[0], p3[0]), ('<20', '>50', 'other'))
        plt.show()
    elif(variable=="Embarked"):
        num1sur=0
        num1=0
        num2sur=0
        num2=0
        num3sur=0
        num3=0
        for i in range(len(data)):
            if(data[i][11]=="S"):
                num1+=1
                if(float(data[i][1])==1):
                    num1sur+=1
            elif(data[i][11]=="C"):
                num2+=1
                if(float(data[i][1])==1):
                    num2sur+=1
            elif(data[i][11]=="Q"):
                num3+=1
                if(float(data[i][1])==1):
                    num3sur+=1
        N = 2
        ind= (0,1)
        plot1 = (num1-num1sur, num1sur)
        plot2 = (num2-num2sur, num2sur)
        plot3 = (num3-num3sur, num3sur)
        print(plot1)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        pos = [0.25,1.25,2.25]
        plt.yticks(pos, ('1', '2', '3'))
        p1 = plt.barh(ind, plot1, width, color='y',alpha=0.5)
        p2 = plt.barh(ind, plot2, width, color='b',alpha=0.5)
        p3 = plt.barh(ind, plot3, width, color='r',alpha=0.5)
        plt.legend((p1[0], p2[0], p3[0]), ('S', 'C', 'Q'))
        plt.show()
        
#variableSur("Age")
#g)


