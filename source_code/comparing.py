import os
from collections import namedtuple
import glob
import operator

HolderStructure = namedtuple("HolderStructure", ['type', 'pos1', 'pos2', 'sentence'])
result = {'ORG_TP': 0, 'ORG_FP': 0, 'ORG_FN': 0, 'PER_TP': 0, 'PER_FP': 0, 'PER_FN': 0,
          'MON_TP': 0, 'MON_FP': 0, 'MON_FN': 0}

TP_ORG_list = {}
FP_ORG_list = {}
FN_ORG_list = {}
TP_PER_list = {}
FP_PER_list = {}
FN_PER_list = {}
TP_MON_list = {}
FP_MON_list = {}
FN_MON_list = {}


def update_result (data, marker):
    if data == "ORGANIZATION" and marker == "TP":
        result["ORG_TP"] += 1
    elif data == "PERSON" and marker == "TP":
        result["PER_TP"] += 1
    elif data == "MONEY" and marker == "TP":
        result["MON_TP"] += 1

    elif data == "ORGANIZATION" and marker == "FP":
        result["ORG_FP"] += 1
    elif data == "PERSON" and marker == "FP":
        result["PER_FP"] += 1
    elif data == "MONEY" and marker == "FP":
        result["MON_FP"] += 1

    elif data == "ORGANIZATION" and marker == "FN":
        result["ORG_FN"] += 1
    elif data == "PERSON" and marker == "FN":
        result["PER_FN"] += 1
    elif data == "MONEY" and marker == "FN":
        result["MON_FN"] += 1


def update_result_words (data, marker, type):
    if marker == "TP" and type == "ORGANIZATION":
        if data in TP_ORG_list:
            TP_ORG_list[data] += 1
        else:
            TP_ORG_list[data] = 1
    elif marker == "FP" and type == "ORGANIZATION":
        if data in FP_ORG_list:
            FP_ORG_list[data] += 1
        else:
            FP_ORG_list[data] = 1
    elif marker == "FN" and type == "ORGANIZATION":
        if data in FN_ORG_list:
            FN_ORG_list[data] += 1
        else:
            FN_ORG_list[data] = 1
    elif marker == "TP" and type == "PERSON":
        if data in TP_PER_list:
            TP_PER_list[data] += 1
        else:
            TP_PER_list[data] = 1
    elif marker == "FP" and type == "PERSON":
        if data in FP_PER_list:
            FP_PER_list[data] += 1
        else:
            FP_PER_list[data] = 1
    elif marker == "FN" and type == "PERSON":
        if data in FN_PER_list:
            FN_PER_list[data] += 1
        else:
            FN_PER_list[data] = 1
    elif marker == "TP" and type == "MONEY":
        if data in TP_MON_list:
            TP_MON_list[data] += 1
        else:
            TP_MON_list[data] = 1
    elif marker == "FP" and type == "MONEY":
        if data in FP_MON_list:
            FP_MON_list[data] += 1
        else:
            FP_MON_list[data] = 1
    elif marker == "FN" and type == "MONEY":
        if data in FN_MON_list:
            FN_MON_list[data] += 1
        else:
            FN_MON_list[data] = 1


