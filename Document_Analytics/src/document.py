import sys
from utility import *

PTHRESOLD = 1000

#headline
#contributor3 
#primary-company
#enter date
#file date
#edit datee



#geography and language is computed differently
# first user's usage in search perfernce (not specified normally)
# file date, edit date, 

#one research document can have multiple category tags and somehow the sequence matters (which category donimates.)
#different samples



def main():
	documents = packRecordObject(readcsv,docFile,'\t',header,key='docid',fields=['category'])
	documents = list(documents)[0:100]
	for i in documents:
		print i.geography, i.language, i.company, i.contributor, i.category, i.downloads
		print 

	#contributors = controlCompare(documents, None, 'category')
	#sortedContributors = sorted(contributors, key=lambda x: x[1], reverse=True)
	#print sortedContributors[0:20]

if __name__ == '__main__':
	sys.exit(main())