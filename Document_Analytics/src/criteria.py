import sys
from collections import Counter
import utility as util


#change later
def criteriaUsage(item):
	return Counter(set(item))


def main():
	records = util.packRecordObject(util.readcsv,util.criteriaFile,'\t',util.criteriaHeader,
													key='searchid',fields=['searchValue','criteriaid','criteriaName'])
	records = list(records)
	criterialHistogram = Counter()
	for record in records:
		criterialHistogram += criteriaUsage(record.criteriaName)

	print (criterialHistogram)
	


if __name__ == '__main__':
	sys.exit(main())
