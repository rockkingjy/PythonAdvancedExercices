import matplotlib.pyplot as plt

import cPickle as pickle

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
def Question1():
	modaliteNan = [0]*len(data[0])
	for i in range(len(data)):
		for j in range(len(data[0])):
		    if(data[i][j]==""):
		        modaliteNan[j]+=1
	print(modaliteNan)
# Question1()
# [0, 0, 0, 0, 0, 177, 0, 0, 0, 0, 687, 2]

#Question 2
def Question2write():
	with open('filename', 'wb') as f:
		dataserial = []
		for i in range(len(data)): 
			dataserial.append(data[i][1]) #survived
		for i in range(len(data)):
			dataserial.append(data[i][2]) #Pclass
		for i in range(len(data)):
			dataserial.append(data[i][4]) #Sex
		for i in range(len(data)):
			dataserial.append(data[i][5]) #Age
		for i in range(len(data)):
			dataserial.append(data[i][11]) #Embarked
		pickle.dump(dataserial, f)
def Question2read():
    with open('filename','rb') as f:
        var = pickle.load(f)
        print var
#Question2write()
#Question2read()

#Question 3 
def Question3(bin = 20):
	agepre = [None]*len(data)
	for i in range(len(data)):
		if(data[i][5]!=""):
		    agepre[i]=float(data[i][5])
	age = []
	for i in range(len(agepre)):
		if(agepre[i]!=None):
		       age.append(agepre[i])
	plt.hist(age,bin)
	plt.title("Titanic Age Histogram")
	plt.xlabel("Age")
	plt.ylabel("Frequency")
	plt.show()
#Question3()

#Question 4
def Question4():
	Question3(8)
#Question4()

#Question 5
#a)
def Question5a():
	onboat = [None]*len(data)
	for i in range(len(data)):
		if(data[i][1]!=""):
		    onboat[i]=float(data[i][1])
	numsur = 0
	for i in range(len(onboat)):
		if(onboat[i]==1):
		    numsur+=1
	print("a) La proportion de passagers ayant survecu: {0}".format(numsur/float(len(onboat))))
	return numsur,len(onboat)
#Question5a()
#b)
def Question5b():
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
	print("b) La proportion de femmes ayant survecu: {0},\n \
	la proportion de hommes ayant survecu: {1}").format( \
	float(numsurfemale)/float(numfemale),float(numsurmale)/float(nummale))
	return numsurmale, nummale, numsurfemale, numfemale
#Question5b()
#c)
def Question5c1(numsur, numall):
	plotsur = (numall-numsur, numsur)

	fig=plt.figure()
	ytickspos = [0, 0.5] #position of y tick labels of the bar
	h = 0.2 #height of the bar
	b = [0-h/2,0.5-h/2] #bottom of the bar
	p1 = plt.barh(bottom = b, width = plotsur, height = h, left=None, color='b')
	plt.title('Survival Breakdown')
	plt.yticks(ytickspos, ('Died', 'Survived'))
	plt.grid()
	plt.show()
#(numsur, numall) = Question5a()
#Question5c1(numsur, numall)

def Question5c2(numsurmale, nummale, numsurfemale, numfemale):
	plotsurmale = (nummale-numsurmale, numsurmale)
	plotsurfemale = (numfemale-numsurfemale, numsurfemale)
	
	fig=plt.figure()
	ytickspos = [0, 0.5] #position of y tick labels of the bar
	h = 0.2 #height of the bar
	b = [0-h/2,0.5-h/2] #bottom of the bar
	alf = 0.5
	p1 = plt.barh(b, plotsurmale, h, color='b',alpha=alf)
	p2 = plt.barh(b, plotsurfemale, h, color='r',alpha=alf)
	plt.legend((p1[0], p2[0]), ('Men', 'Women'))
	plt.yticks(ytickspos, ('Died', 'Survived'))
	plt.grid()
	plt.show()
