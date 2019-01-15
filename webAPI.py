import os
from slackclient import SlackClient

slack_token = os.environ["ZZZZZZ"]
sc = SlackClient(slack_token)

sc.api_call(
  "channels.info",
  channel="ZZZZZZZZZZZz",
  name="thumbsup",
  timestamp="1234567890.123456",

)