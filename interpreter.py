import sys
#BF program podamo kot argument v txt datoteki

class Trak(object):
    def __init__(self):
        self.trak=[0]
        self.pos=0
    def get(self):
        return self.trak[self.pos]
    def set(self,v):
        self.trak[self.pos]=v
    def povecaj(self):
        self.trak[self.pos]=self.trak[self.pos]+1
    def zmanjsaj(self):
        self.trak[self.pos]=self.trak[self.pos]-1
    def desno(self):
        self.pos=self.pos+1
        if len(self.trak)<=self.pos:
            self.trak.append(0)
    def levo(self):
        self.pos=self.pos-1

def bf(program):
    kazalec=0
    trak=Trak()
    while(kazalec<len(program)):
        znak=program[kazalec]
        if(znak==">"):
            trak.desno()
        elif(znak=="<"):
            trak.levo()
        elif(znak=="+"):
            trak.povecaj()
        elif(znak=="-"):
            trak.zmanjsaj()
        elif(znak=="."):
            sys.stdout.write(chr(trak.get()))
        elif(znak==","):
            trak.set(ord(sys.stdin.read()))
        elif(znak=="[" and trak.get()==0):
	    tmp=1
	    while tmp>0:
		kazalec+=1
		c=program[kazalec]
		if c=="[":
		    tmp+=1
		elif c=="]":
		    tmp-=1
        elif(znak == "]"):
            tmp=1
            while tmp>0:
                kazalec=kazalec-1
                c=program[kazalec]
                if c=='[':
                    tmp=tmp-1
                elif c == ']':
                    tmp=tmp+1
            kazalec=kazalec-1
        kazalec=kazalec+1
    
program=(open(sys.argv[1], 'r')).read()
bf(program)
