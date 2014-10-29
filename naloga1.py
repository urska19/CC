import math
import fractions
import sys

def NN_N(xp, yp):
    stevec=1
    x=1
    y=1
    while(x!=xp or y!=yp):
        if (y==1):
            y=x+1
            x=1
        else:
            y=y-1
            x=x+1
        stevec=stevec+1
    return stevec

def N_NN(n):
    stevec=1
    y=1
    x=1
    while(stevec!=n):
        if(y==1):
            y=x+1
            x=1
        else: 
            y=y-1
            x=x+1
        stevec=stevec+1
    return (x,y)

def Q_N(xp, yp):
    stevec=1
    x=1
    y=1
    gcd=fractions.gcd(xp,yp)
    if (gcd!=1):
        xp=xp/gcd
        yp=yp/gcd
    while(x!=xp or y!=yp):
        if (y==1):
            y=x+1
            x=1
        else:
            y=y-1
            x=x+1
        if (fractions.gcd(x,y)==1):
            stevec=stevec+1
    return stevec

def N_Q(n):
    stevec=1
    x=1
    y=1
    while(stevec!=n):
        if(y==1):
            y=x+1
            x=1
        else: 
            y=y-1
            x=x+1
        if (fractions.gcd(x, y)==1):
            stevec=stevec+1
    return (x, y)


if len(sys.argv)==3:
    if sys.argv[1]=="N-Q+":
        print N_Q(int(sys.argv[2]))
    elif sys.argv[1]=="N-(N,N)":
        print N_NN(int(sys.argv[2]))
elif len(sys.argv)==4:
    if sys.argv[1]=="Q+-N":
        print Q_N(int(sys.argv[2]),int(sys.argv[3]))
    elif sys.argv[1]=="(N,N)-N":
        print NN_N(int(sys.argv[2]),int(sys.argv[3]))

