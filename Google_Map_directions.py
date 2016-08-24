'''
Accessing Google APIs to access map related information.

1. Print Distance between source and destination.
2. Print Step by Step instructions to reach the destination from source.

'''

import sys,re,subprocess
import googlemaps as GoogleMaps

def main():

    try:
        source = str(raw_input('Please enter the name of source: '))
        destination = str(raw_input('Please enter the name of destination: '))
        mapService = GoogleMaps.Client('*******************')
        directions = mapService.directions(source, destination)

        #Prints distance between source and destination
        print "\n\n Distance between %s and %s is : " %(source, destination) + str(directions[0]['legs'][0]['distance']['text']) + "\n\n"

        #Print instructions by step to reach from source to destination
        counter = 0
        for step in directions[0]['legs'][0]['steps']:
            counter = counter + 1
            print re.sub('<[^<]+?>', '', str(counter) + '. ' + step['html_instructions'])
     
    except:
        print "Unexpected issue encountered. Please check if the places have been spelt right!"
    
if __name__ == '__main__':
    main()

