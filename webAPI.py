from slackclient import SlackClient

import os

slack_token = os.environ["SLACK_API_TOKEN"] = "YOUR TOKEN"
sc = SlackClient(slack_token)

grupos_slack = list()

grupos_slack = sc.api_call("channels.list", )
grupos_slack_chanels = (grupos_slack['channels'])
for item in grupos_slack_chanels:
    if item['num_members'] < 2:
        print('ID: {}, PESSOAS: {}, ARQUIVADO: {}, NOME: {},'.format(item['id'],item['num_members'],item['is_archived'],item['name']))

#int(grupos_slack['channels'])
#for grupo in gruposels_slack:
#    print(grupo)