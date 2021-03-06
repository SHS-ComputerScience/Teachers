""" ------------------------------------------
	OCR GCSE (9-1) Computer Science
	J276-03 Programming Project (NEA): Task 1
	June 2018 Series

	Candidate Number:
	Candidate Name:

	Centre Number: 16135
	Centre Name: Shenfield High School
	------------------------------------------
	"""
# --------------------------------------------
#  Imported modules
# --------------------------------------------

import os
import random
from getpass import getpass # to mask password input

# --------------------------------------------
#  Global constants / variables
# --------------------------------------------

PATH = os.path.dirname(os.path.realpath(__file__))
USERFILE = '/data/userdata'
RESULTFILE = '/data/resultdata'
QNA_PATH = '/questions'

DIFFICULTY_LEVELS = { 1: 'Easy', 2: 'Medium', 3: 'Hard' }

# --------------------------------------------
#  Common functions
# --------------------------------------------

def load(filename): # error-handle
	""" Returns the content of filename (string)
		line by line as a list of strings.
		"""
	with open(PATH + filename) as file:
		return file.read()
		# with implies file.close()

def save(filename, data): # error-handle
	""" Appends data to end of filename (string)
		if it exists or creates new file if not.
		"""
	with open(PATH + '/' + filename, 'a+') as file:
		file.write(str(data) + '\n')
		# with implies file.close()

def parse_data(filedata): # error-handle
	"""
		"""
	parsed_data = []
	start = 0
	while True:
		end = filedata.find('}', start) + 1
		if end == 0:
			break
		else:
			parsed_data.append(eval(filedata[start:end]))
			start = end
	return parsed_data

def valid_input(obj, char_type=None, min_range=None, max_range=None):
	"""
		"""
	# presence check
	if not len(obj) > 0:
		print('ERROR: Field cannot be blank.')
		return False

	# type check
	if char_type == 'alpha' and not obj.isalpha():
		print('ERROR: Please input alpha characters only.')
		return False
	elif char_type == 'int':
		try:
			int(obj)
		except:
			print('ERROR: Please input a whole number.')
			return False

	# range check
	if min_range != None and max_range != None:
		if char_type == 'int':
			if int(obj) < min_range or \
			   int(obj) > max_range:
				print('ERROR: Value must be between {} and {} (inclusive).'.format(min_range, max_range))
				return False

	return True

# --------------------------------------------
#  User access functions
# --------------------------------------------

def get_access():
	""" Function to handle user login/registration.
		"""
	while True:

		print('1. Login')
		print('2. Register')
		print('3. Quit')

		option = input('> ')

		if option == '1':
			userdata = login()
			if userdata != None:
				return userdata

		elif option == '2':
			userdata = register()
			if userdata != None:
				return userdata

		elif option == '3':
			return None

def login():
	"""
		"""
	userfile = parse_data(load(USERFILE))

	username = input('Enter username: ')
	password = getpass('Enter password: ') # get input without echoing to screen

	for i in range(len(userfile)):

		if username == userfile[i]['username'] and \
		   password == userfile[i]['password']:

			return userfile[i]

	# else if no username-password match
	print('ERROR: Invalid username or password.')
	return None

def register():
	"""
		"""
	while True:

		# get name
		while True:
			name = input('Enter name: ')
			if valid_input(name, 'alpha'):
				break

		# format name (title case)
		name = name[0].upper() + name[1:].lower()

		# get age
		while True:
			age = input('Enter age: ')
			if valid_input(age, 'int', 1, 99):
				break

		# get year group
		while True:
			year = input('Enter year group: ')
			if valid_input(year, 'int', 7, 11):
				break

		# confirm details
		print('Name: {}\nAge: {}\nYear Group: {}'.format(name, age, year))

		while True:
			user_input = input('Proceed with these details? (y/n) ').lower()

			if user_input == 'y':
				details_confirmed = True
				break
			elif user_input == 'n':
				details_confirmed = False
				break

		if details_confirmed:
			break
		else:
			while True:
				user_input = input('Cancel registration? (y/n) ').lower()

				if user_input == 'y':
					return None
				elif user_input == 'n':
					break

	userfile = parse_data(load(USERFILE))
	autonumber = 0

	while True:
		if autonumber == 0:
			trailer = ''
		else:
			trailer = str(autonumber)

		username = name[:3].lower() + age + trailer

		exists = False
		for i in range(len(userfile)):
			if username == userfile[i]['username']:
				exists = True
				autonumber += 1
				break
		if not exists:
			break

	print('Your username is', username)

	while True:
		password = getpass('Create password: ')
		passconf = getpass('Confirm password: ')

		if password == passconf:
			save(USERFILE, { 'username' : username,
								  'password' : password,
								  'name'     : name,
								  'age'      : age,
								  'year'     : year
								}
				 )
			print("Your account has been successfully registered!")
			return True
		else:
			print('ERROR: Password mismatch.')

			while True:
				user_input = input('Try again? (y/n) ').lower()

				if user_input == 'y':
					break
				elif user_input == 'n':
					return None

