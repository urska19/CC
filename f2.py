import sys
#fja f izracuna kateremu naravnemu st. pripada BF programu
#naravno st. podamo kot argument 
#f deluje samo na programih do dolzine 3 in brez oklepajev

def bf(n):
    calc=[0]*300000
    calc[0]=1
    calc[1]=6
    calc[2]=36
    if calc[n] !=0:
        return calc[n]
    
    else:
        sum=bf(n-2)+6*bf(n-1)
        for i in range(1,n-2):
            sum=sum+bf(i)*bf(n-2-i)
        calc[n]=sum
        return sum
    
    
def f(n):
    s=0
    l=[]
    for i in range(1,n):
        s=s+bf(i)
        if s>=n:
            k=i
            break
    for i in range(k-1,-1,-1):
        m=n%bf(i)
        c=n/bf(i)
        l.append(c)
        n=m    
        

    for i in range(0,len(l)):
        if l[i]==1:
            l[i]='>'
        if l[i]==2:
            l[i]='<'
        if l[i]==3:
            l[i]='+'
        if l[i]==4:
            l[i]='-'
        if l[i]==5:
            l[i]='.'
        if l[i]==6:
            l[i]=','
    return "".join(l)    


print f(int(sys.argv[1]))
