from datetime import datetime,date
import re

jour = ['','1er']+[str(n) for n in range(2,32)]
mois = ['','janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

def autofind(x,y):
    if int(x[0:2])<=31 and int(x[2:4])<=12 and int(x[4:])>1000:
        if int(x[:4])>1000 and int(x[4:6])<=12 and int(x[6:])<=31:
            return ymd(x,y)
        else:
            return dmy(x,y)
    elif int(x[:4])>1000 and int(x[4:6])<=12 and int(x[6:])<=31:
        return dmy(x,y)

def dmy(x,to_date=False):
    if to_date == True:
        return date(int(x[4:]),int(x[2:4]),int(x[:2]))
    else:
        return jour[int(x[:2])]+' '+mois[int(x[2:4])]+' '+str(x[4:])

def ymd(x,to_date=False):
    if to_date == True:
        return date(int(x[:4]),int(x[4:6]),int(x[6:]))
    else:
        return jour[int(x[6:])]+' '+mois[int(x[4:6])]+' '+str(x[:4])

def conv(input,to_date=False):
    x=input
    if isinstance(x,datetime) or isinstance(x,date):
        if to_date == True:
            return x
        else:
            return ymd(x.strftime('%Y%m%d'))
    elif type(x) == str and re.match('^\d*$',x) and len(x)==8:
        return autofind(x,to_date)
    elif type(x) == str and re.match('^\d+\D\d+\D\d+$',x):
        y = re.split('\D',x)
        z = ''.join(y)        
        if len(y[0])==4 and len(z)==8:
            return ymd(z,to_date)
        elif len(y[2])==4 and len(z)==8:
            return dmy(z,to_date)
        elif len(z)==6:
            return dmy(z[:4]+'20'+z[4:],to_date)
    elif type(x) == str and re.match('^\d+\s[a-zA-Z]+\s\d+$',x):
        y = re.split('\s',x)
        if y[1] in mois:
            m = str(mois.index(y[1]))
            if len(m)==1:
                m='0'+m
            return dmy(y[0]+m+y[2],to_date)

if __name__ == '__main__':
    result=conv(str(input('Saisissez la date à convertir :')))
    print(result)
