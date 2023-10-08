import plivo 
def sendSMS(message,to_Number,from_Number):
    client = plivo.RestClient('<auth_id>','<auth_token>')
    response = client.messages.create(
        src=from_Number,
        dst=to_Number,
        text=message,
        # url='https://<yourdomain>.com/sms_status/',
    )
    print(response)
    #prints only the message_uuid
    print(response.message_uuid)
