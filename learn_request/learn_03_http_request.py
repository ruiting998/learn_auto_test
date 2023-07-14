import requests
# 构建请求头
headers = {
    'user-agent': 'my-app/0.0.1',
    'auth-type': 'jwt-token'
}
payload = {
    'key1':'value1',
    'key2':'value2'
}
# 检查响应消息头
import requests,pprint
response=requests.get("http://www.baidu.com/")
print(type(response.headers))
pprint.pprint(dict(response.headers))
print(response.headers['Content-Type'])
print(response.content)
print(response.content)
print(response.content.decode('utf8'))
import requests,json
response = response.p
