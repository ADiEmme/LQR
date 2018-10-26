#!/bin/python
import sys
import random
import ast

def main():
  print ('''######## Letters quest remastered help tool ########\n# Criteria:\n# - The longer the word is, the more points you will get.\n# - Double letters give more points.\n####################################################''')
  letters=sys.argv[1]
  anagram(letters)

def anagram(letters):
  shuf_array=[]
  shuffled=''.join(random.sample(letters, len(letters)))
  dict_res=[]
  while shuffled not in shuf_array:
    #shuffled = ''.join(random.sample(letters, random.randrange(3,len(letters))))
    shuf_array.append(shuffled)
    with open('/home/adiemme/LQR/words') as f:
        for line in f:
          line = line.strip()
          if line in shuf_array[-1]:
            #print line+" = "+shuf_array[-1]
            dict_res.append(line)
    shuffled = ''.join(random.sample(letters, len(letters)))
    print shuf_array
    while shuffled in shuf_array:
        shuffled = ''.join(random.sample(letters, len(letters)))
        print shuffled
    #shuf_array.append(shuffled)
 
  dict_res.sort(key=len, reverse=True)
  print dict_res
main ()

