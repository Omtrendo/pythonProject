#Перевірка міфу про порядок літер
import random
radok = 'Чи знаєте як липа шелестить, у місячні весняні ночі?'
wrd = radok.split()
radok_n = ''
zpr = ",.!;:'"
for sl in wrd:
    wrd_n = sl
    slb = list(sl)
    if len(slb)>3 and not sl.isdigit():
        fb = slb[0]
        if slb[-1] not in zpr:
            lb = slb[-1]
            mix = slb[1:-1]
        else:
            lb = sl[-1]+sl[-2]
            mix = slb[1: -2]
        random.shuffle(mix)
        srd = ''
        for lit in mix:
            srd = srd + lit
        wrd_n = fb+srd+lb
    radok_n = radok_n + wrd_n + ' '
print(radok)
print(radok_n)
print('-'*40)