import os
import csv
from itertools import groupby

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
docFile = os.path.join(DIR, 'data/documents.csv')
contributorFile = os.path.join(DIR, 'data/contributors.csv')
criteriaFile = os.path.join(DIR, 'data/criteria.csv')

header = ['docid', 'headline','geography', 'industry', 'language', 'company', 'contributorid', 'contributor', 'category', 'downloads', 'views']
contributorHeader = ['contributorid', 'contributor', 'totalContribution']
criteriaHeader = ['searchid', 'date', 'searchType', 'searchValue', 'criteriaid', 'criteriaName', 'searchTypeId', 'searchType']

def regression():
	pass

#vars: total downloads of the contributor, total contributions of this contributor, each document's download times (formula to transform this certain range value)
def contributorRatio(algor):
	pass

#TODO: spearman correlation algorithm
def correlation(data):
	pass

#Control one field of metadata to change while the others stay the same,
#observe the changing (increase/decrease) of the document downloading/view rates 
#x-aixels the changing field var, y-aixels the value of the downloading and viewing
#leave headline & category alone

#controlCompare(data, ['geography', language', 'company', 'contributor'], [])
#maybe one by one...
def keyFunc(fields):
	f = lambda x, attrs: tuple([getattr(x, a) for a in attrs])
	if type(fields) is str:
		return lambda x: getattr(x, fields)
	else:
		return lambda x: f(x, fields)

def controlCompare(data, stableFields=None, changeFields='contributorid'):
	#Done: null ,value,
	#Done: from list to sort key
	#Done: make hashable key
	keyfunc = keyFunc(changeFields)
	groupData = sorted(data, key=keyfunc)
	
	if stableFields is None:
		pass
		#TODO: stabelFields is everything except for headline and category

	elif type(stableFields) is str:
		pass

	else:
		pass

	for k, g in groupby(groupData, key=keyfunc):
		groupDocs = list(g)
		downloadNum, downloadSum, viewSum = len(groupDocs), sum(int(getattr(x, 'downloads')) for x in groupDocs), \
		                                                                                                 sum(int(getattr(x, 'views')) for x in groupDocs)
		yield (k, downloadNum, downloadSum, viewSum)


class RecordObject(object):
	listFields = None
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

	def __setattr__(self, name, value):
		if RecordObject.listFields and name in RecordObject.listFields: 
			value = [value]
			super(RecordObject, self).__setattr__(name, value)
		else:
			super(RecordObject, self).__setattr__(name, value)

	def update(self, **record):
		for name in RecordObject.listFields:
			try:
				self.__getattribute__(name).append(record[name])
			except TypeError:
				print record


def packRecordObject(source, *args, **kwargs):#bad design
	recordObject = None
	if not kwargs or kwargs is None:
		for record in source(*args):
			yield RecordObject(**record)
	else:
		RecordObject.listFields = kwargs['fields']
		for record in source(*args):
			if recordObject is None:
				recordObject = RecordObject(**record)
			elif recordObject.__getattribute__(kwargs['key']) == record[kwargs['key']]:
				try:
					recordObject.update(**record)
				except TypeError:
					continue
			else:
				yield recordObject
				recordObject = RecordObject(**record)
		yield recordObject


def readcsv(filepath, delimiter='\t', header=header):
	with open(filepath, 'rU') as csvfile: #TODO: KeyError.. Ignore
		reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=header)
		for line in reader:
			yield line
