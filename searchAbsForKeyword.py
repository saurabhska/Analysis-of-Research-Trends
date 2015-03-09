import json
import sys
import os


def countKeywordOccurrences(keywordList,dataDict):
  eachDocumentFrequencyWriterEZC=open('eachDocFreq_excZeroCnt.out','w',errors='ignore')
  eachDocumentFrequencyWriterIZC=open('eachDocFreq_incZeroCnt.out','w',errors='ignore')
  allDocumentFrequencyWriter=open('allDocFreq.out','w',errors='ignore')
  temp=0
  for word in keywordList:
    allDocWordCount=0
    for docID,docText in dataDict.items():
      wordCount=docText.lower().count(word.lower())
      if wordCount !=0:
        eachDocumentFrequencyWriterEZC.write(docID+' ---> '+word+' ---> '+str(wordCount)+'\n')
        allDocWordCount+=1
        #print(docID+' : '+word+' : '+str(allDocWordCount))
      eachDocumentFrequencyWriterIZC.write(docID+' ---> '+word+' ---> '+str(wordCount)+'\n')
    allDocumentFrequencyWriter.write(word+' ---> '+str(allDocWordCount)+'\n')
    temp=temp+1
    print('completed processing word...'+str(temp))
  eachDocumentFrequencyWriterEZC.close()
  eachDocumentFrequencyWriterIZC.close()
  allDocumentFrequencyWriter.close()

def getDocumentAbstracts(dataFile):
  json_data=open(dataFile,'r',errors='ignore')
  data=json.load(json_data)
  json_data.close()
  dataList=data['hits']['hits']
  dataDict=dict()
  docsWithNoAbstractWriter=open('docsWithNoAbstract.out','w',errors='ignore')
  docsWithAbstractWriter=open('dataAbstracts.out','w',errors='ignore')
  #print(dataList)
  for i in range(0,len(dataList)):
    if  'hasAbstractPart.text' in dataList[i]['fields']:
      dataDict[dataList[i]['_id']]=dataList[i]['fields']['hasAbstractPart.text'][0]
      docsWithAbstractWriter.write(dataList[i]['fields']['hasAbstractPart.text'][0])
    else:
      docsWithNoAbstractWriter.write(dataList[i]['_id'])
      docsWithNoAbstractWriter.write('\n')
  docsWithNoAbstractWriter.close()
  return dataDict

def getKeywords(keywordFile):
  #read keywords from input file, remove end of line character and return keyword list.
  infile=open(keywordFile,'r',errors='ignore')
  lines=infile.readlines()
  keywordList=list()
  for line in lines:
    line=line.replace('\n', '').replace('\r', '')
    keywordList.append(line)
  return keywordList

def main():
  #Check for proper arguments
  if len(sys.argv) != 3:
    print ('usage: python3 searchAbsForKeyword.py data-dictionary-file data-corpus-file')
    sys.exit(1)
  #Scan inputs
  keywordFile = sys.argv[1]
  dataFile = sys.argv[2]
  #Get a list of keywords from input file
  keywordList=getKeywords(keywordFile)
  #Get all abstracts from data corpus
  dataDict=getDocumentAbstracts(dataFile)
  #count occurences and output to a file
  countKeywordOccurrences(keywordList,dataDict)

  

if __name__ == '__main__':
  main()
