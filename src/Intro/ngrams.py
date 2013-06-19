#!/usr/bin/env python3

"""
(C) 2013 by Damir Cavar

Function to generate an N-gram model from a sequence (string, list...).
"""


def makeNgramModel(tokenlist, n):
   """This function generates an N-gram model as a dictionary data-structure.
   """
   fp = {}
   for start in range( len(tokenlist) - (n - 1) ):
      tokenslice = tokenlist[start : start + n]
      #print("Token-slice:", tokenslice)

      stringngram = " ".join(tokenslice)
      #print("String N-gram:", stringngram)
   
      #print(" ".join(tokens[start : start + n]))
      fp[stringngram] = fp.get(stringngram, 0) + 1
   return fp

#print(makeNgramModel("this is a small test", 3))

