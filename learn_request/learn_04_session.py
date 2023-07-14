import requests
# 封装相应
def print_response(response):
    print("---------------------------HTTP response * begin---------------------------------------")
    # 输出响应状态码 202 201 404
    print(response.status_code)
    for k,v in response.headers.items():
        print(f'{k}:{v}\n')
    print(" ")
    print(response.content.decode("utf8"))
    print("---------------------------HTTP response * end  ----------------------------------------\n\n")

# 创建session
s = requests.Session()
reponse = s.post("http://127.0.0.1/api/mgr/signin",
                 data={
                      'username': 'byhy',
                      'password': '88888888'
                 })
print_response(reponse)
response = s.get("http://127.0.0.1/api/mgr/customers",
                 params={
                    'action'    :  'list_customer',
                    'pagesize'  :  10,
                    'pagenum'   :  1,
                    'keywords'  :  '',
                 })
print_response(response)