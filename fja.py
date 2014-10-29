import sys
#fja f izracuna katero naravno st. pripada BF programu
#program podamo kot argument v txt datoteki

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
   


def f(program,k):
    s=0
    if len(program)==1 and program=='>':
        s=1
    if len(program)==1 and program=='<':
        s=2
    if len(program)==1 and program=='+':
        s=3
    if len(program)==1 and program=='-':
        s=4
    if len(program)==1 and program=='.':
        s=5
    if len(program)==1 and program==',':
        s=6
        
    if k==0:
        for i in range(1,len(program)):
            s=s+bf(i)
        k=1    

    if len(program)>=2:
        if program[0]=='>':
            program=program[1:]
            s=s+f(program,1)
        elif program[0]=='<':
            program=program[1:]
            s=s+1*bf(len(program))
            s=s+f(program,1)
        elif program[0]=='+':
            program=program[1:]
            s=s+2*bf(len(program))
            s=s+f(program,1)
        elif program[0]=='-':
            program=program[1:]
            s=s+3*bf(len(program))
            s=s+f(program,1)
        elif program[0]=='.':
            program=program[1:]
            s=s+4*bf(len(program))
            s=s+f(program,1)
        elif program[0]==',':
            program=program[1:]
            s=s+5*bf(len(program))
            s=s+f(program,1)
        elif program[0]=='[':
            id=program.find(']')
            program=program[1:id]+program[id+1:] 
            l=len(program) 
            if id>=3:         
                for i in range(1,l+1):
                    s=s+bf(i)*bf(l-i)
                    if i==id-2:
                        break
            s=s+6*bf(len(program)+1)
            s=s+f(program,1)
    return s
    


program=(open(sys.argv[1], 'r')).read()
l=len(program)
program=program[0:l-1]

print f(program,0)
