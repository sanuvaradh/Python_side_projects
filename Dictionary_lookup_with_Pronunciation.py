'''
Access dictionary information like meanings and word pronunciations by using wordnik module

1. Access all meanings of a given word and print them.
2. Access and open url's to pronounce the given word.

'''

import sys,os,time
from wordnik import *
import webbrowser

def main():

    while(1):

        print '\nType \'exit\' to exit this script\n '
        user_input = raw_input('Please enter a word: ')
        apiToken = '*********************************'
        apiUrl = 'http://api.wordnik.com/v4'

        #Exit program if user input is 'exit'
        if( user_input == 'exit'):
            print "\n Exiting script!!! \n"
            sys.exit()

        try:
            client = swagger.ApiClient(apiToken, apiUrl)
            wordApi = WordApi.WordApi(client)
            meanings = wordApi.getDefinitions(user_input)

            #Print word meanings
            counter = 0 
            print "Following are the meanings to the word {} \n" .format(user_input)
            for meaning in meanings:
                counter = counter + 1
                print str(counter) + '. ' + meaning.text

            #Play pronunciations
            pronunciations = wordApi.getAudio(user_input) 
            try:
                if pronunciations.__len__() > 0:
                    for pron in pronunciations:
                        webbrowser.open(pron.fileUrl)
                        time.sleep(pron.duration+1)
            except:
                print "No Pronunciations found!!"
    
        except:
            print "Please enter a valid word and try again!!"
            continue

if __name__ == '__main__':
    main()
