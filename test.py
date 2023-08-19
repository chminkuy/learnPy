import os
import sys
#print(os.getcwd())

sys.stdin = open('input.txt')

#li=list(map(int,input().split()))
#print(*li)

def prob1():
   li = []
   while 1:
       l = input().strip()
       if(l=='-1'): break
       li.append(int(l))
       pass

   print(*li)
   pass

prob1()


