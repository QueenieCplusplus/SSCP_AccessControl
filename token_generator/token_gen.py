# -*- coding: utf-8 -*-
# https://jwt.io
import jwt, os
import json
from datetime import datetime, timedelta
import requests
# import uuid

with open(os.path.join(os.path.dirname(__file__), 'private_pwd.pem'), 'rb') as pwd:
    private_key = pwd.read()
print(private_key)

# PEM 代表隱私權增強式郵件。 
# PEM 格式通常用於代表憑證、憑證要求、憑證鏈和金鑰。 
# PEM 格式檔案的一般副檔名為 .pem ，但這不是必要副檔名

with open(os.path.join(os.path.dirname(__file__), 'public_pwd.pem'), 'rb') as pwd:
    public_key = pwd.read()
print(public_key)

token_header = {  "alg": "HS256", "typ": "JWT"}

class token_gen_api():

    def __init__(self):
        self.url = "https://vivy.com.tw"
        self.timestamp = str(datetime.now())

    def token_gen(self, id='vivy', apply_date="1090413"):
        now = datetime.utcnow()
        payload = { 
                    "userId": "vivy", #使用者帳號
                    "timestamp"   : self.timestamp, #查詢時間
                    "initial"   : now - timedelta(seconds=100), #token 發行時間, millisecond 格式
                    "expire"   : now + timedelta(seconds=500), #token 有效時間, millisecond 格式
                    # "uuid"   : str(uuid.uuid4()), 
                    "sub": " ",
                    "name": " Vivy Chen",
                    "iat": 998877663,
                    "conditionMap"  : json.dumps({  "userAccountId" : "{:6}".format(id), #被查驗者帳號，6 碼
                                                    "applyYyyＭmＤd" : "{:7}".format(apply_date), #異動帳號日期，民國格式7 碼 idMarkDate
                                                    }),
                    }
        token = jwt.encode(payload, private_key, algorithm='RS256', headers=token_header)

        return token

    def token_decode(self, jwt_token):
        dec_token = jwt.decode(jwt_token, public_key, audience=self.timestamp, algorithms='RS256')
        
        return dec_token

    def send_token(self, token):
        headers = { "charset": "UTF-8",
                    "Authorization": " " + token.decode(),
                    "Content-Encoding" : "UTF-8",
                    "Accept-Encoding" : "UTF-8",
                    "Accept" : "application/json"
                    }

        resp = requests.get(self.url, headers=token_headers)

        if resp.status_code==200:
            return True, resp.json()
        else:
            return False, resp.json()


if __name__ == '__main__':

    token_gen_agent = token_gen_api()
    token = token_gen_agent.token_gen()
    print(token)

    # decoded_content = token_gen_agent.token_decode(token)
    # print(decoded_content)

    response_status, json_string = token_gen_agent.send_token(token)
    print(response_status, json_string)
    
# pip install oauthlib==0.7.2
    