def print_stat():
    print("True Positive ORGANIZATION")
    sorted_list = reversed(sorted(TP_ORG_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("False Positive ORGANIZATION")
    sorted_list = reversed(sorted(FP_ORG_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("False Negative ORGANIZATION")
    sorted_list = reversed(sorted(FN_ORG_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("True Positive PERSON")
    sorted_list = reversed(sorted(TP_PER_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("False Positive PERSON")
    sorted_list = reversed(sorted(FP_PER_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("False Negative PERSON")
    sorted_list = reversed(sorted(FN_PER_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("True Positive MONEY")
    sorted_list = reversed(sorted(TP_MON_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 2:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("False Positive MONEY")
    sorted_list = reversed(sorted(FP_MON_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 1:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")
    print("False Negative MONEY")
    sorted_list = reversed(sorted(FN_MON_list.items(), key=operator.itemgetter(1)))
    for i in sorted_list:
        if i[1] >= 1:
            print("%d - %s" % (i[1], i[0]))
    print("-----------------------------------------------------------")

def clean_folder(spacy_folder):
    os.chdir(os.getcwd() + spacy_folder + "\\")
    files = glob.glob('*.ann')
    for filename in files:
        os.unlink(filename)

def compare(spacy_folder):
# spacy_folder = "\\new_spacy_exit\\"

    file_counter = 0
    for filename in glob.glob('data/actual/**/*.ann'):
        #print(file_counter)
        if filename.endswith('.ann'):

            file = open(os.getcwd() + "\\" + filename, 'r+')
            my_struct = []

            #Try to do function
            lines = file.read().splitlines()
            for line in lines:
                words = line.split()
                if words[1] == "ORGANIZATION" or words[1] == "PERSON" or words[1] == "MONEY":
                    my_struct.append(HolderStructure(words[1], words[2], words[3], words[4:]))
                #-----------------------
            file.close()

            file = open(os.getcwd() + spacy_folder + str(file_counter) + ".ann")
            file_counter += 1
            spacy_struct = []

            # Try to do function
            lines = file.read().splitlines()
            for line in lines:
                words = line.split()
                if words[1] == "ORGANIZATION" or words[1] == "PERSON" or words[1] == "MONEY":
                    spacy_struct.append(HolderStructure(words[1], words[2], words[3], words[4:]))
                    # -----------------------
            file.close()



            for ent in reversed(my_struct):
                for ent2 in reversed(spacy_struct):
                    if " ".join(ent.sentence).lower() == " ".join(ent2.sentence).lower() and ent.type == ent2.type:
                        update_result(ent.type, "TP")
                        update_result_words(str(ent.sentence), "TP", ent.type)

                        my_struct.remove(ent)
                        spacy_struct.remove(ent2)
                        break
                    elif " ".join(ent.sentence).lower() == " ".join(ent2.sentence).lower() and ent.type != ent2.type:

                        update_result(ent.type, "FN")
                        update_result(ent2.type, "FP")

                        # Adding to list
                        update_result_words(str(ent.sentence), "FN", ent.type)
                        update_result_words(str(ent2.sentence), "FP", ent2.type)

                        #if (' '.join(i.sentence) == "Bill Gates"):
                        #    print(file)
                        #    print(filename)
                        #    print("--------------------")

                        my_struct.remove(ent)
                        spacy_struct.remove(ent2)
                        break
                    elif ent.pos1 == ent2.pos1 and ent.pos2 == ent2.pos2 \
                            and ent.sentence != ent2.sentence:
                        print("WTF,its not same sentence,check f**** code")
                        print(ent.sentence)
                        print(ent2.sentence)


            for i in my_struct:
                update_result(i.type, "FN")
                update_result_words(str(i.sentence), "FN", i.type)

                #if (i.type == "MONEY"):
                #    print("FN ", i.sentence, " || -----------------", " || ", filename, " || ", file)

            for ii in spacy_struct:
                update_result(ii.type, "FP")
                update_result_words(str(ii.sentence), "FP", ii.type)

                #if (ii.type == "MONEY"):
                #    print("FP  ", "------------------- || ", ii.sentence, " || ", filename, " || ", file)


    precision_ORG = result["ORG_TP"] / (result["ORG_TP"] + result["ORG_FP"])
    precision_PER = result["PER_TP"] / (result["PER_TP"] + result["PER_FP"])
    precision_MON = result["MON_TP"] / (result["MON_TP"] + result["MON_FP"])

    recall_ORG = result["ORG_TP"] / (result["ORG_TP"] + result["ORG_FN"])
    recall_PER = result["PER_TP"] / (result["PER_TP"] + result["PER_FN"])
    recall_MON = result["MON_TP"] / (result["MON_TP"] + result["MON_FN"])

    f_ORG = (2 * precision_ORG * recall_ORG) / (precision_ORG + recall_ORG)
    f_PER = (2 * precision_PER * recall_PER) / (precision_PER + recall_PER)
    f_MON = (2 * precision_MON * recall_MON) / (precision_MON + recall_MON)

    print("ORG_TP", result["ORG_TP"], "MON_TP", result["MON_TP"], "PER_TP", result["PER_TP"])
    print("ORG_FP", result["ORG_FP"], "MON_FP", result["MON_FP"], "PER_FP", result["PER_FP"])
    print("ORG_FN", result["ORG_FN"], "MON_FN", result["MON_FN"], "PER_FN", result["PER_FN"])

    print("precision: ORG= %f || PER= %f || MON: %f" % (precision_ORG, precision_PER, precision_MON))
    print("recall:    ORG= %f || PER= %f || MON: %f" % (recall_ORG, recall_PER, recall_MON))
    print("f:         ORG= %f || PER= %f || MON: %f\n" % (f_ORG, f_PER, f_MON))

    #-------------------------------------------------------------------------------------------------
    print_stat()

    clean_folder(spacy_folder)