from os import getenv
from time import sleep

wso2 = getenv('WSO2_APIMANAGER_URL')
get_token = getenv('AUTHENTICATION_CONFIG_LOGIN_URL')
teste = getenv('TESTE')

if wso2 != None and get_token != None and teste != None:
    while True:
        print(f'A url do wso2 é : {wso2}\nO token está sendo gerado. pela url {get_token}, valor generico informado .env "{teste}"')
        sleep(30)
else:
    print('Os valores não informados!')
