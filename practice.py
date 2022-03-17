from flask import Flask,request
from twilio.twiml.messaging_response import Message, MessagingResponse


app = Flask(__name__)

@app.route('/sms', methods=['POST'])

def sms_reply():
    number = request.form['From']
    # changed this from message_body = request.form['Body'] and added 'GET' above
    message_body = request.form['Body']
     
    resp = MessagingResponse()

    my_dict = {
        'Tell me a joke': 'Creating meaning in a meaningless world.',
        'Who are you': 'I am a chat bot 🤖 '
    }


    if message_body == 'Tell me a joke':
        resp.message(my_dict.get('Tell me a joke'))
    elif message_body == 'Who are you':
        resp.message(my_dict.get('Who are you'))


    return str(resp)

if __name__=='__main__':
    app.run(debug=True)
