#!/bin/python
import sys
import random
import ast
import itertools

def main():
  print ('''######## Letters quest remastered help tool ########\n# Criteria:\n# - The longer the word is, the more points you will get.\n# - Double letters give more points.\n####################################################''')
  letters=sys.argv[1]
  anagram(letters)


def anagram(letters):
  shuf_array=list(map("".join, itertools.permutations(letters)))
  dict_res=[]
  #print shuf_array
  for shuf in shuf_array:
    with open('words') as f:
      for line in f:
        line = line.strip().lower()
        if line in shuf or shuf in line:
          dict_res.append(line)
  
  dict_res=sorted(list(set(dict_res)), key=len, reverse=True)

  print dict_res

main ()

