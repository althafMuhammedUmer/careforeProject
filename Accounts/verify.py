# from django.conf import settings
from decouple import config
import os
from twilio.rest import Client


def send_otp(phone_number):
    number= '+91'+str(phone_number)
    account_sid = config('ACCOUNT_SID')
    auth_token = config("AUTH_TOKEN")
    service_id=config("SERVICES_ID")
    # account_sid = "AC7c61a6c494f664ad116383194272315a"
    # auth_token = "7cd319584e4c5cc01b134ad3b32134ff"
    # service_id= "VA6bb8fd0de0de733165d890c5e151c6d4"
    client = Client(account_sid,auth_token)
    verification = client.verify \
                        .services(service_id) \
                        .verifications \
                        .create(to=number, channel='sms')

    print(verification.sid)
    return(verification.sid)


def verify_otp(phone_number,otp):
    number= '+91'+str(phone_number)
    account_sid = config('ACCOUNT_SID')
    auth_token = config("AUTH_TOKEN")
    service_id=config("SERVICES_ID")
    # account_sid = "AC7c61a6c494f664ad116383194272315a"
    # auth_token = "7cd319584e4c5cc01b134ad3b32134ff"
    # service_id= "VA6bb8fd0de0de733165d890c5e151c6d4"
    client = Client(account_sid, auth_token)
    verification_check = client.verify \
                        .services(service_id) \
                        .verification_checks \
                        .create(to=number, code=otp)

    print(verification_check.status)
    if verification_check.status=='approved':
        print('verification confirm')
        return True
    else:
        return False