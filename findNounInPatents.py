import json
import sys
import os
import nltk
import pickle

absNounDict=dict()
def getDocumentAbstracts(fileNames,inputFilePath):
  dataDict=dict()
  fileCounter=0
  for dataFile in fileNames:
    fileCounter+=1
    print('processing file...'+str(fileCounter))
    dataFile=inputFilePath+dataFile
    json_data=open(dataFile,'r',errors='ignore')
    dataList=json.load(json_data)
    json_data.close()
    #dataList=data['hits']['hits']    
    #print(dataList)
    for i in range(0,len(dataList)):
      print('reading abstract...'+str(i))
      if  'Abstract' in dataList[i].keys():
        dataDict[dataList[i]['Publication Number']]=dataList[i]['Abstract']
  return dataDict


#def getAbsNouns(absIdTextDict):
	#for  absId,absText in absIdTextDict.items():
		#text=nltk.word_tokenize(absText)
		#taggedText=nltk.pos_tag(text)

def getAbsNouns(absIdTextDict):
  global absNounDict
  counter=0
  for absId,absText in absIdTextDict.items():
    counter+=1
    print('finding nouns in abstract......'+str(counter))
    text=nltk.word_tokenize(absText)
    taggedText=nltk.pos_tag(text)
    tempList=list()
    for word, pos in taggedText:
      if 'NN' in pos:
        tempList.append(word)
    absNounDict[absId]=tempList
    #if counter == 30:
      #break
        #print(pos)
      #if counter==0:
        #print(absText)
        #print(taggedText)
        #counter=1

def printAbsNoun():
  global absNounDict
  outfile=open('absNoun.out','wb')
  pickle.dump(absNounDict, outfile)
  outfile.close()


def main():
  #Check for proper arguments
  global absIdNounDict
  if len(sys.argv) != 2:
    print ('usage: python3 findNounInPatents.py input-path')
    sys.exit(1)
  #Scan inputs
  #dataFile = sys.argv[1]
  inputFilePath = sys.argv[1]
  fileNames=sorted(os.listdir(inputFilePath))
  #Get all abstracts from data corpus
  absIdTextDict=getDocumentAbstracts(fileNames,inputFilePath)
  #print(absIdTextDict)
  #print(absIdTextDict.keys())
  #print(str(len(absIdTextDict.keys())))
  #Get Noun list
  getAbsNouns(absIdTextDict)
  #print(absNounDict)
  #getAbsNouns(absIdTextDict)
  printAbsNoun()

if __name__ == '__main__':
  main()
