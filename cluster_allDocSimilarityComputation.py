import sys
import os
import json

docWordDict=dict()
docLinksDict=dict()
URIList=list()

def createDocWordDict(uriKeywordMapFile):
  global docWordDict
  infile=open(uriKeywordMapFile,'r')
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
  #print(docWordDict)
  
def computeURIList(outPaperFile):
  global URIList
  infile=open(outPaperFile,'r')
  lines=infile.readlines()
  for line in lines:
    line=line.replace("\n","")
    words=line.split('\t')
    docURI=words[0]
    URIList.append(docURI)
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

def computeDocLinks(docGraphFile,outputFile):
  global docWordDict
  global docLinksDict
  global URIList
  infile=open(docGraphFile,'r')
  lines=infile.readlines()
  outFile=open(outputFile,'w')
  docWordDictKeys=docWordDict.keys()
  for line in lines:
    flag1=0
    flag2=0
    line=line.replace("\n","")
    words=line.split('\t')
    docID1=int(words[0])
    docID2=int(words[1])
    #print("*******************************************")
    #print("docID1" + docID1)
    doc1=URIList[docID1]
    doc2=URIList[docID2]
    if doc1 in docWordDictKeys:
      wordList1Set=set(docWordDict[doc1])
      flag1=1
    else:
      print('doc1...'+words[0])
    if doc2 in docWordDictKeys:
      wordList2Set=set(docWordDict[doc2])
      flag2=1
    else:
      print('doc2...'+words[1])
    if (flag1==1 and flag2==1):
      commons=len(list(wordList1Set.intersection(wordList2Set)))
      if (commons != 0):
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
  
  if len(sys.argv)!=5:
    print('usage: python3 allDocSimilarityComputation.py URI_KeywordMap docGraphFile outPaperFile outputFile')
    exit(1)
  
  uriKeywordMapFile=sys.argv[1]
  docGraphFile=sys.argv[2]
  outPaperFile=sys.argv[3]
  outputFile=sys.argv[4]
  print('creating createDocWordDict...')
  createDocWordDict(uriKeywordMapFile)
  print('created createDocWordDict...')
  #print(wordDocDict)
  print('creating URI list...')
  computeURIList(outPaperFile)
  print('computing Links...')
  computeDocLinks(docGraphFile,outputFile)

if __name__=='__main__':
  main()
