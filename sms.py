
import clx.xms
import requests

def sendSMS(number1,number2,name):
    client = clx.xms.Client(service_plan_id=', token='')

    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = ''
    create.recipients = {'91'+number1,'91'+number2}
    create.body = 'HELP!!!!!!! '+name+' is in an emergency and needs your help.'

    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
        clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))



