
# Part 1
def name_output1(name):
	for i in range(0,len(name)):
		print name[i]['first_name'] + ' ' + name[i]['last_name']

students = [ 
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

name_output1(students)

# Part 2

def name_output2(name):
	for key, data in name.items():
		print key
		list_num = 0
		for value in data:
			list_num += 1
			full_name = value['first_name'] + ' '+ value['last_name']
			digits = len(value['first_name']) + len(value['last_name'])
			print '{} - {} - {}'.format(list_num, full_name, digits)

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

name_output2(users)

# answer sheet solution
'''
users = {
 'students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Trey', 'last_name' : 'Villafane'}
  ]
 }

for key, data in users.items():
	print "\n%s" %key.title()
	counter = 0

	for value in data:
		counter = counter +1
		full_name = value["first_name"] + " " + value["last_name"]
		full_name_upper = full_name.upper()
		name_count = len(value["first_name"]) + len(value["last_name"])
		
		print "%d - %s - %d" %(counter, full_name_upper, name_count)
'''