import random
import config.traits_dict as td


ptk = td.type_dict.keys()
ptype = list(ptk)


p_type = ['Female'][0]

hk = td.head_dict.keys()
head = list(hk)

fhk = td.fhead_dict.keys()
fhead = list(fhk)

eks = td.eyes_dict.keys()
eyes = list(eks)

feks = td.feyes_dict.keys()
feyes = list(feks)



def headchoice(p_type, fhead, head):
    if p_type == ['Female'][0]:
        head = random.choices(fhead, weights = (50, 5, 30, 30, 30, 20, 30, 50, 30, 30, 40, 40, 40, 5, 30, 40, 10, 20, 20, 10, 10), k=1)[0]
        return head
    else:
        head = random.choices(head, weights = (50, 5, 30, 30, 30, 20, 30, 50, 30, 30, 40, 40, 40, 5, 30, 40, 10, 10), k=1)[0]
        return head

p_head = headchoice(p_type, fhead, head)

if p_type == ['Female'][0]:
    punk_head = td.fhead_dict.get(p_head)
else:
    punk_head = td.head_dict.get(p_head)


print('Head:', p_head)



def eyeschoice(p_type, p_head, feyes, eyes):

	if p_type == ['Female'][0] and p_head != ['Pink pilot hat'][0]:
		eyes = random.choices(feyes, weights = (30, 50, 30, 40, 50, 40, 60, 40, 50, 40, 30, 150), k=1)[0]
		return eyes
	else:
		return 'error'


p_eyes = eyeschoice(p_type, p_head, feyes, eyes)

if p_type == ['Female'][0]:
            punk_eyes = td.feyes_dict.get(p_eyes)
else:
            punk_eyes = td.eyes_dict.get(p_eyes)

print('Eyes:', p_eyes)
print(punk_eyes)
