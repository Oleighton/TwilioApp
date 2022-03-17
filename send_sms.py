# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


def send_text_message(destination: str, message:str):

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = account_sid 
    auth_token = auth_token

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_='+12242063938',
                        to=destination,
                    )

    print(message.sid)


def main():
    send_text_message('+12693860479', 'Hi, my name is TROGDOR how can I assist you today? :)')


if __name__=='__main__':
    main()
