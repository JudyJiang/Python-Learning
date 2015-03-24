import re
import sys
from itertools import groupby
from collections import Counter, defaultdict
from datetime import datetime, timedelta


#TODO: build Filter pipeline
#TODO: transform data into pipeline
#TODO: maybe keep a filtering class just to filtering!!!!! (inside both Parser & Analytics)
# This filter function takes argument as "function names" and when Parser & Record object calls it it can use the lambda~!!!
#TODO: Clean up code (separate classes) after get the feature popularity
class IISFormat(): 
	FIELDS_PREFIX = '#Fields'
	DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
	iis_patern = {
	                'date' : '(?P<date>^\d+[-\d+]+',
	                'time' : '[\d+:]+)[.\d]*?',
	                'cs-uri-stem' : '(?P<path>/\S*)',
	                'cs-uri-query' : '(?P<query>\S*)',
	                'c-ip': '"?(?P<ip>[\d*.]*)"?', #?
	                'cs(User-Agent)' : '(?P<agent>".*?"|\S+)',
	                'cs(Cookie)':'(?P<cookie>".*?"|\S+)',
	                'cs(Referer)' : '(?P<referrer>\S+)',
	                'cs-host' : '(?P<host>\S+)',
	                'sc-status' : '(?P<status>\d+)',
	                'sc-bytes' : '(?P<length>\S+)',
	                'cs-username' : '(?P<uname>\S+)',
	                'time-taken' : '(?P<generation_time>[.\d]+)' #0.15sec... 
	                    }

	def __init__(self):
		self.regex = None
		self.date_format = self.DATE_FORMAT #if no other specified


	def create_regex(self, line):
		try:
			line_fields = line.split()
			field = line_fields[0].replace(':', '')
			line_fields = line_fields[1::]
			if field == self.FIELDS_PREFIX: 
				full_regex = []
				for field in line_fields:
					try:
						tmp_regex = self.iis_patern[field]
					except KeyError:
						tmp_regex = '\S+'
					full_regex.append(tmp_regex)
				full_regex = '\s+'.join(full_regex)
				self.regex = full_regex
				return True
			else: 
				print ("Current not support pattern: {p}".format(p=line))
		except Exception: #in case it's an empty line  (rarely)
			print ("Unbreakable field: ".format(line))

	def match(self, line):
		return re.compile(self.regex).match(line)



#this class takes care of each line within the file
class Parser():
	
	def __init__(self):
		pass

	@staticmethod
	def detect_format(line):
		#TODO: haven't figure out how to detect format when there're multiple log formats.
		if line.startswith('#Fields'):
			return FORMATS['IIS']
		return None


	#Done: read several lines of the file until find the format
	#TODO: what if one large log file chunck into several smaller log files? 
	#      How to achieve chunck reading?
	def read_format(self, file):
		line_limit = 100 #set line number limit. 
		line_num = 0
		format = False
		while not format and line_num < line_limit:
			line = file.readline()
			if not line or not line.startswith('#'):
				break
			line_num += 1
			format = Parser.detect_format(line)
			if format:
				format.create_regex(line)
				break

		return format


	#remove cookie without logging info but only machineId (system server self generated)
	def check_useful_cookie(self, cookie):
		if cookie in ('-', ' ', '', None):
			return None
		sessionid = None
		cookie_session = ['ObSSOCookie=', 'ASP.NET_SessionId=', 'userLoggedIn=']
		if any(x in cookie for x in cookie_session):
			pos = 0
			end = '[;|]'
			while pos < len(cookie_session):
			    try:
			    	start = cookie_session[pos]
			    	regex = start + '(.*?)' + end
			    	r = re.compile(regex)
			    	m = r.search(cookie)
			    	if m :
			    		sessionid = m.group(1)
			    		break
			    	pos += 1
			    except ValueError:
			    	sessionid = None
			    	pos += 1

		return sessionid
		

	#TODO: if batch reading, first set parameters in Config class to detect a folder or a file
	#TODO: shrink the parser cleaning!Shrink the code here!
	#      setup parameter in both Config and Parse class. Then Parser knows it's continue reading
	#      when parameter (boolean most likely) is set, Parse.parse won't detect format but use previous
	#      format object to continue reading & parsing
	def parse(self, filename):
		records = [] #list container for all the records within the log file
		try:
			with open(filename) as logfile:
				format = self.read_format(logfile) #will continue reading after find the #Fields
				for lineno, line in enumerate(logfile):
					try:
						line_match = format.match(line)
					except UnicodeDecodeError:
						print ("Invalid line not in unicode style {l}".format(l=line))
						continue #ignore invalid line or record invalid line
					
					if not line_match:
						print ("Invalid line doesn't match IIS format: {l}".format(l=line))
						continue

					#first remove record if without cookie (not logged in)

					line_match = line_match.groupdict()
					sessionid = self.check_useful_cookie(line_match['cookie'])
					if not sessionid:
						continue
					user_request = Record.check_useful_request(line_match['path'])
					if not user_request:
						continue

					record = Record(
						sessionid=sessionid,
						path=line_match['path'],
						action=False,
						error_page=False, 
						redirect_page=False)
					#DONE: check & set query, agent, uid, ip, host and status
					record.query = line_match['query'] if line_match['query'] is not '-' else ''
					record.agent = line_match['agent'] if line_match['agent'] is not '-' else ''
					record.uid = line_match['uname'] if line_match['uname'] is not '-' else ''
					record.ip = line_match['ip']
					record.host = line_match['host']
					record.status = line_match['status']
					record.referer = line_match['referrer']

					#DONE: check & set date
					date_time = line_match['date']
					try:
						date_time_record = datetime.strptime(date_time, format.date_format)
						record.date = date_time_record.date()
						record.time = date_time_record.time()
					except ValueError:
						print ('Raise time format error, \
							either invalid line or incompatible date format: \
							lineno: {_lineno} line: {_line}'.format(_lineno=lineno, _line=line))
						record.date = None
						record.time = None
						continue

					try:
						record.length = int(line_match['length'])
					except (ValueError, BaseFormatException):
						record.length = 0

					try:
						record.generation_time = float(line_match['generation_time'])
					except (ValueError, BaseFormatException):
						pass
					record.clean_check()
					records.append(record)
		except IOError:
			print ('Raise file error: {f}'.format(f=filename))
			sys.exit(1)
		print len(records)
		analytics = Analytics(records)
		analytics.page_view()