# --------------------------------------------
#  Main menu function
# --------------------------------------------

def main_menu(savedata):
	"""
		"""
	while True:
		print('1. Take Quiz')
		print('2. Run Report')
		print('3. Quit')

		option = input('> ')

		if option == '1':
			take_quiz(savedata)
		elif option == '2':
			report_menu()
		elif option == '3':
			return False

# --------------------------------------------
#  Quiz functions
# --------------------------------------------

def take_quiz(savedata):
	"""
		"""
	savedata['topic']      = select_topic()
	savedata['difficulty'] = select_difficulty()
	savedata['questions']  = get_questions(savedata['topic'],
													   savedata['difficulty'])
	savedata['results']    = get_results(savedata['questions'])

	display_results(savedata['results'])
	store_results(savedata)

def select_topic():
	"""
		"""
	key = 1
	topics = {}
	for file in os.listdir(PATH + QNA_PATH):
		if file.endswith('.qna'):
			topics[str(key)] = file
			key += 1

	while True:
		# display topic options
		for key in sorted(list(topics)):
			print('{}. {}'.format(key, topics[key][0].upper() + topics[key][1:-4]))

		option = input('> ')

		if option in topics:
			return QNA_PATH + '/' + topics[option]

def select_difficulty():
	"""
		"""
	for key in DIFFICULTY_LEVELS:
		print('{}. {}'.format(key, DIFFICULTY_LEVELS[key]))

	while True:
		option = input('> ')

		if valid_input(option, 'int', 1, len(DIFFICULTY_LEVELS)):
			return int(option)

def get_questions(topic, difficulty):
	"""
		"""
	questions = []

# 	# get topic questions and answers from file
	question_data = load(topic)
	question_data = parse_data(question_data)

	# shuffle questions & answers
	random.shuffle(question_data)

# 	# extract individual questions and answers
	for i in range(len(question_data)):
		question = question_data[i]['question']
		correct_answer = question_data[i]['correct_answer']
# 		incorrect_answers = list(question_data[i][2:])
		incorrect_answers = question_data[i]['incorrect_answers']
# 		# shuffle incorrect answers
		random.shuffle(incorrect_answers)
# 		# add correct answer to list of answers displayed
		displayed_answers = [correct_answer]

# 		# check if sufficient answers for difficulty level
		if difficulty > len(incorrect_answers): # <<<<< TEST!!!
			print('ERROR: Too few answers on file for current difficulty level.')
			break

# 		# add incorrect answers displayed based on difficulty
		for i in range(difficulty):
			displayed_answers.append(incorrect_answers[i])

# 		# shuffle answers displayed
		random.shuffle(displayed_answers)

# 		# append to questions dict
		questions.append({'question' : question,
								'correct_answer' : correct_answer,
								'displayed_answers' : displayed_answers
							  })
	return questions

def get_results(questions):
	"""
		"""
	score = 0

	for question in questions:
		score += ask_question(question)

	total = len(questions)
	percentage = get_percentage(score, total)

	return { 'score' : score,
		      'total' : total,
		      'percentage' : percentage,
		      'grade' : get_grade(percentage)
		    }

def ask_question(question_data):
	"""
		"""
	question = question_data['question']
	correct_answer = question_data['correct_answer']
	displayed_answers = question_data['displayed_answers']
	number_of_answers_displayed = len(displayed_answers)

	while True:
		print(question)
		for i in range(number_of_answers_displayed):
			print('{}. {}'.format(i + 1, displayed_answers[i]))

		user_answer = input('> ')
		if valid_input(user_answer, 'int', 1, number_of_answers_displayed):
			# get actual answer from user_answer index
			user_answer = displayed_answers[int(user_answer) - 1]
			if user_answer == correct_answer: # answer check
				print('Correct!')
				return 1 # 1 point
			else:
				print('Incorrect!')
				return 0 # 0 points

def get_percentage(number, total):
	"""
		"""
	return number / total

def get_grade(percentage):
	"""
		"""
	if percentage >= 0.8:
		return 'A'
	elif percentage >= 0.6:
		return 'B'
	elif percentage >= 0.4:
		return 'C'
	elif percentage >= 0.2:
		return 'D'
	else:
		return 'U'

def display_results(results):
	"""
		"""
	print('Score: {} out of {} ({:.2%})'.format(results['score'],
															  results['total'],
															  results['percentage']))
	print('Grade:', results['grade'])

