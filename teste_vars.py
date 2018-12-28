from os import getenv
from time import sleep

print(f'A url do wso2 é : {getenv("WSO2_APIMANAGER_URL")}\nO token está sendo gerado. pela url {getenv("AUTHENTICATION_CONFIG_LOGIN_URL")}\nvalor generico informado .env "{getenv("TESTE")}"')
