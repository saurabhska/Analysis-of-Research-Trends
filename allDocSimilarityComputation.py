import sys
import os
import json

docWordDict=dict()
docLinksDict=dict()
def createDocWordDict(inputFile):
  global docWordDict
  infile=open(inputFile,'r')
  lines=infile.readlines()
  for line in lines:
    line=line.replace("\n","")
    words=line.split(',')
    docName=words[0]
    keyword=words[1]
    if docName not in docWordDict.keys():
      tempList=list()
      tempList.append(keyword)
      docWordDict[docName]=tempList
    else:
      docWordDict[docName].append(keyword)
  print("printing docWordDict............")
  #print(wordDocDict)
  

def updateDocLinks(iWord,jWord):
  global docLinksDict
  if iWord not in docLinksDict.keys():
    tempDict=dict()
    tempDict[jWord]=1
    docLinksDict[iWord]=tempDict
  else:
    valueDict=docLinksDict[iWord]
    if jWord not in valueDict:
      valueDict[jWord]=1
    else:
      valueDict[jWord]+=1
    docLinksDict[iWord]=valueDict

def computeDocLinks(outputFile):
  global docLinksDict
  global docWordDict
  outFile=open(outputFile,"w")
  num=len(docWordDict.keys())
  counter=0
  for doc1,wordList1 in docWordDict.items():
    counter+=1
    print("processing document..."+str(counter)+"...of..."+str(num))
    wordList1Set=set(wordList1)
    for doc2,wordList2 in docWordDict.items():
      if doc1 != doc2:
        commons=len(list(wordList1Set.intersection(set(wordList2))))
        if commons != 0:
          outFile.write(doc1+','+doc2+','+str(commons))
          outFile.write('\n')
          #outFile.write('wordList1: '+str(wordList1)+' ,wordList1: '+str(wordList2))
          #outFile.write('\n')
          #outFile.write("--------------------------------------------")
          #outFile.write('\n')
          #outFile.write(doc2+','+doc1+','+str(commons))
          #outFile.write('\n')
    #del docWordDict[doc1]
  outFile.close()

def main():
  global wordDocDict
  global docLinksDict
  
  if len(sys.argv)!=3:
    print('usage: python3 allDocSimilarityComputation.py input output')
    exit(1)
  
  inputFile=sys.argv[1]
  outputFile=sys.argv[2]
  print('creating createDocWordDict...')
  createDocWordDict(inputFile)
  print('created createDocWordDict...')
  #print(wordDocDict)
  print('computing Links...')
  computeDocLinks(outputFile)
  print('computed Links...')

if __name__=='__main__':
  main()
