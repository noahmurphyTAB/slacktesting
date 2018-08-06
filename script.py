import requests

url = "https://hooks.slack.com/services/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"
with open('message.json') as file:
    payload = file.read()

headers = {"Content-type": "application/json"}

r = requests.post(url, data = '{}'.format(payload), headers = headers)
