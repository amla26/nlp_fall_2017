# Name: Amla Srivastava
# Email ID: as5196@columbia.edu
# Homework 1


# How to train and test your classifier?
1. Install the emoji package
2. Run hw1.py to see the results for best-performing unigram, bigram, trigram and best final models trained on train_newline.txt
3. Run classify.py from command line using training data and testing data textfiles as arguments to check accuracy of the best performing model. This saves the best model to a model.pkl file and the vectorized test dataset to vectorized.pkl file
    - e.g. python classify.py train_newline.txt dev_newline.txt
4. Run analyze.py from command line with model and vectorized test data in pickel files to get top 20 features and confusion matrix
    - e.g. python analyze.py model.pkl vectorized.pkl
5. classify.py and analyze.py have been written with modules in a way which makes it possible to access them from hw1.py as well as from command line


# Special features and Limitations

The best model is a Bernoulli Naive Bayes classifier trained on data which is vectorized using a CountVectorizer with unigrams (unigram analysis gave best performance in initial models) and original word case retained. As specified in the assignment
no stopword removal or stemming has been applied. Techniques for feature selection such as SelectKBest were applied but did not give an increase in accuracy for the best model.
For the purpose of this analysis all features have been retained. Certain new features have been incorporated through either preprocessing or transformation to capture
style information from the tweets.

1. Emojis - Emojis capture a lot of information about user sentiment, context and meaning. They are frequently used in tweets. I used the emoji library
   to convert all emojis to their unicode references during preprocessing. Since the tweets were about election, the use of the american flag emoji (:us:) was pretty common.
   
2. Multiple exclamation marks - During preprocessing, before vectorization all strings of form !( !)+ were replaced by the word 'punctuation'. Such use of language can signal emphasis, excitement, etc.
   In case one part is more favoured for a win, its supporters may use such language to convey their excitement. On the other hand such use of punctuation may also imply negative feelings or anger
   or disbelief.

3. Word lengthening: In order to capture effect of wordlength I created a column called long_ind which contained the counts of words in a tweet that were longer than 10 characters.
   10 characters were chosen as a threshhold after rigorous analysis. The following list contains of (word_length, count) pairs for the training data.
   [(0, 0), (2, 1137), (4, 6064), (6, 8357), (8, 8961), (10, 22469), (12, 4417), (14, 2996), (16, 308), (18, 157), (20, 109), (22, 49), (24, 18), (26, 19), (28, 8), (30, 9), (32, 5), (34, 3), (36, 0), (38, 0), (40, 0), (42, 0), (44, 0), (46, 1), (48, 0), (50, 0), (52, 1), (54, 1), (56, 0), (58, 0), (60, 0), (62, 0), (64, 0), (66, 0), (68, 0), (70, 0), (72, 0), (74, 0), (76, 0), (78, 0), (80, 0), (82, 0), (84, 0), (86, 0), (88, 0), (90, 0), (92, 0), (94, 0), (96, 0), (98, 0)] 
   The count of words with length greater than 10 quickly peters off. On further analysis it was observed that these features were often extended words 
   like coooooool, web links and hashtags e.g. 100ReasonsNotToVoteRepublican, Hahahahahahahahahahahahaha, HeHasBeenToyingWithMyAffection
   
4. Capitalized words: Capitalized words such as DEMOCRAT, AGREED, APATHY were present in the data and often capture additional meaning such as emphasis. An additional
   column indicator called cap_ind was created to store the count of capitalized words in the tweet (combination of alphabet only). The CountVectorizer was set in a way to not ignore cases so as to capture this information.
   
For the dev dataset, the best performance was observed using Bernoulli Naive Bayes algorithm and its parameters were set after grid search to 
be (alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None). An accuracy of 62.5 % was observed. The inclusion of additional features did not give an significant
increase in accuracy but with the use of further data cleaning and preprocessing and possibly with other modeling techniques, information from these 
features will potentially boost performance. Also in this case comparison has been done using only accuracy feasures. Precision, recall, f1 scores, AUC scores can be tested in the future.
A possible reason for the lack of improvement is also that the dataset is noisy and contains several features that do not capture meaningful information such as misspelled data.
Stopword removal, minimum frequesncy and further feature selection may prove useful.

