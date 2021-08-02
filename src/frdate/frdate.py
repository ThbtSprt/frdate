from datetime import datetime,date
from euros.fr import nombre2lettres as ltr
import re

jour = ['','1er']+[str(n) for n in range(2,32)]
jour_l = ['','premier']+[ltr(str(n)) for n in range(2,32)]
mois = ['','janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

def autofind(x,y,z):
    if int(x[:4])>1000 and int(x[4:6])<=12 and int(x[6:])<=31:
        if int(x[0:2])<=31 and int(x[2:4])<=12 and int(x[4:])>1000: #En cas d'ambiguïté de la date saisie (ex : 10101212 peut aussi bien être le 10 octobre 1212 ou le 12 décembre 1010, on fait ici le choix de privilégier l'hypothèse du format DDMMYYYY, plus probable en français
            return dmy(x,y,z)
        else:
            return ymd(x,y,z)
    elif int(x[0:2])<=31 and int(x[2:4])<=12 and int(x[4:])>1000:
        return dmy(x,y,z)

def dmy(x,to_date,litteral):
    if to_date == True:
        return date(int(x[4:]),int(x[2:4]),int(x[:2]))
    elif litteral == True:
        return jour_l[int(x[:2])]+' '+mois[int(x[2:4])]+' '+ltr(str(x[4:]))
    else:
        return jour[int(x[:2])]+' '+mois[int(x[2:4])]+' '+str(x[4:])

def ymd(x,to_date,litteral):
    if to_date == True:
        return date(int(x[:4]),int(x[4:6]),int(x[6:]))
    elif litteral == True:
        return jour_l[int(x[6:])]+' '+mois[int(x[4:6])]+' '+ltr(str(x[:4]))
    else:
        return jour[int(x[6:])]+' '+mois[int(x[4:6])]+' '+str(x[:4])

def conv(input,to_date=False,litteral=False):
    x=input
    if isinstance(x,datetime) or isinstance(x,date):
        if to_date == True:
            return x
        else:
            return ymd(x.strftime('%Y%m%d'),False,litteral)
    elif type(x) == str and re.match(r'^\d*$',x) and len(x)==8:
        return autofind(x,to_date,litteral)
    elif type(x) == str and re.match(r'^\d+\D\d+\D\d+$',x):
        y = re.split(r'\D',x)
        z = ''.join(y)
        if len(y[0])==4 and len(z)==8:
            return ymd(z,to_date,litteral)
        elif len(y[2])==4 and len(z)==8:
            return dmy(z,to_date,litteral)
        elif len(z)==6:
            return dmy(z[:4]+'20'+z[4:],to_date,litteral)
    elif type(x) == str and re.match(r'^\S+\s[éûa-zÉÛA-Z]+\s\d+$',x):
        y = re.split(r'\s',x)
        if not re.match(r'^\d+$',y[0]):
            if y[0] == '1er':
                y[0]='01'
            elif y[0] in jour_l:
                y[0]=str(jour_l.index(y[0]))
        if len(y[0])==1:
            y[0]='0'+y[0]

        if y[1] in mois:
            m = str(mois.index(y[1]))
            if len(m)==1:
                m='0'+m
            return dmy(y[0]+m+y[2],to_date,litteral)
        else:
            return x
    elif type(x) == dict:
        for i in x:
            if 'date' in i:
                x[i] = conv(x[i],to_date,litteral)
        return x
    elif type(x) == list:
        for i in range(len(x)):
            x[i] = conv(x[i],to_date,litteral)
        return x
    else:
        return x

if __name__ == '__main__':
    result=conv(str(input('Saisissez la date à convertir :')))
    print(result)
