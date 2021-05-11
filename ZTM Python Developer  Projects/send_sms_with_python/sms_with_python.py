
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid ='your account_sid'
auth_token = 'your auth_token'
# best practice
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+ add number",
    from_="+ add number",
    body="Your message")
    
print(message.sid)
