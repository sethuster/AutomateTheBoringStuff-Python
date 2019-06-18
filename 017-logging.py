#! python3
import logging
# This will disable the log messages from being displayed
# logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# writes the log output to a file instead
# logging.basicConfig(filename='mylogfile.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of Factorial(%s)' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(%s)' % (n))
  return total

print(factorial(5))
logging.debug('End of program')

# Log levels 
# logging.debug() - The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
# logging.info() - Used to record information on general events in your program or confirm that things are working at their point in the program.
# logging.warning() - Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
# loggin.error() - 	Used to record an error that caused the program to fail to do something.
# logging.critical() - The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