#(numsurmale, nummale, numsurfemale, numfemale) = Question5b()
#Question5c2(numsurmale, nummale, numsurfemale, numfemale)
#d)Non
#e)f)
def Question5ef(variable):
    if(variable=="Sex"):
        (numsurmale, nummale, numsurfemale, numfemale) = Question5b()
        Question5c2(numsurmale, nummale, numsurfemale, numfemale)
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
        plot1 = (num1-num1sur, num1sur)
        plot2 = (num2-num2sur, num2sur)
        plot3 = (num3-num3sur, num3sur)

        ytickspos = [0, 0.5] #position of y tick labels of the bar
        h = 0.2 #height of the bar
        b = [0-h/2,0.5-h/2] #bottom of the bar
        alf = 0.5
        p1 = plt.barh(b, plot1, h, color='y',alpha=alf)
        p2 = plt.barh(b, plot2, h, color='b',alpha=alf)
        p3 = plt.barh(b, plot3, h, color='r',alpha=alf)
        plt.legend((p1[0], p2[0], p3[0]), ('class1', 'class2', 'class3'))
        plt.yticks(ytickspos, ('Died', 'Survived'))
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
        plot1 = (num1-num1sur, num1sur)
        plot2 = (num2-num2sur, num2sur)
        plot3 = (num3-num3sur, num3sur)

        ytickspos = [0, 0.5] #position of y tick labels of the bar
        h = 0.2 #height of the bar
        b = [0-h/2,0.5-h/2] #bottom of the bar
        alf = 0.5
        p1 = plt.barh(b, plot1, h, color='y',alpha=alf)
        p2 = plt.barh(b, plot2, h, color='b',alpha=alf)
        p3 = plt.barh(b, plot3, h, color='r',alpha=alf)
        plt.legend((p1[0], p2[0], p3[0]), ('<20', '>50', 'other'))
        plt.yticks(ytickspos, ('Died', 'Survived'))
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
        plot1 = (num1-num1sur, num1sur)
        plot2 = (num2-num2sur, num2sur)
        plot3 = (num3-num3sur, num3sur)

        ytickspos = [0, 0.5] #position of y tick labels of the bar
        h = 0.2 #height of the bar
        b = [0-h/2,0.5-h/2] #bottom of the bar
        alf = 0.5
        p1 = plt.barh(b, plot1, h, color='y',alpha=alf)
        p2 = plt.barh(b, plot2, h, color='b',alpha=alf)
        p3 = plt.barh(b, plot3, h, color='r',alpha=alf)
        plt.legend((p1[0], p2[0], p3[0]), ('S', 'C', 'Q'))
        plt.yticks(ytickspos, ('Died', 'Survived'))
        plt.show()
#Question5ef("Embarked")
#g)
import scipy.stats as stats
import pandas as pd
def Question5g():
	df = pd.read_csv('train.csv')
	df1,df2 = df['Survived'], df['Sex']
	result = [[sum((df1 == cat1) & (df2 == cat2))
              for cat1 in (0,1)]
              for cat2 in ('male','female')]
	print result
	chi2,p,dof,expected = stats.chi2_contingency(result)
	print chi2, p
#Question5g()

#Question 6,7
import math
def Question67(variable='Sex'):
	df = pd.read_csv('train.csv')
	df1,df2 = df['Survived'], df[variable]
	if(variable=='Sex'):
		items = ('male','female')
	elif(variable=='Pclass'):
		items = (1,2,3)
	elif(variable=='Age'):
		pd.options.mode.chained_assignment = None # default='warn'
		for age in range(len(df2)):
			if math.isnan(df2[age]) != True:
				if df2[age] < 20:
					df2[age] = '<20'
				elif df2[age] > 50:
					df2[age] = '>50'
				else:
					df2[age] = '>20<50'      
		print df2  
		items = ('<20','>50','>20<50')
	elif(variable=='Embarked'):
		items = ('C','S','Q')
	result = [[sum((df1 == cat1) & (df2 == cat2))
              for cat1 in (0,1)]
              for cat2 in items]
	print result
	chi2,p,dof,expected = stats.chi2_contingency(result)
	print chi2, p
#Question67('Age')

#Question 8
import matplotlib as mpl
def Question8():
	df = pd.read_csv('train.csv')
	df1,df2 = df['Age'], df['Pclass']
	cut = [14,19,22,25,28,31,36,42,50,80]

	xedges = range(10)
	yedges = [1, 2, 3]

	H = np.ones((3, 10)).cumsum().reshape(3, 10)
	print(H[::-1])  # This shows the bin content in the order as plotted

	for age in range(len(df1)):
		for i in range(len(cut)):
			if(df1[age] < cut[i]):
				#print i, int(df2[age])-1
				H[int(df2[age])-1][i] += 1
				break;
	print H	
	fig = plt.figure(figsize=(7, 3))
	plt.title('Class and age square binning')
	im = plt.imshow(H, interpolation='nearest', origin='low',
		            extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
	ytickspos = [1, 2, 3] #position of y tick labels of the bar
	plt.yticks(ytickspos, ('Class1', 'Class2', 'Class3'))
	plt.xticks(xedges, ('[0,14]', '[14,19]', '[19,22]', '[22,25]', '[25,28]', '[28,31]', '[31,36]', '[36,42]', '[42,50]', '[50,80]'))
	plt.show()
Question8()

#Question 9





