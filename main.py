from PIL import Image
import config.traits_dict as td
import random
import csv
import os
import numpy as np


dirname = os.path.dirname(__file__)


# background list
bgks = td.bg_dict.keys()
background = list(bgks)
#print(background)


# ptype
ptk = td.type_dict.keys()
ptype = list(ptk)
#print(ptype)


# mouth list
mks = td.mouth_dict.keys()
mouth = list(mks)
#print(mouth)

#fmouth list
fmks = td.fmouth_dict.keys()
fmouth = list(fmks)
#print(fmouth)

# eyes list
eks = td.eyes_dict.keys()
eyes = list(eks)
#print(eyes)


# feyes list
feks = td.feyes_dict.keys()
feyes = list(feks)
#print(feyes)


# beard list
bks = td.beard_dict.keys()
beard = list(bks)
#print(beard)


# accessory list
ak = td.acc_dict.keys()
accessory = list(ak)
#print(accessory)


# faccessory list
fak = td.facc_dict.keys()
faccessory = list(fak)
#print(faccessory)


# head list
hk = td.head_dict.keys()
head = list(hk)
#print(head)


# fhead list
fhk = td.fhead_dict.keys()
fhead = list(fhk)
#print(fhead)


# psych-eyes list
pek = td.psych_dict.keys()
psychadeliceyes = list(pek)
#print(psychadeliceyes)


# psych-type list
ptk = td.psych_dict.keys()
psychadelicptype = list(ptk)
#print(psychadelicptype)


# psych-head list
phk = td.psych_dict.keys()
psychadelichead = list(phk)
#print(psychadelichead)


# psych-accessory list
pak = td.psych_dict.keys()
psychadelicacc = list(pak)
#print(psychadelicacc)

#psych-mouth list
pmk = td.psych_dict.keys()
psychadelicmouth = list(pmk)
#print(psychadelicmouth)



