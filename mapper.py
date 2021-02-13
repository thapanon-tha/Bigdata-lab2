#!/usr/bin/env python3
import sys


# f = open("hadoop-log4j.log", "r")
# test = open("test.txt", "w")
focus =[]
for line in sys.stdin:
# for line in f:
    # print(line)
    line = line.strip("\n")
    words = line.split(": ")
    for word in words:
      if ( word.find("INFO")!= -1 or word.find("WARN")!= -1 or word.find("ERROR")!= -1 )  and ( word.find("-")!= -1 and word.find(":")!= -1 and word.find(",")!= -1 ) and word.find("}")== -1 and word.find("{")== -1:
        focus.append(word)

for words in focus:
  word = words.split()
  # test.write('%s\t%d\n'%(word[0],1))
  # test.write('%s\t%d\n'%(word[2],1))
  # test.write('%s\t%d\n'%(word[3],1))
  print('%s\t%d'%(word[0],1))
  print('%s\t%d'%(word[2],1))
  print('%s\t%d'%(word[3],1))
  if word[2] == "ERROR":
    #test.write('%s_%s\t%d\n'%(word[3],word[2],1))
    print('%s: %s\t%d'%(word[3],word[2],1))


# test.close()
