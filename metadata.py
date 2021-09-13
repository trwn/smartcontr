import csv
import os
import json
import pandas as pd

dirname = os.path.dirname(__file__)

# csv_file = pd.read_csv(dirname + '/data/punks.csv')
# x=0
# z=1
# BASE_URI = 'https://ipfs.io/ipfs/QmfDvmohyZASHixyQKoK38h4tM8DaB8gTMCFqhxDVy9XZ9'


# while x <= 100:
#     csv_file.loc[x,'image:'] = BASE_URI + '/PsychPunk_' + str(z) + '.png'
    
#     x += 1
#     z += 1
# csv_file.to_csv(dirname + '/data/punks.csv', index=False)


csv_file = open(dirname + '/data/punks.csv','r')
csv_reader = csv.DictReader(csv_file,fieldnames = ('image:','Name:','Background:', 'Type:', 'Mouth:', 'Accessory:', 'Eyes:', 'Hair:', 'Beard:', 'Psych DNA:'))




lcount = 0
for row in csv_reader:
    out = json.dumps(row, indent=4)

    jsonoutput = open(dirname + '/metadata/PsychPunk_'+str(lcount)+'.json','w')
    jsonoutput.write(out)
    lcount+=1
# os.remove(dirname + '/metadata/PsychPunk_0.json')
jsonoutput.close()
csv_file.close()
