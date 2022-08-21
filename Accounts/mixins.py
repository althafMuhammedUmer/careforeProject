from django.conf import settings
from twilio.rest import Client  




class massHandler:
    
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp
        
    def send_otp_on_phone(self):
        account_sid = 'AC7c61a6c494f664ad116383194272315a' 
        auth_token = '[AuthToken]' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(
                                    body = f'Your OTP is {self.otp}'
                                    from = '+19809828708'
                                        
                                         
                                    to='+916282595046' 
                                ) 
        
        print(message.sid)
        