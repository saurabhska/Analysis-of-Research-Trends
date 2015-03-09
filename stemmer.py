import sys
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def main():
  #Check for proper arguments
  if len(sys.argv) != 2:
    print ('usage: python3 stemmer.py inputFile')
    sys.exit(1)
  #Scan inputs
  inputFile = sys.argv[1]
  infile=open(inputFile,'r',errors='ignore')
  lines=infile.readlines()
  for line in lines:
    line=line.replace("\n","")
    print(stemmer.stem(line))
  
if __name__ == '__main__':
  main()