def store_results(savedata):
	"""
		"""
	save(RESULTFILE, { 'username'   : savedata['user']['username'],
							 'name'       : savedata['user']['name'],
							 'age'        : savedata['user']['age'],
							 'year'       : savedata['user']['year'],
							 'topic'      : savedata['topic'],
							 'difficulty' : savedata['difficulty'],
							 'score'      : savedata['results']['score'],
							 'grade'      : savedata['results']['grade']
						  }
		 )

# --------------------------------------------
#  Report functions
# --------------------------------------------

def report_menu():
	"""
		"""
	while True:
		print('1. Run User Report')
		print('2. Run Topic Report')
		print('3. Go Back')

		option = input('> ')

		if option == '1':
			run_user_report()
		elif option == '2':
			run_topic_report()
		elif option == '3':
			break

def run_user_report():
	"""
		"""
	# load & parse resultdata
	resultdata = parse_data(load(RESULTFILE))

	while True:
		# get username
		username = input("Enter username for report: ").lower()
		print('Quizzes taken by {}:'.format(username))

		# get all topics and grades for username
		count = 0
		for record in resultdata:
			if record['username'] == username:
				count += 1
				print('{}. {}, Grade: {}'.format(count,
															record['topic'],
															record['grade']))
		if count == 0:
				print('No results found for user \'{}\'!'.format(username))

		while True:
			user_input = input('Run another report? (y/n) ').lower()
			if user_input == 'y':
				stop = False
				break
			elif user_input == 'n':
				stop = True
				break
		if stop:
			break

def run_topic_report():
	"""
		"""
	# load and parse resultdata
	resultdata = parse_data(load(RESULTFILE))

	# get recorded topics
	saved_topics = []
	for record in resultdata:
		if record['topic'] not in saved_topics:
			saved_topics.append(record['topic'])

	count = 0
	for topic in sorted(saved_topics):
		count += 1
		print('{}. {}'.format(count, topic))

	if count > 0:
		while True:
			option = input('> ')
			if valid_input(option, 'int', 1, count):
				topic = saved_topics[int(option) - 1]
				break

		# get recorded difficulties
		saved_difficulties = []
		for record in resultdata:
			if record['topic'] == topic and \
				record['difficulty'] not in saved_difficulties:
				saved_difficulties.append(record['difficulty'])

		count = 0
		for difficulty in sorted(saved_difficulties):
			count += 1
			print('{}. {}'.format(count, DIFFICULTY_LEVELS[difficulty]))

		if count > 0:
			while True:
				option = input('> ')
				if valid_input(option, 'int', 1, count):
					difficulty = saved_difficulties[int(option) - 1]
					break
		else:
			print('No records found')
	else:
		print('No records found')

	# get all scores and user details for topic & difficulty
	reportdata = []
	for record in resultdata:
		if resultdata['topic'] == topic and resultdata['difficulty'] == difficulty:
			reportdata.append(record)

	# calculate average score


	# calculate highest score and dispay user details

# --------------------------------------------
#  Main function
# --------------------------------------------

if __name__ == '__main__':
	""" Main program
		"""
# 	savedata = {} # container for user and quiz data

# 	savedata['user'] = get_access()

# 	if savedata['user'] != None:
# 		main_menu(savedata)
# 	else:
# 		print('Goodbye!')

#  TESTING -----------------------------------------------
#  savedata = {'questions': [{'question': 'Which three countries share their borders with Cambodia?', 'correct_answer': 'Laos, Thailand and Vietnam', 'displayed_answers': ['Laos, Thailand and Vietnam', 'China, Laos and Myanmar']}, {'question': 'Which is the highest country in the world?', 'correct_answer':'Bhutan', 'displayed_answers': ['Lesotho', 'Bhutan']}, {'question': 'Which is the smallest continent in the world?', 'correct_answer': 'Australia', 'displayed_answers': ['Australia', 'Antarctica']}, {'question': 'Which is the largest sea in the world?', 'correct_answer': 'The Philippine Sea','displayed_answers': ['The South China Sea', 'The Philippine Sea']}, {'question': 'What is the captial of Australia?', 'correct_answer': 'Canberra', 'displayed_answers': ['Sydney', 'Canberra']}], 'difficulty': 1, 'results': {'grade': 'B', 'total': 5, 'score': 3, 'percentage': 0.6}, 'topic': '/questions/geography.qna'}
# 	savedata['username'] = 'tes16'
# 	savedata['password'] = 'password'
# 	savedata['name']     = 'Test User'
# 	savedata['age']      = 16
# 	savedata['year']     = 11
#  savedata['results']['score'] = 4
#  savedata['results']['grade'] = 'A'
#  store_results(savedata)

	run_topic_report()
