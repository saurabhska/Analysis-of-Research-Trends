import json
import sys
import os
import nltk
import pickle

absNounDict=dict()
def getDocumentAbstracts(dataFile):
  json_data=open(dataFile,'r',errors='ignore')
  data=json.load(json_data)
  json_data.close()
  dataList=data['hits']['hits']
  dataDict=dict()
  #print(dataList)
  for i in range(0,len(dataList)):
    print('reading abstract...'+str(i))
    if  'hasAbstractPart.text' in dataList[i]['fields']:
      dataDict[dataList[i]['_id']]=dataList[i]['fields']['hasAbstractPart.text'][0]
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
  if len(sys.argv) != 2:
    print ('usage: python3 findNounInText.py data-corpus-file')
    sys.exit(1)
  #Scan inputs
  dataFile = sys.argv[1]
  #Get all abstracts from data corpus
  absIdTextDict=getDocumentAbstracts(dataFile)
  #Get Noun list
  #absIdNounDict=getAbsNouns(absIdTextDict)
  getAbsNouns(absIdTextDict)
  printAbsNoun()

  

if __name__ == '__main__':
  main()
