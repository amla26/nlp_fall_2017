n[4]:

import numpy as np
import sklearn.metrics
import re
import sys
import pickle
import emoji
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import *
from sklearn.naive_bayes import BernoulliNB
np.set_printoptions(precision=3, suppress=True)

def classify_run(trainfile = 'train_newline.txt', testfile = 'dev_newline.txt'):
    #reading in data
    text_train = []
    y_train = []
    text_dev = []
    y_dev = []

    # print(str(sys.argv)[1]) #train data
    # print(str(sys.argv)[2]) #test data

    f_train = open(trainfile, 'r') 
    f_dev = open(testfile,'r')

    for line in f_train:

        #replacing multiple exclamation marks with the word 'punctuation'
        line = re.sub('!( !)+', 'punctuation', line)    
        x = line.strip().split('\t')

        #replacing emojis by their respective names from emoji package
        for i in x[0]:
            if i in emoji.UNICODE_EMOJI.keys():
                x[0] = re.sub(i,emoji.UNICODE_EMOJI[i],x[0])

        text_train.append(x[0])
        y_train.append(x[1])

    for line in f_dev:

        #replacing multiple exclamation marks with the word 'punctuation'
        line = re.sub('!( !)+', 'punctuation', line)   
        x = line.strip().split('\t')

        #replacing emojis by their respective names from emoji package
        for i in x[0]:
            if i in emoji.UNICODE_EMOJI.keys():
                x[0] = re.sub(i,emoji.UNICODE_EMOJI[i],x[0])

        text_dev.append(x[0])
        y_dev.append(x[1])

    f_train.close()
    f_dev.close()

    print('Data loaded')


    text = np.array(text_train)
    labels = np.array(y_train)


    #using unigrams as they gave best result from previous modeling iterations
    #not converting text to lowercase to enable extraction of features such as 'AWESOME'
    cv4 = CountVectorizer(ngram_range= (1,1), lowercase = False)

    X_train = cv4.fit_transform(text_train)
    X_dev = cv4.transform(text_dev)

    feature_names4 = cv4.get_feature_names()
    print("Vocabulary size: {}".format(len(cv4.vocabulary_)))
    print("Vocabulary (first 10 words):\n{}".format(feature_names4[0:10]))

    #creating an index to capture all features made only with uppercase alphabet
    cap_ind = []

    for i in range(len(feature_names4)):
        if feature_names4[i] == feature_names4[i].upper() and re.search('^[A-Z]+$', feature_names4[i]):
            cap_ind.append(i)

    def capsum(a):
        return a[cap_ind].sum()

    cap_train = list(np.apply_along_axis( capsum, 1,X_train.toarray() ))
    cap_dev = list(np.apply_along_axis( capsum, 1,X_dev.toarray()))

    #merging data with column encoding no. of words which follow all CAPS criteria
    X_train = hstack((X_train,np.array(cap_train)[:,None]))
    X_dev = hstack((X_dev,np.array(cap_dev)[:,None]))

    #creating an index to track all feature which have word length > 10; usually correspond to extended words and hashtags
    long_ind = []

    for i in range(len(feature_names4)):
        if len(feature_names4[i]) > 10:
            long_ind.append(i)

    def longsum(a):
        return a[long_ind].sum()

    long_train = list(np.apply_along_axis(longsum, 1,X_train.toarray()))
    long_dev = list(np.apply_along_axis(longsum, 1,X_dev.toarray()))

    #merging column encoding no. of long words in text
    X_train = hstack((X_train,np.array(long_train)[:,None]))
    X_dev = hstack((X_dev,np.array(long_dev)[:,None]))

    #extending feature names list
    feature_names4 = feature_names4 + ['cap_ind', 'long_ind']

    #building Bernoulli Naive Bayes model for classification
    #after manual search default parameters (alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None) gave best performance

    bnb = BernoulliNB()
    bnb.fit(X_train, y_train)

    print('Best model trained')
    print('Accuracy of best model: ',bnb.score(X_dev, y_dev))

    #saving model, truelabels and feature names to pickle file
    with open('model.pkl', 'wb') as f:
        pickle.dump((bnb,y_dev,feature_names4), f) 

    #saving vectorized test data to vectorized_pkl.file

    with open('vectorized.pkl', 'wb') as f:
        pickle.dump( X_dev, f)
        
if __name__ == '__main__':       
    classify_run(str(sys.argv[1]), str(sys.argv[2]))



