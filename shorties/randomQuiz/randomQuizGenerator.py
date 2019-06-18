#! python3
# randomQuizGenerator.py - creates quizzes with questions and answers in 
# random order, along with the answer key
import random
import os

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(2):
  # Create the quiz and answer key
  # looks like there's an easy way to do string concat here
  
  quizFile = open('./shorties/randomQuiz/quizes/capitalquiz%s.txt' % (quizNum + 1), 'w')
  answerKeyFile = open('./shorties/randomQuiz/quizes/capitalquiz_answers%s.txt' % (quizNum + 1), 'w')

  #  write out the header for the quiz
  quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
  quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
  quizFile.write('\n\n')

  # Shuffle the order of the states
  states = list(capitals.keys())
  random.shuffle(states)

  # Loop through all 50 states, making a question for each
  for questionNum in range(50):
    # select a correct answer by state name from the keys
    correctAnswer = capitals[states[questionNum]]
    # duplicate all the values from the capitals dict into a new list
    wrongAnswers = list(capitals.values())
    # delete the right answer from the duplicated list
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    # use random to get 3 random wrong answers
    wrongAnswers = random.sample(wrongAnswers, 3)
    # create a list of answer options
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    #write the question and the answer options to the quiz file
    quizFile.write('%s. What is the capital of %s?\n\n' % (questionNum + 1, states[questionNum]))
    for i in range(4):
      quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
      quizFile.write('\n')

    #write the answer key to a file
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    
  quizFile.close()
  answerKeyFile.close()
