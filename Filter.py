from slackclient import SlackClient

import os

slack_token = os.environ["SLACK_API_TOKEN"] = "YOUR_TOKEN"
sc = SlackClient(slack_token)

grupos_slack = list()

grupos_slack = sc.api_call("channels.list", exclude_archived=1)
grupos_slack_chanels = (grupos_slack['channels'])
for item in grupos_slack_chanels:
    if item['num_members'] < 2:

        print(sc.api_call("channels.archive",channel=item['id']))

