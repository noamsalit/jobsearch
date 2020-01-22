path = '/home/noam/job/job.txt'
fhandle = open(path,'r+')
jobstr = fhandle.read()
joblist = jobstr.split('\n')
joblist.reverse()
def jlist():
	for i in joblist:
		print (i.split('%'))

def add():
	jobstring = input('enter company name:') + '%' + input('enter position:') + '%' + input('enter date:') + '\n'
	fhandle.write(jobstring)
	print ('job was added')

def abclist():
	alphabetlist = joblist
	alphabetlist.sort()
	for i in alphabetlist:
		print (i.split('%'))

def check():
	company =  input('enter company name:')
	position = input('enter position:')
	for i in joblist:
		if company == i.split('%')[0]:
			if position == i.split('%')[1]:
				return(print ('applied in',i.split('%')[2]))
	print('never applied')



while True:
	func = input ()
	if func == 'list':
		jlist()
	elif func =='add':
		add()
	elif func == 'exit':
		break
	elif func == 'abclist':
		abclist()
	elif func == 'check':
		check()
	else:
		print('no such function')

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

