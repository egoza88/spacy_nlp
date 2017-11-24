import os
import spacy
import en_core_web_sm
import glob
import time
import numpy
import comparing

start_time = time.time()

# ----------------1.9
# nlp = spacy.load('en')
nlp = spacy.load('en_core_web_md')

# ----------------2.0
# nlp = spacy.load('en_core_web_lg')
# nlp = spacy.load('en_core_web_sm')

with open("output.txt", 'r') as input_f:
#input_f = open("output.txt", 'r')

    lines = input_f.read().splitlines()
    file_counter = 0
    for line in lines:
        output_f = open(os.getcwd() + '\\spacy_exit\\' + str(file_counter) + '.ann', 'w')
        file_counter += 1
        # print(file_counter)

        doc = nlp(line)
        end_point = 0
        from_ = 0
        to_ = 0
        counter = 1

        for ent in doc.ents:
            from_ = line.find(ent.text, end_point)
            to_ = from_ + len(ent.text)
            end_point = to_


            #print(ent.label_)
            if ent.label_ == 'ORG': output_f.write("T%d ORGANIZATION " % counter)
            elif ent.label_ == 'PERSON': output_f.write("T%d PERSON " % counter)
            elif ent.label_ == 'MONEY': output_f.write("T%d MONEY " % counter)
            else: continue

            output_f.write("%d %d\t%s\n" % (from_ + 31, to_ + 31, ent.text))
            counter += 1

        output_f.close()
    #input_f.close()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("SUCCES")
    comparing.compare("\\spacy_exit\\")








