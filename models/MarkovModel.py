
""" This takes in a Tokenized pandas dataframe column and creates a dictionary from it """

import pandas as pd
import numpy as np
from numpy.random import choice

def create_dictionary(tokenized_column):
    """ Creates a dictionary from a tokenized column, this dictionary will be used to create a transition probability matrix """
    
    # Getting the list of all words 
    words = []
    for row in tokenized_column:
        for i in range(len(row)):
            words.append(row[i])

    # Creating dictionary dataframe
    # This dataframe will serve as a dictionary
    # column "lead" will store 1st word
    # colum "follow" will store the word that follows the corresponding lead word
    # This would eventually result in a 2nd Order Markov Model

    lead = []
    follow = []
    count = 0

    for row in tokenized_column:
        for i in range(len(row)-1):
            lead.append(row[i])
            follow.append(row[i+1])

    dict_df = pd.DataFrame(columns = ['lead', 'follow', 'freq'])
    dict_df['lead'] = lead
    dict_df['follow'] = follow
    dict_df['freq']= dict_df.groupby(by=['lead','follow'])['lead','follow'].transform('count').copy()
    dict_df = dict_df.drop_duplicates()
    dict_df['freq'] = dict_df['freq'].fillna(0.0).astype(float)
    dict_df = dict_df.dropna()

    # end words will be used to end our generated sentences (attempt to make sentences logically resonable)
    end_words = []
    for word in words:
        if word[-1] in ['.','!','?'] and word != '.':
            end_words.append(word)

    return dict_df, end_words

def transition_probability_matrix(dictionary):
    """ Creates a transition probability matrix from given dictionary """
    small_dict = dictionary[0:100000]
    prob_matrix = small_dict.pivot(index = 'lead', columns= 'follow', values='freq')
    sum_words = prob_matrix.sum(axis=1)
    prob_matrix = prob_matrix.apply(lambda x: x/sum_words)

    return prob_matrix

def make_a_sentence(start, prob_matrix, end_words):
    """ Generates sentences starting with the start word and until an end word """

    word= start
    # our sentence starts from word
    sentence=[word]
    # restrict length of our sentence
    while len(sentence) < 30:
        # numpy choice picks a word using transition probability matrix
        next_word = choice(a = list(prob_matrix.columns), p = (prob_matrix.iloc[prob_matrix.index ==word].fillna(0).values)[0])
        if next_word == 'EndWord':
                continue
        elif next_word in end_words:
            if len(sentence) > 2:    
                sentence.append(next_word)
                break
            else :
                continue
        else :
            sentence.append(next_word)
        word=next_word
    sentence = ' '.join(sentence)
    return sentence