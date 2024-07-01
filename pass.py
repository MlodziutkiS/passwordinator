import sys
import random
import time
import pyperclip

s=time.time()

def noobie():
        print("Syntax should be:",sys.argv[0]," (use upper case) (use numbers) (use special chars) (choose length)")
        print("Arguments are passed to bool()")

def makelist(ual,num,spec):
        list1 = []
        for x in range(97,123):
                list1+=chr(x)
        upper = []
        for x in range(65,91):
                upper+=chr(x)
        numbers = [1,2,3,4,5,6,7,8,9,0]
        special=[]
        for x in range(33,48):
                special+=chr(x)
        for x in range(58,65):
                special+=chr(x)
        for x in range(123,127):
                special+=chr(x)

        if(bool(ual)==True):
                list1+=upper
        if(bool(num)==True):
                list1+=numbers
        if(bool(spec)==True):
                list1+=special
        return list1

try:
        list1=makelist(sys.argv[1],sys.argv[2],sys.argv[3])
except:
        noobie()
        quit()

try:
        count=sys.argv[4]
except:
        count=32
        print("default value of length is 32")

output=""

for x in range(int(count)):
        output+=str(random.choice(list1))

pyperclip.copy(str(output))

print("time",time.time()-s)
