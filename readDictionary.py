import json
import sys
import os
import nltk
import pickle

def main():
  #Check for proper arguments

  if len(sys.argv) != 2:
    print ('usage: python3 readDictionary.py input')
    sys.exit(1)
    
  inputFile = sys.argv[1]
  infile=open(inputFile,'rb')
  dictionary=pickle.load(infile)
  infile.close()
  writeKeys=open('keys.out','w')
  writeValues=open('values.out','w')
  for key,value in dictionary.items():
    writeKeys.write(key)
    writeKeys.write("\n")
    writeValues.write(" ".join(value))
    writeValues.write("\n")
  writeValues.close()
  writeKeys.close()
  
if __name__ == '__main__':
  main()
