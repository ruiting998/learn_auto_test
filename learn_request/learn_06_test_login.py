import requests
import time
# 测试 登录接口
# 构造数据头
header = {
    "Content-Type":"application/x-www-form-urlencoded"
}
data={
    "username":"byhy",
    "password":"88888888"
}

login_url = "http://127.0.0.1/api/mgr/signin"
# 生成会话
s = requests.Session()
response = s.post(url=login_url,data=data,headers=header);
print(response.text)


# 测试 列出列表
header = {
    "Content-Type":"application/json"
}
params ={
    "action":"list_customer",
    'pagesize'  :  10,
    'pagenum'   :  1,
    'keywords'  :  '',
}
list_constmer_url = "http://127.0.0.1/api/mgr/customers"
# 这里如果没有登录cookie ，就会登录权限受限
response2 = s.get(list_constmer_url,params=params)
print(response2.text)


