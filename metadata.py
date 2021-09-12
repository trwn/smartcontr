import csv
import os
import json

dirname = os.path.dirname(__file__)

csv_file = open(dirname + '/data/punks.csv','r')
csv_reader = csv.DictReader(csv_file,fieldnames = ('image:','Name:','Background:', 'Type:', 'Mouth:', 'Accessory:', 'Eyes:', 'Hair:', 'Beard:', 'Psych DNA:'))

lcount = 0
for row in csv_reader:
    out = json.dumps(row, indent=4)

    jsonoutput = open(dirname + '/fin/PsychPunk_'+str(lcount)+'.json','w')
    jsonoutput.write(out)
    lcount+=1
os.remove(dirname + '/fin/PsychPunk_0.json')
jsonoutput.close()
csv_file.close()
