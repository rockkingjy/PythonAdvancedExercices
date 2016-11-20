#recommandation
import math
from textblob import TextBlob as tb
from sklearn.feature_extraction.text import CountVectorizer

NumberDocument = 4
def tf(word, blob):
    return float(blob.words.count(word)) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / float(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return float(tf(word, blob) * idf(word, bloblist))

text1 = """Python is a 2000 made-for-TV horror movie directed by Richard
Clabaugh. The film features several cult favorite actors, including William
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
Whalen. The film concerns a genetically engineered snake, a python, that
escapes and unleashes itself on a small town. It includes the classic final
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
 California and Malibu, California. Python was followed by two sequels: Python
 II (2002) and Boa vs. Python (2004), both also made-for-TV films."""

text2 = """Deep Learning is a new area of Machine Learning research, which has been introduced with the objective of moving Machine Learning closer to one of its original goals: Artificial Intelligence.

This website is intended to host a variety of resources and pointers to information about Deep Learning. In these pages you will find

a reading list,
links to software,
datasets,
a list of deep learning research groups and labs,
a list of announcements for deep learning related jobs (job listings),
as well as tutorials and cool demos.
announcements and news about deep learning
For the latest additions, including papers and software announcement, be sure to visit  the Blog section and subscribe to our RSS feed of the website. Contact us if you have any comments or suggestions!"""

text3 = """In general, a learning problem considers a set of n samples of data and then tries to predict properties of unknown data. If each sample is more than a single number and, for instance, a multi-dimensional entry (aka multivariate data), it is said to have several attributes or features.
"""

text4 = """Big Data is a phrase used to mean a massive volume of both structured and unstructured data that is so large it is difficult to process using traditional database and software techniques. In most enterprise scenarios the volume of data is too big or it moves too fast or it exceeds current processing capacity.
Big Data has the potential to help companies improve operations and make faster, more intelligent decisions. This data, when captured, formatted, manipulated, stored, and analyzed can help a company to gain useful insight to increase revenues, get or retain customers, and improve operations."""

"""
document1 = tb(text1.lower())
document2 = tb(text2.lower())
document3 = tb(text3.lower())
document4 = tb(text4.lower())


bloblist = [document1, document2, document3, document4]

Len = 10
items = []
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:Len]:
		items.append((word,score))
		#print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))

inword = "big"
#print(items)
i = 0
for item in items:
	i += 1;
	if(inword == item[0]):
		print("Recommand document:", int(i/Len) + 1)
"""
#=========================================
t = [text1,text2,text3,text4]

vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(t)
print(X)
similarite = X*X.transpose()

r = [[0 for x in range(NumberDocument)] for y in range(NumberDocument)] 
for i in range(NumberDocument):
    norm = float(similarite[i,i])
    for j in range(NumberDocument):	
		r[i][j] = float(similarite[i,j]) / norm
print(r)

"""
#question2
inwords = "big data machine learning"
t.append(inwords)
vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(t)
#print(X)
similarite = X*X.transpose()

sim2 = [0 for x in range(NumberDocument)] 
for i in range(NumberDocument):
    norm = float(similarite[i,i])	
    sim2[i] = float(similarite[NumberDocument,i]) / norm
print(sim2)
for i in range(NumberDocument):
	if(sim2[i]==max(sim2)):
		print("Recommand document:", i+1)

"""




