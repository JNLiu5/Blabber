import markov
import tools
import string

class sentence_generator(markov.markov_chain):
    def __init__(self, filename, level=1):
        try:
            raw_file = open(filename)
            raw_txt = raw_file.read()
            raw_file.close()
            words_list = self.__clean_raw_file__(raw_txt).split()
            super().__init__(words_list, level)
        except IOError:
            print("IO Error: File " + filename + "does not exist!")


    #cleans up raw file by simplifying text
    #such as removing punctuation, lowercase, etc
    def __clean_raw_file__(self,raw):
        str_lower = raw.lower()
        return tools.strip_punctuation(str_lower)

    #maybe implement a recursive grammar chain
    def generate_sentence(self, length = 10):
        sentence = super().generate_obj_list(length)
        for word in sentence:
            print (word,end=" ")
        print("\n")
