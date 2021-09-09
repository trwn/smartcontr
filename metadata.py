import csv
import os
import json

dirname = os.path.dirname(__file__)

csv_file = open(dirname + '/data/punks.csv','r')
csv_reader = csv.DictReader(csv_file,fieldnames = ('Name:','Background:', 'Type:', 'Mouth:', 'Accessory:', 'Eyes:', 'Hair:', 'Beard:', 'Psych DNA:'))

lcount = 0
for row in csv_reader:
    out = json.dumps(row, indent=4)

    jsonoutput = open(dirname + '/fin/PsychPunk'+str(lcount)+'.json','w')
    jsonoutput.write(out)
    lcount+=1
jsonoutput.close()
csv_file.close()
