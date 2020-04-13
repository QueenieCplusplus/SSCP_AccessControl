# Access Control (Auth)

all about who rcv msg what kept secret and intgrity of what the content the msg sent by whom with correct timestamp which ensure the limited lifetime.

by the way the auth(authentication) server can be fail point at any time.

----------------------------------------------

Acceess control defines itself as a mechanisms that govern the access to resources and the operations that being performed on those resources, which includes 

* Physical Resources

* Computer System

* Information

----------------------------------------------

The entity means who manages the access, such as 

* Systems

* Softwares

* Users

----------------------------------------------

Intrernetwork Trust Architectures

*one-way

*two-way

*transitive way 信任關係移轉

the transitive trust can be used to extend other relationship with other domains

----------------------------------------------

Auth Mechanism shall understand the internet work trust architectures and requires the federated id mgmt accross desperate systems.

* Device Auth, 包含生物辨識與智慧卡和代幣代碼

* Single/Multi-factor Auth, 多重驗證

  the 2nd auth usually uses Biometrics || Peripherial Devices.

* SSO, Single Sign On Auth using Kerberos Network Auth Protocol, 單一簽入

  Single sign-on can allow a single identify to be be shared across multiple apps, which enable users to authenticate once and gain access to multiple resources.
  
  It is both easier for user and for hacker to access many resource with only one set credential for authentication.
  
  As mentioned above, the risk of SSO exists indeed, with all of the user's credential stored on asingle auth server, when single point of failure (means the failure of the server) can prevent access for the user to all apps.
  
  When talk about DOS (Denial of Service) attacks, user can be dnied from service (to system) by haker to attack only the single point of access (which is prone). 

----------------------------------------------

Types of Authentications:

   (1) Dual Control
   
   (2) Continuous Auth
   
   (3) Periodic Auth (Session)
   
   (4) Two Factor
   
   (5) Time Out
   
   (6) Reverse Auth
   
   (7) Cert-based
   
   (8) Authorization: who can a user do auth only once.

----------------------------------------------

Type of Token Generators:

OTP, 一次性隨機密碼

   One-Time Password (Token Generator) used in mail and sms message.

Out of Band, 單一通道進行帶外管理

   this is a verification for authentication, before user log in, server request user to their password over the phone|mail. It is samilar to OTP. 
   
Peripherial Device Recognition, 機體辨識

   this is often to be used as 2nd factor auth by placing a crypto (cipher) device marker on users existing devices. (maybe ipod or memory card in smart phone), and which is required to be plugged in computer when user log in.
   
----------------------------------------------

ID Mgmt

1. Authoriztion using Policy 授權

2. Proof 驗證

3. Provision 帳號相關補充文件

4. Maintenance

5. Entitlement 保證人

   by People
   
   by Devices
   
   by Organization || Agent
   
   by Code

----------------------------------------------

Access Control Framework:

-[Ｘ] Mandatory, 強制 MAC

-[Ｘ] Discretionary, 委託 DAC

-[Ｘ] Role & Attributes, 角色屬性 RBAC

-[X] Time Based, (Temporal Isolation)

----------------------------------------------

# ACL 

to define access control list to sys can facilitate user access to data too, which also may include access to network also.


# Token Generator

公私鑰 Pub_Key

    import os

    with open(os.path.join(os.path.dirname(__file__), 'private_pwd.pem'), 'rb') as pwd:
        private_key = pwd.read()
    print(private_key)

    with open(os.path.join(os.path.dirname(__file__), 'public_pwd.pem'), 'rb') as pwd:
        public_key = pwd.read()
    print(public_key)
    

用私鑰封裝（編碼）文件

    import jwt

    token_header = {  "alg": "HS256", "typ": "JWT"} # 跟打API的封包標頭有關

    def func_name(param):
        pyload = {
                  'user_id':001122,
                  'init_date':20200413,
                  'expired_date':202021012,
                  'mapping_info' = param
                  }
        
    # 代碼符號標記等同於 使用jwt工具打包隱私訊息與私有鑰匙以及加入標頭修改的內容
    token = jwt.encode(payload, private_key, algorithm='RS256', headers=token_header)

    return token
    
用公鑰打開（解碼）文件

    def function_name(self, token):
            dec_token = jwt.decode(jwt_token, public_key, audience=self.timestamp, algorithms='RS256')

            return dec_token



