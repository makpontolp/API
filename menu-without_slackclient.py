from slackclient import SlackClient
import os
import requests
import json


#Preparando chamada para API do SLACK
token = str(input('Insira aqui o seu TOKEN de integracao com o slack: '))  # type: str
#slack_token = os.environ["SLACK_API_TOKEN"] = token
#sc = SlackClient(slack_token)
r = requests
#data = {'token': token,
#        'excluded_archived': 'true'}
#
##FUNcaO PARA LISTAR TODOS OS GRUPOS COM MENOS DE X USUARIOS
#def lista_grupos_slack(num):
#    grupos_slack = list()
#    grupos_slack = sc.api_call("channels.list", )
#    grupos_slack_chanels = (grupos_slack['channels'])
#    for item in grupos_slack_chanels:
#        if item['num_members'] < num:
#            print('ID: {}, PESSOAS: {}, ARQUIVADO: {}, NOME: {},'.format(item['id'],item['num_members'],item['is_archived'],item['name']))
#
def lista_grupos_slack(num):
        grupos_slack = list()
        data = {'token': token,
                'excluded_archived': 'true'}
        grupos_slack = (r.get('https://slack.com/api/channels.list', params=data).json())
        grupos_slack_channels = grupos_slack['channels']
        for item in grupos_slack_channels:
                if item['num_members'] < num:
                        print('ID: {}, PESSOAS: {}, ARQUIVADO: {}, NOME: {},'.format(item['id'], item['num_members'], item['is_archived'], item['name']))


##FUNcaO PARA ARQUIVAR TODOS OS GRUPOS COM MENOS DE X USUARIOS
#def arquiva_grupos_slack(num):
#    grupos_slack = sc.api_call("channels.list", exclude_archived=1)
#    grupos_slack_chanels = (grupos_slack['channels'])
#    for item in grupos_slack_chanels:
#        if item['num_members'] < num:
#            print(sc.api_call("channels.archive", channel=item['id']))
def arquiva_grupos_slack(num):
        data = {'token': token,
                'excluded_archived': 'true'}
        grupos_slack = (r.get('https://slack.com/api/channels.list', params=data).json())
        grupos_slack_channels = grupos_slack['channels']
        for item in grupos_slack_channels:
            if item['num_members'] < num:
                data = {'token': token,
                        'excluded_archived': 'true',
                        'channel': item['id']}
                print(r.post('https://slack.com/api/channels.archive', data=data))
#
##Execucao do programa
while True:
    opcao = int(input('='*50+'\nO que deseja fazer?\n0 - Encerrar\n1 - Arquivar Grupos\n2 - Listar Grupos \n'))
    if opcao == 1:
        num = int(input('Deseja listar Canais com no maximo quantos participantes?: '))
        arquiva_grupos_slack(num)
    if opcao == 2:
        num = int(input('Deseja listar Canais com no maximo quantos participantes?: '))
        lista_grupos_slack(num)
    if opcao == 0:
        break
    else:
        print('Escolha uma opcao valida')



#r = requests
#retorno = (r.get('https://slack.com/api/channels.list', params=data).json())
#channels = retorno['channels']
#for item in range (0,len(channels)):
#        print(channels[item])
