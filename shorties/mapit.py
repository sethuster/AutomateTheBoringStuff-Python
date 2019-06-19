#! python3
# mapit.py - Lauches a map in the browser using an address from the command line or the clipboard
import webbrowser, sys, logging, pyperclip
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Arguments: ' + str(sys.argv))

if(len(sys.argv) > 1):
  # get address from the command line
  address = ' '.join(sys.argv[1:]) #slice off all args except index 0 - sys.argv[0] is the filename?
else: 
  # get address from clipboard
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
