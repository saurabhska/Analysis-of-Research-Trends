Analysis of research trends

Description: the goal of this project is to construct a query/visualization system to analyze research trends using research publications. The system will crawl web sites of research societies and download papers including title, year, authors, affiliations, abstract and PDF. The system then extracts important words for a research area (e.g., in materials research, extract names of composite materials, polymers, processes, etc.). The project involves data cleaning, data integration and record linkage to construct a high-quality knowledge graph. Finally, the system will use visualizations to show the evolution of research trends and show where in the world different types of research is being conducted. 

******************************************************************************************************************************
findAbsKeywords.py : usage: python3 findAbsKeywords.py AbsIDNoun-dictionary-file mapping-file outputFile
                     AbsIDNoun-dictionary-file : File with dictionary of abstract id and nouns in abstracts
                     mapping-file : File with dictionary of nouns and keywords relaed to those nouns found by word2Vec tool
            
This script associates the research paper abstracts (abstractID) with the relevant keywords for those papers.
******************************************************************************************************************************
stemmer.py : This script performs stemming on the input file text.
******************************************************************************************************************************
distance.c.org : Original code of word2Vec tool
distance.c     : Code modified to accept multiple keywords from file to perform cosine similarity.
                 The word2Vec tool requires training data to be in a file named text8 and keywords to be in keywords.txt         
                 Link: https://code.google.com/p/word2vec/
******************************************************************************************************************************
findNounInText.py : usage: python3 findNounInText.py data-corpus-file
                    data-corpus-file : File containing abstracts data extracted out of elastic search.
This script reads the data-corpus-file, performs POS tagging on lines using NLTK and finds Nouns out of it.
******************************************************************************************************************************
searchAbsForKeyword.py : usage: python3 searchAbsForKeyword.py data-dictionary-file data-corpus-file
                         data-dictionary-file : File containing keywords to search
                         data-corpus-file     : File containing abstracts data extracted out of elastic search.
This script searches the abstract data for keywords to find the number of documents that contains the keywords and the number 
of times a keyword appears in each document.
******************************************************************************************************************************