with open((dirname + '/data/punks.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(  ['image:'] + ['Description:'] + ['Name'] + ['Background'] + ['Punk type'] + ['Mouth'] + ['Accessory'] + ['Eyes'] + ['Head'] + ['Beard'] + ['Psych DNA'])


    for x in range(0, 100):
        print('PsychPunk' + str(x))

        # determine background
        def bgchoice(background):
            bg = random.choices(background, weights = (100, 100, 115, 100, 75, 115, 75), k=1)[0]
            return bg
        p_bg = bgchoice(background)
        punk_bg = td.bg_dict.get(p_bg)

        print('Background:', p_bg)


        # determine type
        def ptypechoice(ptype):
            pt = random.choices(ptype, weights = (2, 5, 400, 600, 6), k=1)[0]
            return pt
        p_type = ptypechoice(ptype)
        punk_type = td.type_dict.get(p_type)

        print('Type:', p_type)


        # determine mouth
        def mouthchoice(p_type, fmouth, mouth):
            if p_type == ['Female'][0]:
                m = random.choices(fmouth, weights = (100, 200), k=1)[0]
                return m
            else:
                m = random.choices(mouth, weights = (100, 300, 200), k=1)[0]
                return m 

        p_mouth = mouthchoice(p_type, fmouth, mouth)

        if p_type == ['Female'][0]:
            punk_mouth = td.fmouth_dict.get(p_mouth)
        else:
            punk_mouth = td.mouth_dict.get(p_mouth)

        print('Mouth:', p_mouth)


        # determine accessory
        def accessorychoice(p_type, faccessory, accessory):
            if p_type == ['Female'][0]:
                acc = random.choices(faccessory, weights = (20, 22, 5, 30, 10, 10, 15, 75), k=1)[0]
                return acc
            else:
                acc = random.choices(accessory, weights = (20, 22, 5, 30, 10, 10, 15, 75), k=1)[0]
                return acc
        p_acc = accessorychoice(p_type, faccessory, accessory)

        if p_type == ['Female'][0]:
            punk_acc = td.facc_dict.get(p_acc)
        else:
            punk_acc = td.acc_dict.get(p_acc)

        print('Accessory:', p_acc)



                # determine head choice
        def headchoice(p_type, fhead, head):
            if p_type == ['Female'][0]:
                head = random.choices(fhead, weights = (50, 5, 30, 30, 30, 20, 30, 50, 30, 30, 40, 40, 40, 5, 30, 40, 10, 20, 20, 10, 20), k=1)[0]
                return head
            else:
                head = random.choices(head, weights = (50, 5, 30, 30, 30, 20, 30, 50, 30, 30, 40, 40, 40, 5, 30, 40, 10, 20), k=1)[0]
                return head

        p_head = headchoice(p_type, fhead, head)

        if p_type == ['Female'][0]:
            punk_head = td.fhead_dict.get(p_head)
        else:
            punk_head = td.head_dict.get(p_head)

        print('Head:', p_head)




        # determine eyes
        def eyeschoice(p_type, p_head, feyes, eyes):

            if p_type == ['Female'][0] and p_head != ['Pink pilot hat'][0] and p_head != ['Pilot hat'][0] and p_head != ['Welding goggles'][0]:
                eyes = random.choices(feyes, weights = (30, 50, 30, 40, 50, 40, 60, 40, 50, 40, 30, 150), k=1)[0]
                return eyes
            elif p_type == ['Male'][0] and p_head != ['Pink pilot hat'][0] and p_head != ['Pilot hat'][0] and p_head != ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (30, 50, 30, 40, 50, 40, 60, 40, 50, 40, 150), k=1)[0]
                return eyes
            elif p_type == ['Ape'][0] and p_head != ['Pink pilot hat'][0] and p_head != ['Pilot hat'][0] and p_head != ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (30, 50, 30, 40, 50, 40, 60, 40, 50, 40, 150), k=1)[0]
                return eyes
            elif p_type == ['Zombie'][0] and p_head != ['Pink pilot hat'][0] and p_head != ['Pilot hat'][0] and p_head != ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (30, 50, 30, 40, 50, 40, 60, 40, 50, 40, 150), k=1)[0]
                return eyes
            elif p_type == ['Alien'][0] and p_head != ['Pink pilot hat'][0] and p_head != ['Pilot hat'][0] and p_head != ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (30, 50, 30, 40, 50, 40, 60, 40, 50, 40, 150), k=1)[0]
                return eyes
            elif p_type == ['Female'][0] and p_head == ['Pink pilot hat'][0] or ['Pilot hat'][0] or ['Welding goggles'][0]:
                eyes = random.choices(feyes, weights = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100), k=1)[0]
                return eyes
            elif p_type == ['Male'][0] and p_head == ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100), k=1)[0]
                return eyes
            elif p_type == ['Ape'][0] and p_head == ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100), k=1)[0]
                return eyes
            elif p_type == ['Zombie'][0] and p_head == ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100), k=1)[0]
                return eyes
            elif p_type == ['Alien'][0] and p_head == ['Welding goggles'][0]:
                eyes = random.choices(eyes, weights = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100), k=1)[0]
                return eyes
            else:
                return 'error'
                
        p_eyes = eyeschoice(p_type, p_head, feyes, eyes)

        if p_type == ['Female'][0]:
            punk_eyes = td.feyes_dict.get(p_eyes)
        else:
            punk_eyes = td.eyes_dict.get(p_eyes)

        print('Eyes:', p_eyes)



        # determine beard
        def beardchoice(p_type, beard):
            if p_type == ['Male'][0] or p_type == ['Zombie'][0]:
                b = random.choices(beard, weights = (50, 40 ,30 ,2 ,3 ,3 ,200), k=1)[0]
                return b
            else:
                b = random.choices(beard, weights = (0, 0 ,0 ,0 ,0 ,0 ,100), k=1)[0]
                return b

        p_beard = beardchoice(p_type ,beard)
        punk_beard = td.beard_dict.get(p_beard)


        print('Beard:', p_beard)


        # determine psych-eyes
        def psycheyes(psychadeliceyes):
            pe = random.choices(psychadeliceyes, weights = (10, ) *51, k=1)[0]
            return pe
        pp_eyes = psycheyes(psychadeliceyes)
        psych_eyes = td.psych_dict.get(pp_eyes)



        # determine psych-type
        def psychtype(psychadelicptype):
            pt = random.choices(psychadelicptype, weights = (10, ) *51, k=1)[0]
            return pt
        pp_type =psychtype(psychadelicptype)
        psych_type = td.psych_dict.get(pp_type)



        # determine psych-head
        def psychhead(psychadelichead):
            ph = random.choices(psychadelichead, weights = (10, ) *51, k=1)[0]
            return ph
        pp_head = psychhead(psychadelichead)
        psych_head = td.psych_dict.get(pp_head)



        # determine psych-accessory
        def psychacc(psychadelicacc):
            pa = random.choices(psychadelicacc, weights = (10, ) *51, k=1)[0]
            return pa
        pp_acc = psychhead(psychadelicacc)
        psych_acc = td.psych_dict.get(pp_acc)



        # # determine psych-mouth
        # def psychmouth(psychadelicmouth):
        #     pm = random.choices(psychadelicmouth, weights = (10, ) *51, k=1)[0]
        #     return pm
        # pp_mouth = psychmouth(psychadelicmouth)
        # psych_mouth = td.psych_dict.get(pp_mouth)


        Psych_DNA_list = [(pp_eyes), (pp_type), (pp_head), (pp_acc)]
        Psych_DNA = " ".join(Psych_DNA_list)

        Destination = ()
        
        print('Psych DNA:', Psych_DNA)
        print()



        
