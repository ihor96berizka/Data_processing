import requests

payload = {'device': 'Il/C', 'startDate': '2019-09-29', 'endDate': '2019-10-1', 'properties': 'depth'}
response = requests.get("https://yz58i1wove.execute-api.eu-west-1.amazonaws.com"
                 "/dev/data/group-by/minute", params=payload)

print('response info')
print(response.url)
print(response.status_code)
print(response.json())