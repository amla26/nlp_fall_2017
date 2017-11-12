n[31]:

from analyze import print_top_20, print_confusion_matrix, analyze_run
from classify import *
import numpy as np
import sklearn.metrics
from sklearn.metrics import confusion_matrix
import sys
import pickle
from scipy.sparse import *
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
np.set_printoptions(precision=3, suppress=True)
import re
import emoji
from collections import Counter


#reading in data for initial three models
text_train = []
y_train = []
text_dev = []
y_dev = []

f_train = open('train_newline.txt', 'r') 
f_dev = open('dev_newline.txt','r')


for line in f_train:
        
    x = line.strip().split('\t')
    text_train.append(x[0])
    y_train.append(x[1])
    
    
for line in f_dev:
    
    x = line.strip().split('\t')
    text_dev.append(x[0])
    y_dev.append(x[1])
    
       
f_train.close()
f_dev.close()

text = np.array(text_train)
labels = np.array(y_train)

print("length of text_train: {}".format(len(text_train)))
c = Counter(y_train)
print('No. of observations per class ', c.items() )

from sklearn.feature_extraction.text import CountVectorizer

cv1 = CountVectorizer(ngram_range=(1, 1))
cv2 = CountVectorizer(ngram_range=(2, 2))
cv3 = CountVectorizer(ngram_range=(3, 3))

## UNIGRAM MODEL
X_train = cv1.fit_transform(text_train)
X_dev = cv1.transform(text_dev)

feature_names1 = cv1.get_feature_names()
print("Vocabulary size: {}".format(len(cv1.vocabulary_)))
print("Vocabulary(first 10 words):\n{}".format(feature_names1[:10]))


#fitting Bernoulli Naive Bayes model with parameters determined after grid search
bnb = BernoulliNB(alpha = 1, fit_prior = True)
bnb.fit(X_train, y_train)

print('UNIGRAM MODEL')
print('Unigram accuracy with Bernoulli Naive Bayes on dev set:' ,bnb.score(X_dev, y_dev))

print_top_20(bnb.coef_.ravel(),np.array(feature_names1), nb = True)

y_pred = bnb.predict(X_dev)
np.set_printoptions(precision=2)
print_confusion_matrix(y_dev,y_pred)


## CREATING BIGRAM MODEL
X_train = cv2.fit_transform(text_train)
X_dev = cv2.transform(text_dev)

feature_names2 = cv2.get_feature_names()
print("Vocabulary size: {}".format(len(cv2.vocabulary_)))
print("Vocabulary (first 10 words):\n{}".format(feature_names2[:10]))

#best bigram model based on logistic regression with parameters determined through grid search
# param_grid = {"logisticregression__C": [100, 10, 1, 0.1, 0.01],
#               "logisticregression__penalty": ['l1','l2'],
#               "logisticregression__fit_intercept": [True, False]
#              }
# grid = GridSearchCV(make_pipeline(LogisticRegression()),
#                     param_grid=param_grid, cv=5, scoring="accuracy"
#                    )

# grid.fit(X_train,y_train)

lr = LogisticRegression(C = 10)
lr.fit(X_train,y_train)
print('Bigram accuracy with Logistic regression on dev set:' ,lr.score(X_dev, y_dev))


print_top_20(lr.coef_.ravel(),np.array(feature_names2))

y_pred = lr.predict(X_dev)
print_confusion_matrix(y_dev,y_pred)


print('TRIGRAM MODEL')
X_train = cv3.fit_transform(text_train)
X_dev = cv3.transform(text_dev)

feature_names3 = cv3.get_feature_names()
print("Vocabulary size: {}".format(len(cv3.vocabulary_)))
print("Vocabulary(first 10 words:\n{}".format(feature_names3[:10]))

#best bigram model based on logistic regression with parameters determined through grid search
# param_grid = {"logisticregression__C": [100, 10, 1, 0.1, 0.01],
#               "logisticregression__penalty": ['l1','l2'],
#               "logisticregression__fit_intercept": [True, False]
#              }
# grid = GridSearchCV(make_pipeline(LogisticRegression()),
#                     param_grid=param_grid, cv=5, scoring="accuracy"
#                    )

# grid.fit(X_train,y_train)

lr = LogisticRegression(C = 100)
lr.fit(X_train,y_train)
print('Trigram accuracy with Logistic regression on dev set:' ,lr.score(X_dev, y_dev))


print_top_20(lr.coef_.ravel(),np.array(feature_names3))

y_pred = lr.predict(X_dev)
print_confusion_matrix(y_dev,y_pred)

#Best model

from classify import *
classify_run()

analyze_run()





