from dataset import load_data
from dependency import *
from feature_extraction_da import get_features_da
from sklearn.svm import *
from sklearn.linear_model import SGDClassifier
from utils import *
import numpy as np
import pickle

def train_svm_da(data):
    X,y = get_feature_vectors_for_training_da(data)
    print("Number of training samples : " + str(y.shape[0]))
    print("Number of features : "+str(X.shape[1]))
    print("Training model")
    model = LinearSVC()
    model.fit(X,y)
    print("Completed")
    return model

def get_feature_vectors_for_training_da(data):
    projective_tree_count = 0
    projective_non_parsable = []
    X = []
    y = []
    for id,sent_dict in data.items():
        if len(sent_dict['FORM']) == 1:
           #Example : train file, line 97384. Text : '************************'
            continue
        gold_arcs = get_gold_arcs(sent_dict['HEAD'])
        buff = [i for i in range(len(sent_dict['FORM']))[::-1]]
        projective = is_projective(gold_arcs, len(sent_dict['FORM']))

        if not projective:
            continue
        try:
            dgraph, configurations = make_transitions(buff, oracle_std, gold_arcs)
        except IndexError:
            projective_non_parsable.append(sent_dict)
            continue

        for config in configurations:
            X.append(get_features_da(config[:2],sent_dict))
            y.append(config[2])
        # Root missing.
        if set(gold_arcs)-set(dgraph):
            print("Missing arcs",set(gold_arcs)-set(dgraph))
        projective_tree_count+=1

    feature_values = set([feature for row in X for feature in row])
    feature_dict = {feature: i for i, feature in enumerate(feature_values)}
    with open('feature_dict_da.pkl', 'wb') as f1:
        pickle.dump(feature_dict,f1)

    X_ = one_hot_encoding(X,feature_dict)
    a = 0.0
    for i in range(len(X_)):
        b = float(sum(X_[i]))
        c = float(len(X[i]))
        a += b
    y = np.array(y)

    print("Number of valid projection trees : "+str(projective_tree_count))
    return X_,y


def train_model_da(data):
    # TODO

    model = train_svm_da(data)

    with open('model_da.pkl','wb') as f:
        pickle.dump(model,f)
        
    return model

    #raise NotImplementedError

