from flask import Flask,request
from twilio.twiml.messaging_response import Message, MessagingResponse
from .models import Survey, Question
import json

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])

def sms_reply():
    number = request.form['From']
    # changed this from message_body = request.form['Body'] and added 'GET' above
    message_body = request.form['Body']
     
    resp = MessagingResponse()

    my_dict = {
        'STOP': 'You have been removed from the mailing list',
        'Hello': 'Hi, my name is TROGDOR how can I assist you today? :)',
        'Tell me a joke': 'Creating meaning in a meaningless world.',
        'Who are you': 'I am a chat bot 🤖 ',
    }

    if message_body == 'STOP':
        resp.message('You have been removed from the mailing list.')
    elif message_body == 'Hello':
        resp.message(my_dict.get('Hello'))
    elif message_body == 'Tell me a joke':
        resp.message(my_dict.get('Tell me a joke'))
    elif message_body == 'Who are you':
        resp.message(my_dict.get('Who are you'))


    return str(resp)

if __name__=='__main__':
    app.run(debug=True)
