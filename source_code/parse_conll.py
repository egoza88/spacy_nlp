import spacy
import os
from collections import namedtuple
import glob
import operator
import spacy
import random
from spacy.gold import GoldParse
from spacy.language import EntityRecognizer
from spacy.gold import GoldParse
import time
import comparing


def prepare_data(train_data):
    counter = 0
    filename = ('train_data/conll/bla.train.txt')
    # data_list = []
    ann_file = open(os.getcwd() + "\\" + filename, 'r+')

    veta = ""
    # dictionary['entities'].append(line[1])


    for line in ann_file.read().splitlines():
        words = line.split()

        if (len(words) == 0 or words[0][0] == "." or words[0][0] == "-") and veta == "":
            data_list = []
            dictionary = dict()
            continue
        elif len(words) == 0 or words[0][0] == "." or words[0][0] == "-":
            for line in data_list:
                if 'entities' in dictionary:
                    # append the new number to the existing array at this slot
                    dictionary['entities'].append(line)
                else:
                    # create a new array in this slot
                    dictionary['entities'] = [line]

            train_data.append((veta, dictionary))

            # for list in data_list:
            #     print(list[0], " ", list[1], " ", list[2])

            veta = ""
            # data_list.clear()
            words.clear()

            data_list = []
            dictionary = dict()
            continue

        veta = veta + words[0] + ' '

        if words[3] == "I-ORG":
            data_list.append((len(veta)-len(words[0])-1, len(veta)-1, 'ORG'))
        elif words[3] == "I-MISC":
            data_list.append((len(veta)-len(words[0])-1, len(veta)-1, 'GPE'))
        elif words[3] == "I-PER":
            data_list.append((len(veta)-len(words[0])-1, len(veta)-1, 'PERSON'))
        elif words[3] == "I-LOC":
            data_list.append((len(veta)-len(words[0])-1, len(veta)-1, 'LOC'))

    ann_file.close()

    return train_data


def main():
    train_data = []
    prepare_data(train_data)
    # print("test")
    for i in range(0, 4):
        print(train_data[i])
    # abc = "123456"
    # print(abc[0])

if __name__ == '__main__':
    main()