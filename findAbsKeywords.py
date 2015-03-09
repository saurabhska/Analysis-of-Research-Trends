import json
import sys
import os
import pickle

AbsIDNounDict=dict()
NounKeywordDict=dict()

def readDict(AbsIDNounFile):
  global AbsIDNounDict
  modelread=open(AbsIDNounFile,'rb')
  AbsIDNounDict=pickle.load(modelread)
  modelread.close()
  outfile=open('absIDNounMapping.out','w')
  for key,value in AbsIDNounDict.items():
    outfile.write(key)
    outfile.write("\t")
    outfile.write(str(value))
    outfile.write("\n")
  outfile.close()

def getAbsKeywords(absNounList):
  global NounKeywordDict
  keywords=list()
  for noun in absNounList:
    if noun in NounKeywordDict.keys():
      temp=NounKeywordDict[noun]
      for word in temp:
        if word not in keywords:
          keywords.append(word)
  return keywords

def mapAbsWithKeywords(outputFile):
  global AbsIDNounDict
  global NounKeywordDict
  count=1
  outfile=open(outputFile,'w')
  for absId,absNounList in AbsIDNounDict.items():
     absKeywordList=getAbsKeywords(absNounList)
     #list(set(absKeywordList))
     if absKeywordList != []:
       outfile.write(absId)
       outfile.write("\t")
       outfile.write(str(absKeywordList).replace("[","").replace("]",""))
       outfile.write("\n")
  

def storeMapping(noun,keyword):
  global NounKeywordDict
  if noun not in NounKeywordDict:
    temp=list()
    temp.append(keyword)
    NounKeywordDict[noun]=temp
  else:
    temp=NounKeywordDict[noun]
    temp.append(keyword)
    NounKeywordDict[noun]=temp

def readMapping(mappingFile):
  infile=open(mappingFile,'r')
  lines=infile.readlines()
  for line in lines:
    line=line.replace("\n","")
    words=line.split("|")
    storeMapping(words[0],words[1])  

def main():
  #Check for proper arguments
  if len(sys.argv) != 4:
    print ('usage: python3 findAbsKeywords.py AbsIDNoun-dictionary-file mapping-file outputFile')
    sys.exit(1)
  #Scan inputs
  AbsIDNounFile = sys.argv[1]
  mappingFile = sys.argv[2]
  outputFile=sys.argv[3]
  #Get a list of keywords from input file
  readDict(AbsIDNounFile)
  readMapping(mappingFile)
  mapAbsWithKeywords(outputFile)


if __name__ == '__main__':
  main()
