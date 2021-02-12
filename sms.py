
import clx.xms
import requests

def sendSMS(number1,number2,name):
    client = clx.xms.Client(service_plan_id='ba94aad89039417c9fcd303555432171', token='12c806b724f64fa78552b0c84b4ff009')

    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = '447537404817'
    create.recipients = {'91'+number1,'91'+number2}
    create.body = 'HELP!!!!!!! '+name+' is in an emergency and needs your help.'

    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
        clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))



