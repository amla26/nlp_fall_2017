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

def print_confusion_matrix (y_test,y_pred):
    
    cnf_matrix = confusion_matrix(y_test, y_pred, labels = ['democrat','republican'])
    np.set_printoptions(precision=2)

    print('Confusin matrix where democrat = 0, republican = 1')
    print(cnf_matrix)



# function to print top 20 features
def print_top_20(coef, feature_names, nb = False):
    
    if nb:
        sorted_coef = np.argsort(coef)  
        top_indices = sorted_coef[:20]
        
    else:
        sorted_coef = np.argsort(abs(coef)) 
        top_indices = sorted_coef[-20:]
    
    print('Top 20 features are: ')
    print(feature_names[top_indices])

    
def analyze_run(model = 'model.pkl', data = 'vectorized.pkl'):
# str(sys.argv)[1]  pickle file with model, true_labels and feature_names
# str(sys.argv)[2]  vectorized test data (pickle file with all feature data)


# with open('model.pkl', "rb") as f:
#     model,y_test,feature_names = pickle.load(f) 

# with open('vectorized.pkl', "rb") as f:
#     X_test = pickle.load(f)
    
    with open(model, "rb") as f:
        model,y_test,feature_names = pickle.load(f) 

    with open(data, "rb") as f:
        X_test = pickle.load(f)

    y_pred = model.predict(X_test)
    print('Accuracy of this model on test set: ', model.score(X_test, y_test))
    print_confusion_matrix(y_test,y_pred)
    print_top_20(model.coef_.ravel(),np.array(feature_names), nb = True )

if __name__ == '__main__':
    print(len((sys.argv)))
    analyze_run( str(sys.argv[1]) , str(sys.argv[2]) )
