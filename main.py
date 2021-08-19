from PIL import Image
import config.traits_dict as td
import random
import csv
import os
import numpy as np

#dirname = os.path.dirname(__file__)
#
#with open((dirname + '/data/punks.csv'), 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile, delimiter=',',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    writer.writerow( ['Number'] + ['Background'] + ['Ptype'] + ['Mouth'] + ['Eyes'] + ['Beard'] + ['Accessory'] + ['Head'] + ['Psychadeliceyes'] + ['psychadelicptype'] + ['psychadelichead'] + ['psychadelicacc'] + ['psychadelicmouth'])


# background list
bgks = td.bg_dict.keys()
background = list(bgks)
print(background)


# ptype
ptk = td.type_dict.keys()
ptype = list(ptk)
print(ptype)


# mouth list
mks = td.mouth_dict.keys()
mouth = list(mks)
print(mouth)

#fmouth list
fmks = td.fmouth_dict.keys()
fmouth = list(fmks)
print(fmouth)

# eyes list
eks = td.eyes_dict.keys()
eyes = list(eks)
print(eyes)


# feyes list
feks = td.feyes_dict.keys()
feyes = list(feks)
print(feyes)


# beard list
bks = td.beard_dict.keys()
beard = list(bks)
print(beard)


# accessory list
ak = td.acc_dict.keys()
accessory = list(ak)
print(accessory)


# faccessory list
fak = td.facc_dict.keys()
faccessory = list(fak)
print(faccessory)


# head list
hk = td.head_dict.keys()
head = list(hk)
print(head)


# fhead list
fhk = td.fhead_dict.keys()
fhead = list(fhk)
print(fhead)


# psych-eyes list
pek = td.psych_dict.keys()
psychadeliceyes = list(pek)
print(psychadeliceyes)


# psych-type list
ptk = td.psych_dict.keys()
psychadelicptype = list(ptk)
print(psychadelicptype)


# psych-head list
phk = td.psych_dict.keys()
psychadelichead = list(phk)
print(psychadelichead)


# psych-accessory list
pak = td.psych_dict.keys()
psychadelicacc = list(pak)
print(psychadelicacc)

#psych-mouth list
pmk = td.psych_dict.keys()
psychadelicmouth = list(pmk)
print(psychadelicmouth)


#    def listToString(s): 
#        str1 = ""  
#        for ele in s: 
#            str1 += ele  
#            return str1 
#
#
#    for x in range(0, 100):
#        print('x: ' + str(x))
#
    # determine background
def bgchoice(background):
    bg = random.choices(background, weights = (100,100,115,100,75,115,75), k=1)[0]
    return bg
punk_bg = bgchoice(background)
print('Background:', punk_bg)


    # determine type
def ptypechoice(ptype):
    pt = random.choices(ptype, weights = (10, 20, 400, 600, 80), k=1)[0]
    return pt
punk_type = ptypechoice(ptype)

print('Type:', punk_type)


    # determine mouths
def mouthchoice(punk_type, fmouth, mouth):
    if punk_type == ['Female']:
		m = random.choices(fmouth, weights = (100, 200), k=1)[0]
		return m
    else:
		m = random.choices(mouth, weights = (10, 100, 300, 200), k=1)[0]
		return m

punk_mouth = mouthchoice(punk_type, mouth, fmouth)

print('Mouth:', punk_mouth)


