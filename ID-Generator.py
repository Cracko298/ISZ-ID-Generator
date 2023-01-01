import random
import string
from time import sleep
from os import remove
from os import path
from os import system

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

def Load():
  sleep(0.15)
  print("Created By:  r       ")
  sleep(0.15)
  system(clear)
  print("Created By:  r c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c    8")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o298")
  sleep(0.15)
  system(clear)
  print("Created By: Cracko298")
  sleep(1.5)
  system(clear)
Load()


ch0 = path.exists('_meta.data4')
ch1 = path.exists('Output_GeneratedIDs.txt')

if ch1 == True:
    remove('Output_GeneratedIDs.txt')

if ch0 == True:
    remove('_meta.data4')

tick0 = int(input("How Many ID's Would You Like To Generate: "))
tick1 = 0

while True:
    if tick1 != tick0:
        def ID_Generator(chars = string.ascii_uppercase + string.digits, N=10):
            return ''.join(random.choice(chars) for _ in range(N))
        number1 = ID_Generator(N=16,chars='ABCDEF1234567890')
        number0 = print(f'Generated {tick1}/{tick0}:', ID_Generator(N=16,chars='ABCDEF1234567890'))
        file0 = open('_meta.data4', 'a')
        file0.write(f'{number1}\n')
        tick1+=1
    else:
        file0.close()
        break

OutputFile = open('Output_GeneratedIDs.txt','a')
inputFile = open('_meta.data4','r')
lines = set()

while 1==1:
    if tick1 == tick0:
        for line in inputFile:
            if line not in lines:
                OutputFile.write(f'{line}')
                lines.add(line)
        inputFile.close()
        OutputFile.close()
        remove('_meta.data4')
        tick1 = 0
    else:
        break


