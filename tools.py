__author__ = 'minh'
'''
weighted_random module makes it easier to do weighted random
'''
import random
import string

#weighted choices takes in a dictionary of choices to weight
#and returns randomly a choice given by weights(ints)
def weighted_choice(weights):
    #TODO: stupid way to doing this, I know
    m_list = []
    for obj in weights:
        for times in range(0, weights[obj]):
            m_list.append(obj)
    return random.choice(m_list)

#removes punctuation from a string
#TODO: understand why this is fastest
def strip_punctuation(s):
    return s.translate(s.maketrans("","", string.punctuation))