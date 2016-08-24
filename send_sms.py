'''
This program sends a user entered message as an sms to the requested phone number.
This can be configured with a cron job to alert the user about any specific event
'''

from twilio.rest import TwilioRestClient
import sys

try:
    message1 = sys.argv[1]
except:
    print "Please execute script with message to be sent : Eg: python send_sms.py <sms text>"
    sys.exit()

# Find these values at https://twilio.com
account_sid = "**********"
auth_token = "************************"
client = TwilioRestClient(account_sid, auth_token)

#Enter sender and receiver phone numbers in the from and to fields
message = client.messages.create(to="*******", from_="*********",
                                     body=message1)
