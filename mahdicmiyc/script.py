from twilio.rest import Client
import logging
import time
logging.basicConfig(filename='sms.log', encoding='utf-8', level=logging.INFO)

account_sid = 'AC6e546643d5b7fcfbc49b6525eda1b566'
auth_token = '3ed053dbc328d6339e09b268dacf5975' 

client = Client(account_sid, auth_token)

with open('numbers.txt') as f:
    numbers = f.read().splitlines()

for iteration,number in enumerate(numbers) :
    if (iteration+1) % 5 == 0:
        time.sleep(1)
    message = client.messages \
                .create(
                     body="https://google.com",
                     from_='+46726420326',
                     to=number
                 )
