from slackclient import SlackClient
import os

#Preparando chamada para API do SLACK
token = str(input('Insira aqui o seu TOKEN de integração com o slack: '))
slack_token = os.environ["SLACK_API_TOKEN"] = token
sc = SlackClient(slack_token)

#FUNÇÃO PARA LISTAR TODOS OS GRUPOS COM MENOS DE X USUARIOS
def lista_grupos_slack(num):
    grupos_slack = list()
    grupos_slack = sc.api_call("channels.list", )
    grupos_slack_chanels = (grupos_slack['channels'])
    for item in grupos_slack_chanels:
        if item['num_members'] < num:
            print('ID: {}, PESSOAS: {}, ARQUIVADO: {}, NOME: {},'.format(item['id'],item['num_members'],item['is_archived'],item['name']))

#FUNÇÃO PARA ARQUIVAR TODOS OS GRUPOS COM MENOS DE X USUARIOS
def arquiva_grupos_slack(num):
    grupos_slack = sc.api_call("channels.list", exclude_archived=1)
    grupos_slack_chanels = (grupos_slack['channels'])
    for item in grupos_slack_chanels:
        if item['num_members'] < num:
            print(sc.api_call("channels.archive", channel=item['id']))


#Execução do programa
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
        print('Escolha uma opção valida')