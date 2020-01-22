path = '/home/noam/job/job.txt'
fhandle = open(path,'r+')
jobstr = fhandle.read()
joblist = jobstr.split('\n')
joblist.reverse()
def jlist():
	for i in joblist:
		print (i.split('%'))

def add():
	jobstring = input("enter company name:") + '%' + input("enter position:") + '%' + input("enter date:") + '\n'
	fhandle.write(jobstring)
	print ('job was added')

def abclist():
	alphabetlist = joblist
	alphabetlist.sort()
	for i in alphabetlist:
		print (i.split('%'))

#def check():





while True:
	func = input ()
	if func == 'list':
		jlist()
	if func =='add':
		add()
	if func == 'exit':
		break
	if func == 'abclist':
		abclist()

	fhandle = open(path,'r+')
	jobstr = fhandle.read()
	joblist = jobstr.split('\n')
	joblist.reverse()


#functions:
#jlist - list all job aplliences sorted by date
#add - adds a job apliience to the list (check if already exist, if so - update the date)
#abclist - list all job aplences sorted alphabeticaly
#check - checks if an aplience exist and prints it if so

#company = input("enter company name:")
#position = input("enter position:")
#date = input("enter date:")
#job = (company, position, date)
#joblist = list()

