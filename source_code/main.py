import os
import glob
import spacy
import en_core_web_sm

output_f = open('output.txt', 'w')
counter = 0

for filename in glob.glob('data/actual/**/*.txt'):

    file = open(os.getcwd() + "\\" + filename, 'r')
    content = file.read()
    lines = content.splitlines()
    output_f.write(lines[2] + '\n')
    file.close()
    print(filename)
    counter+=1

output_f.close()
print("SUCCES")