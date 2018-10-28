#!/bin/python
import sys
import random
import ast
import itertools
import multiprocessing as mp


output = mp.Queue()


def main():
  print ('''######## Letters quest remastered help tool ########\n# Criteria:\n# - The longer the word is, the more points you will get.\n# - Double letters give more points.\n####################################################''')
  letters=sys.argv[1]
  anagram(letters)


def anagram(letters):
  shuf_array_big=list(map("".join, itertools.permutations(letters)))
  dict_res=[] 
  nproc=mp.cpu_count()
  for i in range(0,len(shuf_array_big),nproc):  
    jobs = []
    shuf_array=shuf_array_big[i:i+nproc]
    #print shuf_array
    for shuf in shuf_array:
      processes = mp.Process(target=findit, args=(shuf,))
      jobs.append(processes)
  
    # Run processes
    for p in jobs:
      p.start()

    # Exit the completed processes
    for p in jobs:
      p.join()

    # Get process results from the output queue
    results = [output.get() for p in jobs]

    dict_res.append(results)

  dict_res=sorted(set(list(itertools.chain.from_iterable(dict_res))), key=len, reverse=True)
  print dict_res

def findit(shuf):
  with open('words') as f:
    for line in f:
      line = line.strip().lower()
      if line in shuf or shuf in line:
        output.put(line)

main ()

