from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9690fad23b011b612a217d6449059138'
auth_token = 'ec31d0ed3ab66e23e4e7850bebbd26dc'

def sos_call(phone_number):
    client = Client(account_sid, auth_token)


    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='+15558675310',
        from_='+15017122661'
    )
    print(call.sid)
