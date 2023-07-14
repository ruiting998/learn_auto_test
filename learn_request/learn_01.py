import requests
# response = requests.get("http://www.baidu.com")
# print(response.text)
proxies={
    'http':'http://127.0.0.1:80',
    'https':'https://127.0.0.1:443',
}
response = requests.get("https://www.baidu.com/",proxies=proxies,verify=False)
print(response.text)