import re
import time

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

stop = stopwords.words("english")
print time.ctime()
start_time=time.time()
df = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
#print df.head()
df.dropna(inplace=True)
df["Postive rated"]=np.where(df['sentiment']>0,1,0)
#df["Postive rated"]=pd.cut(df['Sentiment'], [0, 1, 2, np.inf], labels=['Neg','Neu','Pos'])

def cleaning_words(raw_words):
	exam=BeautifulSoup(raw_words,"html.parser") #removing html tags
    letters = re.sub("\b[^a-zA-Z]", " ",
                     exam.get_text())  # removing numbers and others except small and capital alphabets
	low=letters.lower() #Converting everything to lower case
	words=low.split() #spiliting sentences into words
    useful = [w for w in words if not w in stop]  #removing stopping words


use_sent = " ".join(useful)
	return use_sent



num=df["review"].size
#print num
perfect_words=[]

for i in xrange(0,num):
	#if( (i+1)%1000 == 0 ):
	print "Review %d of %d\n" % ( i+1, num)
	perfect_words.append(cleaning_words(df["review"][i]))
	
#print df.head(67)
#print df["Postive rated"].mean()
X_train, X_test, y_train, y_test = train_test_split(perfect_words,df['Postive rated'],random_state=0)
#print X_train[10]
#print X_train.shape
#print df['Postive rated']

vect=CountVectorizer(min_df=5,ngram_range=(1,2)).fit(X_train)
print len(vect.get_feature_names())

X_train_vetorised=vect.transform(X_train)
#print X_train_vetorised

print "starting training!!!!!"
model=LogisticRegression()
print "Stage 1 is completed"
model.fit(X_train_vetorised,y_train)
print "Stage 2 is completed"
predictions=model.predict(vect.transform(X_test))
print "Stage 3 is completed"
print ("AUC:",roc_auc_score(y_test,predictions))

feature_name=np.array(vect.get_feature_names())
sort_coeff=model.coef_[0].argsort()
print ("small coeff : {}",format(feature_name[sort_coeff[:10]]))
print ("large coeff : {}",format(feature_name[sort_coeff[:-11:-1]]))

print time.ctime()
testing=raw_input("Enter the sentence for testing: ")
print(model.predict(vect.transform([testing])))
print ("The total time for execution is",time.time()-start_time)