'''    # determine accessory
def accessorychoice(accessory,faccessory):
    if punk_type == 'Male' or 'Ape' or 'Zomebie' or 'Alien':
        acc = random.choices(accessory, weights =(20, 40, 5, 30, 100, 15, 35), k=1)
        return acc
    else:
        acc = random.choices(faccessory, weights =(20, 40, 5, 30, 100, 15, 35), k=1)
        return acc
punk_acc = accessorychoice(accessory,faccessory)

print('Accessory:', punk_acc)



    # determine eyes
def eyeschoice(punk_type, feyes, eyes):
    if punk_type == [dirname + '/images/Type/female.png']:
        eyes = random.choices(feyes, weights = (30,50,30,40,50,40,60,40,50,40,10,30,150), k=1)
        return eyes
    else:
        eyes = random.choices(eyes, weights = (30,50,30,40,50,40,60,40,50,40,10,150), k=1)
        return eyes
punk_eyes = eyeschoice(punk_type, feyes, eyes)
print('Eyes:', punk_eyes)



    # determine head choice
def headchoice(punk_type, fhead, head):
    if punk_type == [dirname + '/images/Type/female.png']:
        head = random.choices(fhead, weights = (50, 5, 30, 30, 30, 20, 30, 50, 30, 30, 40, 40, 40, 5, 30, 40, 10, 20, 20, 10, 15), k=1)
        return head
    else:
        head = random.choices(head, weights = (50, 5, 30, 30, 30, 20, 30, 50, 30, 30, 40, 40, 40, 5, 30, 40, 10), k=1)
        return head
punk_head = headchoice(punk_type, fhead, head)
print('Head:', punk_head)

    # determine beard
def beardchoice(punk_type, beard):
    if punk_type == [dirname + '/images/Type/male.png']:
        b = random.choices(beard, weights = (50, 40 ,30 ,2 ,3 ,3 ,200), k=1)
        return b
    elif punk_type == [dirname + '/images/Type/zombie.png']:
        b = random.choices(beard, weights = (50, 40 ,30 ,2 ,3 ,3 ,200), k=1)
        return b
    else:
        b = random.choices(beard, weights = (0, 0 ,0 ,0 ,0 ,0 ,100), k=1)
        return b
punk_beard = beardchoice(punk_type ,beard)
print('Beard:', punk_beard)
    


    # determine psych-eyes
def psycheyes(psychadeliceyes):
    peyes = random.choices(psychadeliceyes, weights = (10, )*41, k = 1)
    return peyes
psych_eyes = psycheyes(psychadeliceyes)
print('Psych-eyes:', psych_eyes)

    # determine psych-type
def psychtype(psychadelicptype):
    ptype = random.choices(psychadelicptype, weights = (10, )*41, k = 1)
    return ptype
psych_type = psychtype(psychadelicptype)
print('Psych-type:', psych_type)

    # determine psych-head
def psychhead(psychadelichead):
    phead = random.choices(psychadelichead, weights = (10, )*41, k = 1)
    return phead
psych_head = psychhead(psychadelichead)
print('Psych-head:', psych_head)

    # determine psych-accessory
def psychacc(psychadelicacc):
    peyes = random.choices(psychadelicacc, weights = (10, )*41, k = 1)
    return peyes
psych_acc = psychacc(psychadelicacc)
print('Psych-accessory:', psych_acc)

    # determine psych-mouth
def psychmouth(psychadelicmouth):
    pmouth = random.choices(psychadelicmouth, weights = (10, )*41, k = 1)
    return pmouth
psych_mouth = psychmouth(psychadelicmouth)
print('Psych-mouth:', psych_mouth)'''



