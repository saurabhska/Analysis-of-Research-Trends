import json
import sys
import os
import nltk
import pickle

absIDURIDict=dict()
def getDocumentURIs(dataFile):
  global absIDURIDict
  json_data=open(dataFile,'r',errors='ignore')
  data=json.load(json_data)
  json_data.close()
  dataList=data['hits']['hits']
  dataDict=dict()
  #print(dataList)
  for i in range(0,len(dataList)):
    print('reading abstract...'+str(i))
    if  'hasAbstractPart.text' in dataList[i]['fields']:
      absIDURIDict[dataList[i]['_id']]=dataList[i]['fields']['uri'][0]
  #return absIDURIDict
  
def mapIDUri(absIDKeywordFile,outputFile):
  global absIDURIDict
  infile=open(absIDKeywordFile,'r')
  outfile=open(outputFile,'w')    
  lines=infile.readlines()
  infile.close()
  for line in lines:
    line=line.strip()
    line=line.replace("\n","")
    absID=line.split(",")[0]
    keyword=line.split(",")[1]
    keyword=keyword.strip()
    printString=absIDURIDict[absID]+','+keyword
    outfile.write(printString)
    outfile.write("\n")
  outfile.close()
  
def main():
  global absIDURIDict
  #Check for proper arguments
  if len(sys.argv) != 4:
    print ('usage: python3 mapAbsIDWithURI.py dataFile absIDKeywordFile outputFile')
    sys.exit(1)
  #Scan inputs
  dataFile = sys.argv[1]
  absIDKeywordFile = sys.argv[2]
  outputFile = sys.argv[3]
  #Get all abstracts from data corpus
  getDocumentURIs(dataFile)
  mapIDUri(absIDKeywordFile,outputFile)
  #Get Noun list
  #absIdNounDict=getAbsNouns(absIdTextDict)
  #getAbsNouns(absIdTextDict)
  #printAbsNoun()

if __name__ == '__main__':
  main()
