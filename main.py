from urllib import response
import requests
import time
import json
from datetime import datetime

ZABBIX_SERVER = 'https://monitor.mooseninja.co.uk/zabbix/api_jsonrpc.php'
user = 'cstafford'
password = 'H302xsp1!'
zapiauth = requests.post(ZABBIX_SERVER,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.login",
                      "params": {
                          "user": user,
                          "password": password},
                      "id": 1
                  })

AUTHTOKEN = zapiauth.json()["result"]

zapihosts = requests.get(ZABBIX_SERVER,
                  json={
                      "jsonrpc": "2.0",
                      "method": "host.get",
                      "params" : {
                      },
                      "auth": AUTHTOKEN,
                      "id": 1
                  })
zapihosts = json.loads(zapihosts.text)
zapihosts = zapihosts['result']
for host in zapihosts:
    if host['host'] == 'Home Router':
        hostid = host['hostid']

zapigraphs = requests.get(ZABBIX_SERVER,
                  json={
                      "jsonrpc": "2.0",
                      "method": "graph.get",
                      "params" : {
                            "output": "extend",
                            "hostids": hostid,
                            "sortfield": "name"
                      },
                      "auth": AUTHTOKEN,
                      "id": 1
                  })

zapigraphs = json.loads(zapigraphs.text)
zapigraphs = zapigraphs['result']
for graph in zapigraphs:
    print(graph['name'] + ' | ' + graph['graphid'])

# for host in zapihosts.content:
#     print(host)
    

# def api_authetication(user,password,url):
#     headers = {
#         "jsonrpc": "2.0",
#         "method": "user.login",
#         "params": {
#             "user": user,
#             "password": password
#         },
#         "id": 1,
#         #"auth": null
#     }
#     response_api = requests.get(url,data=headers)




# def main():
#     auth_reponse = api_authetication('api_user','H302xsp1!','https://monitor.mooseninja.co.uk/zabbix/api_jsonrcp.php,api_user')
#     print(auth_reponse)

# if __name__ == "__main__":
#     main()