# creating CSV file
        x += 1
        name = 'PsychPunk_' + str(x)
        metadataIMG = '/PsychPunk_' + str(x)
        image = ''
        description = ''
        row = x
        writer.writerow([description, image, name, p_bg, p_type, p_mouth, p_acc, p_eyes, p_head, p_beard, Psych_DNA])



        bgimg = punk_bg
        with Image.open(bgimg) as bgimg:
            bga = np.asarray(bgimg)



        typeimg = punk_type
        with Image.open(typeimg) as typeimg:
            ta = np.asarray(typeimg)

        mouthimg = punk_mouth
        with Image.open(mouthimg) as mouthimg:
            ma = np.asarray(mouthimg)


        eyesimg = punk_eyes
        with Image.open(eyesimg) as eyesimg:
            ea = np.asarray(eyesimg)

        beardimg = punk_beard
        with Image.open(beardimg) as beardimg:
            ba = np.asarray(beardimg)

        accessoryimg = punk_acc
        with Image.open(accessoryimg) as accessoryimg:
            aa = np.asarray(accessoryimg)


        headimg = punk_head
        with Image.open(headimg) as headimg:
            ha = np.asarray(headimg)

        psycheimg = psych_eyes
        with Image.open(psycheimg) as psycheimg:
            pea = np.asarray(psycheimg)


        psychpimg = psych_type
        with Image.open(psychpimg) as psychpimg:
            ppa = np.asarray(psychpimg)


        psychhimg = psych_head
        with Image.open(psychhimg) as psychhimg:
            pha = np.asarray(psychhimg)


        psychaimg = psych_acc
        with Image.open(psychaimg) as psychaimg:
                paa = np.asarray(psychaimg)


        # psychmimg = psych_mouth
        # with Image.open(psychmimg) as psychmimg:
        #         pma = np.asarray(psychmimg)


        def comb1():
            background = Image.fromarray(bga)
            typeoverlay = Image.fromarray(ta)
            typeoverlay = typeoverlay.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - typeoverlay.width) // 2
            height = (background.height - typeoverlay.height) // 2
            background.paste(typeoverlay, (width, height), typeoverlay)
            background.save(dirname + '/config/temp/bg_type.png', format="png")


        def removewhitetype():
            img = Image.open(dirname + '/config/temp/bg_type.png')
            img = img.convert("RGBA")
            datas = img.getdata()
            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            img.save(dirname + "/config/temp/whiteremove.png", "PNG")   


        def psychtypeimg():
            os.remove(dirname + "/config/temp/bg_type.png")
            filename1 = Image.fromarray(ppa)
            width, height = filename1.size
            imagee_size = width, height
            portion_size = (337,337)
            x1 = random.randint(0, imagee_size[0]-portion_size[0]-1)
            y1 = random.randint(0, imagee_size[1]-portion_size[1]-1)
            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
            coords = (x1,y1,x2,y2)        
            newimgf = filename1.crop(coords)
            newimgf.save(dirname + '/config/temp/resizepsycht.png')
            filename = (dirname + '/config/temp/whiteremove.png')
            frontImage = Image.open(filename)
            background = Image.open(dirname + '/config/temp/resizepsycht.png')
            whitefile = (dirname + '/config/images/white.png')
            white = Image.open(whitefile)
            frontImage = frontImage.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - frontImage.width) // 2
            height = (background.height - frontImage.height) // 2
            white.paste(background, (width, height), background)
            white.save(dirname + '/config/temp/whiteadded.png')


        def white():
            filename = (dirname + '/config/temp/whiteadded.png')
            filename2 = (dirname + '/config/temp/whiteremove.png')
            add = Image.open(filename)
            remove = Image.open(filename2)
            add = add.convert("RGBA")
            remove = remove.convert("RGBA")
            width = (add.width - remove.width) // 2
            height = (add.height - remove.height) // 2
            add.paste(remove, (width, height), remove)
            add.save(dirname + "/config/temp/base.png", format="png")  


        def comb2():
            eyeoverlay = Image.fromarray(aa)
            background = Image.open(dirname + '/config/temp/base.png')
            eyeoverlay = eyeoverlay.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - eyeoverlay.width) // 2
            height = (background.height - eyeoverlay.height) // 2
            background.paste(eyeoverlay, (width, height), eyeoverlay)
            background.save(dirname + '/config/temp/accadded.png', format="png")


        def removewhiteeye():
            img = Image.open(dirname + '/config/temp/accadded.png')
            img = img.convert("RGBA")
            datas = img.getdata()
            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            img.save(dirname + "/config/temp/whiteremove.png", "PNG")


        def accpsych():
            filename1 = Image.fromarray(paa)
            width, height = filename1.size
            imagee_size = width, height
            portion_size = (337,337)
            x1 = random.randint(0, imagee_size[0]-portion_size[0]-1)
            y1 = random.randint(0, imagee_size[1]-portion_size[1]-1)
            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
            coords = (x1,y1,x2,y2)        
            newimgf = filename1.crop(coords)
            newimgf.save(dirname + '/config/temp/resizepsycht.png')
            filename = (dirname + '/config/temp/resizepsycht.png')
            background = Image.open(filename)
            whitefile = (dirname + '/config/images/white.png')
            white = Image.open(whitefile)
            white = white.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - white.width) // 2
            height = (background.height - white.height) // 2
            white.paste(background, (width, height), background)
            white.save(dirname + '/config/temp/whiteadded.png')


        def white2():            
            filename = (dirname + '/config/temp/whiteadded.png')
            filename2 = (dirname + '/config/temp/whiteremove.png')
            add = Image.open(filename)
            remove = Image.open(filename2)
            add = add.convert("RGBA")
            remove = remove.convert("RGBA")
            width = (add.width - remove.width) // 2
            height = (add.height - remove.height) // 2
            add.paste(remove, (width, height), remove)
            add.save(dirname+'/fin/PsychPunk_'+str(x)+'.png', 'PNG')


        def delstuff():
            os.remove(dirname + '/config/temp/whiteadded.png')
            os.remove(dirname + '/config/temp/whiteremove.png')
            os.remove(dirname + '/config/temp/resizepsycht.png')


        def delstuff2():
            os.remove(dirname + '/config/temp/whiteadded.png')
            os.remove(dirname + '/config/temp/whiteremove.png')
            os.remove(dirname + '/config/temp/accadded.png')


        def delstuff3():            
            os.remove(dirname + '/config/temp/resizepsycht.png')
            os.remove(dirname + '/config/temp/whiteadded.png')
            os.remove(dirname + '/config/temp/whiteremove.png')
            os.remove(dirname + '/config/temp/accadded.png')
            os.remove(dirname + '/config/temp/base.png')


        def comb3():
            eyeoverlay = Image.fromarray(ha)
            background = Image.open(dirname + '/config/temp/base.png')
            eyeoverlay = eyeoverlay.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - eyeoverlay.width) // 2
            height = (background.height - eyeoverlay.height) // 2
            background.paste(eyeoverlay, (width, height), eyeoverlay)
            background.save(dirname + '/config/temp/accadded.png', format="png")


        def removewhitehead():
            img = Image.open(dirname + '/config/temp/accadded.png')
            img = img.convert("RGBA")
            datas = img.getdata()
            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            img.save(dirname + "/config/temp/whiteremove.png", "PNG")


        def headpsych():
            filename1 = Image.fromarray(pha)
            width, height = filename1.size
            imagee_size = width, height
            portion_size = (337,337)
            x1 = random.randint(0, imagee_size[0]-portion_size[0]-1)
            y1 = random.randint(0, imagee_size[1]-portion_size[1]-1)
            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
            coords = (x1,y1,x2,y2)        
            newimgf = filename1.crop(coords)
            newimgf.save(dirname + '/config/temp/resizepsycht.png')
            filename = (dirname + '/config/temp/resizepsycht.png')
            background = Image.open(filename)
            whitefile = (dirname + '/config/images/white.png')
            white = Image.open(whitefile)
            white = white.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - white.width) // 2
            height = (background.height - white.height) // 2
            white.paste(background, (width, height), background)
            white.save(dirname + '/config/temp/whiteadded.png')  


        def eyepsych():
            filename1 = Image.fromarray(pea)
            width, height = filename1.size
            imagee_size = width, height
            portion_size = (337,337)
            x1 = random.randint(1, imagee_size[0]-portion_size[0]-1)
            y1 = random.randint(1, imagee_size[1]-portion_size[1]-1)
            x2,y2 = x1+portion_size[0]-1, y1+portion_size[1]-1
            coords = (x1,y1,x2,y2)        
            newimgf = filename1.crop(coords)
            newimgf.save(dirname + '/config/temp/resizepsycht.png')
            filename = (dirname + '/config/temp/resizepsycht.png')
            background = Image.open(filename)
            whitefile = (dirname + '/config/images/white.png')
            white = Image.open(whitefile)
            white = white.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - white.width) // 2
            height = (background.height - white.height) // 2
            white.paste(background, (width, height), background)
            white.save(dirname + '/config/temp/whiteadded.png')


        def comb4():
            eyeoverlay = Image.fromarray(ea)
            background = Image.open(dirname + '/config/temp/base.png')
            eyeoverlay = eyeoverlay.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - eyeoverlay.width) // 2
            height = (background.height - eyeoverlay.height) // 2
            background.paste(eyeoverlay, (width, height), eyeoverlay)
            background.save(dirname + '/config/temp/accadded.png', format="png")


        def comb5():
            eyeoverlay = Image.fromarray(ba)
            background = Image.open(dirname + '/config/temp/base.png')
            eyeoverlay = eyeoverlay.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - eyeoverlay.width) // 2
            height = (background.height - eyeoverlay.height) // 2
            background.paste(eyeoverlay, (width, height), eyeoverlay)
            background.save(dirname + '/config/temp/accadded.png', format="png")


        def beardpsych():
            white = Image.open(dirname + '/config/temp/accadded.png')
            white.save(dirname + '/config/temp/whiteadded.png')


        def mouthhimg():
            eyeoverlay = Image.fromarray(ma)
            background = Image.open(dirname + '/config/temp/base.png')
            eyeoverlay = eyeoverlay.convert("RGBA")
            background = background.convert("RGBA")
            width = (background.width - eyeoverlay.width) // 2
            height = (background.height - eyeoverlay.height) // 2
            background.paste(eyeoverlay, (width, height), eyeoverlay)
            background.save(dirname + '/config/temp/base.png', format="png")


        def delstuff1():
            os.remove(dirname + '/config/temp/resizepsycht.png')
            os.remove(dirname + '/config/temp/whiteadded.png')
            os.remove(dirname + '/config/temp/whiteremove.png')
            os.remove(dirname + '/config/temp/accadded.png')





        #bg and type creation
        comb1()
        removewhitetype()
        psychtypeimg()
        white()
        delstuff()
        #beard
        comb5()
        removewhiteeye()
        beardpsych()
        white()
        delstuff2()
        #mouth
        mouthhimg()
        #Head
        comb3()
        removewhitehead()
        headpsych()
        white()
        delstuff1()
        #accessory
        comb2()
        removewhiteeye()
        accpsych()
        white()
        delstuff1()
        #eyes
        comb4()
        removewhiteeye()
        eyepsych()
        white2()
