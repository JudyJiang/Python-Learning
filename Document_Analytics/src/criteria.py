 import sys
from utility import *
from collections import Counter, defaultdict

#Goal:
'''
1. Finish this global staff 
2. Give out the usage of current criterias (Explain this is user's search criteira, different from downloads criteira)
    This is different from google search? Cause no matter what they search, we'll always return staff (documents) which matches their search
3. Next step is to analyze criteria factor for their downloads. Use prefer to search based on this, if this pattern matches their downloading patterns.
    Or they have several perference over several contributors and companies.
4. Find out the Analyst

    This weekend read & learn Spearmen correlation & stanford one staff.

    Tonight post one blog about 
    1. Generator consumer (your high-order function can be considered)
    2. multiple function global variables
'''
def criteriaUsage(item):
	#return two dictionaries. one define search involve which criterial. the other define if they use this criteria multiple times
	return Counter(set(item))

def criteriaUsageI(item):
	pass



def main():
	records = packRecordObject(readcsv, criteriaFile, '\t', criteriaHeader, key='searchid', fields=['searchValue','criteriaid','criteriaName'])
	records = list(records)
	criteriaHist = Counter()
	for record in records:
		criteriaHist += criteriaUsage(record.criteriaName)

	print len(records)
	for item in criteriaHist.items():
		print item

if __name__ == '__main__':
	sys.exit(main())

'''class Consumer(object):
	def send(self, item):
		print self, "got", item


def gen(times=10):
	count = 0
	while count < times:
		yield count + 1
		count += 1

def broadcast(source, consumer):
	for item in source:
		for c in consumer:
			c.send(item)

c1 = Consumer()
c2 = Consumer()
c3 = Consumer()

res = gen(10)
broadcast(res, [c1, c2, c3])'''