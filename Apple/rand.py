import secrets
import string

sG = secrets.SystemRandom()
pcode_suff = (sG.randint(1,100))

if pcode_suff < 10:
    pcode_suff = '00' + str(pcode_suff) 
elif pcode_suff >= 10 & pcode_suff < 100:
    pcode_suff = '0' + str(pcode_suff) 
else :
    pcode_suff = str(pcode_suff)
pcode = '400' + pcode_suff
print(pcode)
#400 068

date = sG.randint(1,29)
if date < 10 :
    date = '0' + str(date)
else :
    date =str(date)

month = sG.randint(1,12)
if month < 10 :
    month = '0' + str(month)
else :
    month = str(month)

year = str(sG.randint(1950,2002))

dob = date+month+year
print(dob)

