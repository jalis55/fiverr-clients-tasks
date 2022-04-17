# from twilio.rest import Client 

# account_sid = 'AC6e546643d5b7fcfbc49b6525eda1b566' 

# auth_token = 'fef9d46e259a29bbfa9e1762805e1dc0' 

# import time


# with open('numbers.txt') as f:
#     numbers = f.read().splitlines()

# for iteration,number in enumerate(numbers):
#     if iteration %5 == 0:
#         time.sleep(1)

    # print(iteration,number)

# client = Client(account_sid, auth_token) 

# sms="Your sms text..."
# # for number in numbers:
# #     print(f"sending to {number}")
# #     message = client.messages.create(to=number,body=sms) 
# #     print(message.sid)

# # message = client.messages.create(to='+8801623708711',body=sms) 
# # print(message.sid)

# # importing twilio
# from twilio.rest import Client

# import logging
# logging.basicConfig(filename='sms.log', encoding='utf-8', level=logging.INFO)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = 'AC6e546643d5b7fcfbc49b6525eda1b566'
# auth_token = '3ed053dbc328d6339e09b268dacf5975' 
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="https://google.com",
#                      from_='+46726420326',
#                      to='+212643791738'
#                  )

# # logging.info(message.sid)

# print(message.sid)


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