#        bgimg = listToString(punk_bg)
#        with Image.open(bgimg) as bgimg:
#            bga = np.asarray(bgimg)
#            
#            
#        
#        typeimg = listToString(punk_type)
#        with Image.open(typeimg) as typeimg:
#            ta = np.asarray(typeimg)
#
#        mouthimg = listToString(punk_mouth)
#        with Image.open(mouthimg) as mouthimg:
#            ma = np.asarray(mouthimg)
#
#
#		eyesimg = listToString(punk_eyes)
#		with Image.open(eyesimg) as eyesimg:
#			ea = np.asarray(eyesimg)
#
#		beardimg = listToString(punk_beard)
#		with Image.open(beardimg) as beardimg:
#			ba = np.asarray(beardimg)
#
#        accessoryimg = listToString(punk_acc)
#        with Image.open(accessoryimg) as accessoryimg:
#            aa = np.asarray(accessoryimg)
#            
#
#        headimg = listToString(punk_head)
#        with Image.open(headimg) as headimg:
#            ha = np.asarray(headimg)
#        
#        psycheimg = listToString(psychadeliceyes)
#        with Image.open(psycheimg) as psycheimg:
#            pea = np.asarray(psycheimg)
#        
#
#        psychpimg = listToString(psych_type)
#        with Image.open(psychpimg) as psychpimg:
#            ppa = np.asarray(psychpimg)
#            
#
#        psychhimg = listToString(psych_head)
#        with Image.open(psychhimg) as psychhimg:
#            pha = np.asarray(psychhimg)
#            
#
#        psychaimg = listToString(psych_acc)
#        with Image.open(psychaimg) as psychaimg:
#            paa = np.asarray(psychaimg)
#            
#
#        psychmimg = listToString(psych_mouth)
#        with Image.open(psychmimg) as psychmimg:
#            pma = np.asarray(psychmimg)
#
#        def comb1():
#            background = Image.fromarray(bga)
#            typeoverlay = Image.fromarray(ta)
#            typeoverlay = typeoverlay.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - typeoverlay.width) // 2
#            height = (background.height - typeoverlay.height) // 2
#            background.paste(typeoverlay, (width, height), typeoverlay)
#            background.save(dirname + '/temp2/bg_type.png', format="png")
#        
#        def removewhitetype():
#            img = Image.open(dirname + '/temp2/bg_type.png')
#            img = img.convert("RGBA")
#            datas = img.getdata()
#
#            newData = []
#            for item in datas:
#                if item[0] == 255 and item[1] == 255 and item[2] == 255:
#                    newData.append((255, 255, 255, 0))
#                else:
#                    newData.append(item)
#
#            img.putdata(newData)
#            img.save(dirname + "/temp2/whiteremove.png", "PNG")
#            
#
#        def psychtypeimg():
#            os.remove(dirname + "/temp2/bg_type.png")
#            filename1 = Image.fromarray(ppa)
#            width, height = filename1.size
#            imagee_size = width, height
#            portion_size = (337,337)
#
#            x1 = random.randint(0, imagee_size[0]-portion_size[0]-1)
#            y1 = random.randint(0, imagee_size[1]-portion_size[1]-1)
#
#            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
#
#            coords = (x1,y1,x2,y2)
#        
#            newimgf = filename1.crop(coords)
#            newimgf.putalpha(200)
#            newimgf.save(dirname + '/temp2/resizepsycht.png')
#
#            filename = (dirname + '/temp2/whiteremove.png')
#            frontImage = Image.open(filename)
#            background = Image.open(dirname + '/temp2/resizepsycht.png')
#            whitefile = (dirname + '/images/white.png')
#            white = Image.open(whitefile)
#            frontImage = frontImage.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - frontImage.width) // 2
#            height = (background.height - frontImage.height) // 2
#            white.paste(background, (width, height), background)
#            white.save(dirname + '/temp2/whiteadded.png')
#            
#        def white():
#            filename = (dirname + '/temp2/whiteadded.png')
#            filename2 = (dirname + '/temp2/whiteremove.png')
#            add = Image.open(filename)
#            remove = Image.open(filename2)
#            add = add.convert("RGBA")
#            remove = remove.convert("RGBA")
#            width = (add.width - remove.width) // 2
#            height = (add.height - remove.height) // 2
#            add.paste(remove, (width, height), remove)
#            add.save(dirname + "/temp2/base.png", format="png")
#
#
#            
#            
#
#        def comb2():
#            eyeoverlay = Image.fromarray(aa)
#            background = Image.open(dirname + '/temp2/base.png')
#            eyeoverlay = eyeoverlay.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - eyeoverlay.width) // 2
#            height = (background.height - eyeoverlay.height) // 2
#            background.paste(eyeoverlay, (width, height), eyeoverlay)
#            background.save(dirname + '/temp2/accadded.png', format="png")
#
#        def removewhiteeye():
#            img = Image.open(dirname + '/temp2/accadded.png')
#            img = img.convert("RGBA")
#            datas = img.getdata()
#
#            newData = []
#            for item in datas:
#                if item[0] == 255 and item[1] == 255 and item[2] == 255:
#                    newData.append((255, 255, 255, 0))
#                else:
#                    newData.append(item)
#
#            img.putdata(newData)
#            img.save(dirname + "/temp2/whiteremove.png", "PNG")
#
#        def accpsych():
#            filename1 = Image.fromarray(paa)
#            width, height = filename1.size
#            imagee_size = width, height
#            portion_size = (337,337)
#
#            x1 = random.randint(0, imagee_size[0]-portion_size[0]-1)
#            y1 = random.randint(0, imagee_size[1]-portion_size[1]-1)
#
#            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
#
#            coords = (x1,y1,x2,y2)
#        
#            newimgf = filename1.crop(coords)
#            newimgf.putalpha(200)
#            newimgf.save(dirname + '/temp2/resizepsycht.png')
#
#            filename = (dirname + '/temp2/resizepsycht.png')
#            background = Image.open(filename)
#
#            whitefile = (dirname + '/images/white.png')
#            white = Image.open(whitefile)
#            white = white.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - white.width) // 2
#            height = (background.height - white.height) // 2
#            white.paste(background, (width, height), background)
#            white.save(dirname + '/temp2/whiteadded.png')
#
#        def white2():
#            
#            filename = (dirname + '/temp2/whiteadded.png')
#            filename2 = (dirname + '/temp2/whiteremove.png')
#            add = Image.open(filename)
#            remove = Image.open(filename2)
#            add = add.convert("RGBA")
#            remove = remove.convert("RGBA")
#            width = (add.width - remove.width) // 2
#            height = (add.height - remove.height) // 2
#            add.paste(remove, (width, height), remove)
#            add.save(dirname+'/fin/PsychPunk_'+str(x)+'.png', 'PNG')
#            
#            
#            
#            
#        def delstuff():
#            os.remove(dirname + '/temp2/whiteadded.png')
#            os.remove(dirname + '/temp2/whiteremove.png')
#            os.remove(dirname + '/temp2/resizepsycht.png')
#
#        def delstuff2():
#            os.remove(dirname + '/temp2/whiteadded.png')
#            os.remove(dirname + '/temp2/whiteremove.png')
#            os.remove(dirname + '/temp2/accadded.png')
#
#        def delstuff3():
#            
#            os.remove(dirname + '/temp2/resizepsycht.png')
#            os.remove(dirname + '/temp2/whiteadded.png')
#            os.remove(dirname + '/temp2/whiteremove.png')
#            os.remove(dirname + '/temp2/accadded.png')
#            os.remove(dirname + '/temp2/base.png')
#            
#        
#
#        def comb3():
#            eyeoverlay = Image.fromarray(ha)
#            background = Image.open(dirname + '/temp2/base.png')
#            eyeoverlay = eyeoverlay.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - eyeoverlay.width) // 2
#            height = (background.height - eyeoverlay.height) // 2
#            background.paste(eyeoverlay, (width, height), eyeoverlay)
#            background.save(dirname + '/temp2/accadded.png', format="png")
#
#        def removewhitehead():
#            img = Image.open(dirname + '/temp2/accadded.png')
#            img = img.convert("RGBA")
#            datas = img.getdata()
#
#            newData = []
#            for item in datas:
#                if item[0] == 255 and item[1] == 255 and item[2] == 255:
#                    newData.append((255, 255, 255, 0))
#                else:
#                    newData.append(item)
#
#            img.putdata(newData)
#            img.save(dirname + "/temp2/whiteremove.png", "PNG")
#
#        def headpsych():
#            filename1 = Image.fromarray(pha)
#            width, height = filename1.size
#            imagee_size = width, height
#            portion_size = (337,337)
#
#            x1 = random.randint(0, imagee_size[0]-portion_size[0]-1)
#            y1 = random.randint(0, imagee_size[1]-portion_size[1]-1)
#
#            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
#
#            coords = (x1,y1,x2,y2)
#        
#            newimgf = filename1.crop(coords)
#            newimgf.putalpha(200)
#            newimgf.save(dirname + '/temp2/resizepsycht.png')
#
#            filename = (dirname + '/temp2/resizepsycht.png')
#            background = Image.open(filename)
#
#            whitefile = (dirname + '/images/white.png')
#            white = Image.open(whitefile)
#            white = white.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - white.width) // 2
#            height = (background.height - white.height) // 2
#            white.paste(background, (width, height), background)
#            white.save(dirname + '/temp2/whiteadded.png')
#            
#
#        def eyepsych():
#            filename1 = Image.fromarray(pea)
#            width, height = filename1.size
#            imagee_size = width, height
#            portion_size = (337,337)
#
#            x1 = random.randint(1, imagee_size[0]-portion_size[0]-1)
#            y1 = random.randint(1, imagee_size[1]-portion_size[1]-1)
#
#            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
#
#            coords = (x1,y1,x2,y2)
#        
#            newimgf = filename1.crop(coords)
#            newimgf.putalpha(200)
#            newimgf.save(dirname + '/temp2/resizepsycht.png')
#
#            filename = (dirname + '/temp2/resizepsycht.png')
#            background = Image.open(filename)
#
#            whitefile = (dirname + '/images/white.png')
#            white = Image.open(whitefile)
#            white = white.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - white.width) // 2
#            height = (background.height - white.height) // 2
#            white.paste(background, (width, height), background)
#            white.save(dirname + '/temp2/whiteadded.png')
#
#        def comb4():
#            eyeoverlay = Image.fromarray(ea)
#            background = Image.open(dirname + '/temp2/base.png')
#            eyeoverlay = eyeoverlay.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - eyeoverlay.width) // 2
#            height = (background.height - eyeoverlay.height) // 2
#            background.paste(eyeoverlay, (width, height), eyeoverlay)
#            background.save(dirname + '/temp2/accadded.png', format="png")
#
#
#
#        def comb5():
#            eyeoverlay = Image.fromarray(ba)
#            background = Image.open(dirname + '/temp2/base.png')
#            eyeoverlay = eyeoverlay.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - eyeoverlay.width) // 2
#            height = (background.height - eyeoverlay.height) // 2
#            background.paste(eyeoverlay, (width, height), eyeoverlay)
#            background.save(dirname + '/temp2/accadded.png', format="png")
#
#
#        def beardpsych():
#            white = Image.open(dirname + '/temp2/accadded.png')
#            white.save(dirname + '/temp2/whiteadded.png')
#
#        def mouthhimg():
#            eyeoverlay = Image.fromarray(ma)
#            background = Image.open(dirname + '/temp2/base.png')
#            eyeoverlay = eyeoverlay.convert("RGBA")
#            background = background.convert("RGBA")
#            width = (background.width - eyeoverlay.width) // 2
#            height = (background.height - eyeoverlay.height) // 2
#            background.paste(eyeoverlay, (width, height), eyeoverlay)
#            background.save(dirname + '/temp2/base.png', format="png")
#
#        def delstuff1():
#            os.remove(dirname + '/temp2/resizepsycht.png')
#            os.remove(dirname + '/temp2/whiteadded.png')
#            os.remove(dirname + '/temp2/whiteremove.png')
#            os.remove(dirname + '/temp2/accadded.png')
#
#
#        #bg and type creation
#        comb1()
#        removewhitetype()
#        psychtypeimg()
#        white()
#        delstuff()
#
#        #eyes
#        comb4()
#        removewhiteeye()
#        eyepsych()
#        white()
#        delstuff1()
#
#        #mouth
#        mouthhimg()
#
#        #beard
#        comb5()
#        removewhiteeye()
#        beardpsych()
#        white()
#        delstuff2()
#
#        #Head
#        comb3()
#        removewhitehead()
#        headpsych()
#        white()
#        delstuff1()
#
#        #accessory
#        comb2()
#        removewhiteeye()
#        accpsych()
#        white2()
#        delstuff3()




#        row = x
#        print('row :' + str(row))
#        writer.writerow([row, punk_bg, punk_type, punk_mouth, punk_eyes, punk_beard, punk_acc, punk_head, psych_eyes, psych_type, psych_head, psych_acc, psych_mouth])
#        print('----------------------')
#    else:
#        print('----------------------')
