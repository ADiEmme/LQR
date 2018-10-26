#!/bin/python
import sys
import random
import ast
import itertools
import pprint

def main():
  print ('''######## Letters quest remastered help tool ########\n# Criteria:\n# - The longer the word is, the more points you will get.\n# - Double letters give more points.\n####################################################''')
  letters=sys.argv[1]
  anagram(letters)

def anagram(letters):
  shuf_array=list(map("".join, itertools.permutations(letters)))
  dict_res=[]
  for shuf in shuf_array:
    with open('words') as f:
      for line in f:
        line = line.strip().lower()
        if line == shuf:
          dict_res.append(line)
  
  dict_res=list(set(dict_res))
  print dict_res

main ()

