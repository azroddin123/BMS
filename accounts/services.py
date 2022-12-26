import jwt
from django.conf import settings


def generate_token(email) : 
    payload = {
        'email' : email
    }
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
    return token