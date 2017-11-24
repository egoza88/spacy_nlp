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
    for filename in glob.glob('train_data/actual/**/*.ann'):
        data_list = []
        ann_file = open(os.getcwd() + "\\" + filename, 'r+')
        filename1 = filename[0:len(filename) - 3] + "txt"
        txt_file = open(os.getcwd() + "\\" + filename1, 'r+')

        temp = txt_file.read().splitlines()
        veta = temp[2]

        for line in ann_file.read().splitlines():
            words = line.split()
            if words[1] == "PERSON" or words[1] == "MONEY":
                data_list.append((int(words[2]) - 31, int(words[3]) - 31, words[1]))
            elif words[1] == "ORGANIZATION":
                data_list.append((int(words[2]) - 31, int(words[3]) - 31, 'ORG'))

        # print(data_list)
        train_data.append((veta, data_list))

        # data_list.clear()
        ann_file.close()
        txt_file.close()
    print(train_data)
    return train_data


def train_ner(train_data):
   # Add new words to vocab.


    # for raw_text, _ in train_data:
    #     doc = nlp.make_doc(raw_text)
    #     for word in doc:
    #     _ = nlp.vocab[word.orth]
   #
   # Train NER.
   #  ner = EntityRecognizer(nlp.vocab, entity_types=entity_types)
   #
   #  for itn in range(3):
   #      random.shuffle(train_data)
   #      for raw_text, entity_offsets in train_data:
   #          doc = nlp.make_doc(raw_text)
   #          gold = GoldParse(doc, entities=entity_offsets)
   #          ner.update(doc, gold)
   #  ner.model.end_training()


    # -----------------------------------1.9
    # nlp = spacy.load('en')
    nlp = spacy.load('en_core_web_md')
    # -----------------------------------2.0
    # nlp = spacy.load('en_core_web_sm')
    # nlp = spacy.load('en_core_web_lg')

    for itn in range(10):
         print(itn)
         random.shuffle(train_data)
         for raw_text, entity_offsets in train_data:
             doc = nlp.make_doc(raw_text)
             gold = GoldParse(doc, entities=entity_offsets)

             # spacy 1.9
             nlp.entity.update(doc, gold)

             # spacy 2.0
             # nlp.entity.update([doc], [gold])

    return nlp


def main(model_dir=None):
    start_time = time.time()

    train_data = []

    prepare_data(train_data)

    nlp = train_ner(train_data)

    #------------------------------------------------------------------
    with open("output.txt", 'r') as input_f:
        lines = input_f.read().splitlines()
        file_counter = 0
        for line in lines:
            output_f = open(os.getcwd() + '\\new_spacy_exit\\' + str(file_counter) + '.ann', 'w')
            file_counter += 1
            # print(file_counter)

            doc = nlp(line)
            # nlp.tagger(doc)
            # ner(doc)
            end_point = 0
            from_ = 0
            to_ = 0
            counter = 1
            for ent in doc.ents:
                from_ = line.find(ent.text, end_point)
                to_ = from_ + len(ent.text)
                end_point = to_

                #print(ent.label_)
                if ent.label_ == 'ORG':
                    output_f.write("T%d ORGANIZATION " % counter)
                elif ent.label_ == 'PERSON':
                    output_f.write("T%d PERSON " % counter)
                elif ent.label_ == 'MONEY':
                    output_f.write("T%d MONEY " % counter)
                else:
                    continue

                output_f.write("%d %d\t%s\n" % (from_ + 31, to_ + 31, ent.text))
                counter += 1

            output_f.close()
        input_f.close()
        print("--- %s seconds ---" % (time.time() - start_time))
        print("SUCCES")
        comparing.compare("\\new_spacy_exit\\")

if __name__ == '__main__':
    main('ner')