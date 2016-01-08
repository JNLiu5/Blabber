#extra libraries used
import queue
import tools
import random

"""
markov_chain class is a class that creates a(n) markov chain statistical
model on an inputted list of objects.

The class is then able to generate randomly a new list of objects based
on the analysis model of the inputted list.
"""
class markov_chain:
    
    """
    Class constructor, at the very minium, the class needs an inputted list of
    objects the level parameter is extra to specify the level of the markov
    chain
    """
    def __init__(self, obj_list:list, level:int = 1):
        self.level = level #level class variable
        self.obj_list = obj_list #list of objects
        self.pair_tb = {}
        self.__fill_pair_tb(obj_list)
        self.prob_tb = {}
        self.generate_prob_table()


    """
    Populates dictionary of words to tuples of succeeding words. Used to make
    generate_prob_table easier.
    """
    def __fill_pair_tb(self, obj_list):
        previous = ""
        for item in obj_list:
            if previous != "":
                nxt = (item, )
                if previous in self.pair_tb:
                    self.pair_tb[previous] = self.pair_tb[previous] + nxt
                else:
                    self.pair_tb[previous] = nxt
            previous = item
        
    """
    generate_prob_table goes through the list of objects and generates a probability
    table of current object to the previous object that can be used to look up again.

    Uses a dictionary of words to tuples of dictionaries of succeeding words to count.
    i.e. { word1 -> ( { wordA, countA }, { wordB, countB } ), word2 ->... }
    """

    def generate_prob_table(self):
        for key in self.pair_tb:
            for value in self.pair_tb[key]:
                tup = ( { value: 1 }, )
                if key in self.prob_tb:
                    found = False
                    for dict1 in self.prob_tb[key]:
                        if value in dict1:
                            dict1[value] += 1
                            found = True
                            break
                    if not found:
                        self.prob_tb[key] = self.prob_tb[key] + tup
                else:
                    self.prob_tb[key] = tup


    """
    generate_random_list uses the probability table and returns a list of
    objects that adheres to the probability table generated in the previous
    method
    NOTE: the first object has to be selected randomly(the seed)
    NOTE: the count parameter is just to specify the length of the generated
    list
    """
    def generate_obj_list(self, count:int = 10):
        unique = set(self.obj_list)
        y = random.sample(unique, 1)
        rand = y[0]
        randList = []
        itemCount = 0
        #appends count items to randList
        while itemCount < count:
            randList.append(rand)
            itemCount += 1
            #selects random succeeding word self.level times, in order to 
            #allow for nth-degree chains
            for x in range(self.level):
                possibles = ()
                #if the current word is not in the prob_tb (ex. the last 
                #word in the text only appears once), choose another
                while rand not in self.prob_tb:
                    x = random.sample(unique, 1)
                    rand = x[0]
                #steps through every dictionary in the corresponding tuple
                #in prob_tb
                for d in self.prob_tb[rand]:
                    #steps through every word-count pair in the dictionary
                    for key, value in d.items():
                        #adds key to possibles value times to allow for
                        #weighted probabilities
                        for i in range(value):
                            tmp = ( key, )
                            possibles += tmp
                rand = random.choice(possibles)
        return randList


    #TODO repeat until you from a count length list. NOTE: for an nth level
    #markov chain you will need to look up on the probability an n-length tuple
    #once you've generated enough words!