#this class is like a container for each line in the log
class Record():
	PERSERVE_EXTENSION = ['aspx', 'asmx', 'ashx', 'asp', 'html', 'htm', 'js']

	#many attributes to be expected, but all setup in Parser.parse
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

	@staticmethod
	def check_useful_request(request):
		extension = None
		try:
			routes = request.split('/')
			last_route = routes[len(routes) - 1]
			extensions = last_route.split('.')
			if len(extensions) < 2:
				#the only way I can think of...
				return 'action'
			extension = extensions[len(extensions) - 1]
			if extension not in Record.PERSERVE_EXTENSION:
				return None
			else:
				return extensions[len(extensions) - 1]
		except IndexError:
			return None

	def clean_check(self):
		self.check_error_page()
		self.check_redirect()
		pass


<<<<<<< HEAD
=======
	def regulate_Record(self):
		pass 
		#TODO: a method that can identify the object ? hashtable for accessing values?

>>>>>>> 93c48172b9c3eddb661d75fb2595bb6c236b1f1b
	def check_error_page(self):
		try:
			start = self.status[0]
			if start in ('4', '5'):
				self.error_page = True
		except ValueError:
			self.error_page = True

	def check_redirect(self):
		try:
			if self.status.startswith('3') and self.status != '304':
				self.redirect_page = True
		except ValueError:
				self.error_page = True






#this class takes data imported from Parser and analyze it...
#TODO: implement analytics functions, recorders
class Analytics():

	def __init__(self, records):
		self.records = records

	def group_by_attr(self, attr):
		sorted_records = sorted(self.records, key=lambda r : getattr(r, attr))
		self.attr_groups = []
		uniquekeys = []
		counter = Counter()
		for k, g in groupby(sorted_records, key=lambda r : getattr(r, attr)):
			#serves as a iterator to iterate through the self.records based on the 'attr' value
			group = list(g)
			self.attr_groups.append(group)
			uniquekeys.append(k)
			counter[k] = len(group)


	def group_by_time(self, time):
		self.time_group = None
		pass 
		#set time limits (in seconds )

	def get_root_url(self):
		pass

<<<<<<< HEAD
	def extract_page(self, group):
		pass
		#Cond1 : same referer, same request, same date:time one referer & one request if service go up until page level
		#Cond2 : Continuous same Referer with same request different time & date
		#Cond3 : Continuous same Referer with different request same date & time: one referer & sever request page if service go up until page level
		#Cond4 : Continuous same Referer with different request differnet date & time: set time limits
		#return page

	def page_view(self):
		self.group_by_attr('sessionid')
		#each group is a user-session (records with same sessionid)
=======
	def get_page(self, referer, request):
		page = None
		#if not referer, check request in correct format or useful actions, return request page
		#if referer
		return page

	def page_view(self, type):
		self.group_by_attr('sessionid')
		page_view = defaultdict(int)
		for group in self.attr_groups:
			page_view[self.get_page] += 1
		return page_view
		


>>>>>>> 93c48172b9c3eddb661d75fb2595bb6c236b1f1b

	def session_activity(self):
		self.group_by_attr('sessionid')

		pass		


#TODO: Build dictionary for different appendix


	
#TODO: add more formats.
#this is a static dictionary that defines all the formats currently support
FORMATS = {'IIS' : IISFormat()}

def main():
	parser = Parser()
	parser.parse('log/001.log')
	#Analytics.teststatoc()
	


if __name__ == '__main__':
	sys.exit(main())