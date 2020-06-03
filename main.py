import jwt


# Defaults
decoded_jwt = ''
encoded_jwt = ''
error2 = {'error': 2}
secret = 'acelera'
word_dict = {'language': 'Python'}


def create_token(data, secret):
    """
    This function does the JSON Web Token (JWT)
    """
    encoded_jwt = jwt.encode(word_dict, secret, algorithm='HS256')
    return encoded_jwt


def verify_signature(token):
    """
    This function checks the secret
    """
    try:
        decoded_jwt = jwt.decode(token, secret, algorithm='HS256')
        return decoded_jwt
    except:
        return error2
