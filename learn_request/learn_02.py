# request 请求
# https://www.baidu.com/s?wd=iphone&rsv_spt=1
import ssl
import  requests
# urlpara = {
#     'wd':'iphone&ipad',
#     'rsv_spt':'1'
# }
#
# # 请求查询内容为iphone和ipad
#
# resbonse=requests.get("https://www.baidu.com/s",params=urlpara)
# print(resbonse.text)

# post请求
print("==============================POST===========================================")
headers ={
    'user-agent':'my-app/0.0.1',
    'auth-type':'jwt-token'
}
r = requests.post("http://httpbin.org/post",headers=headers)
print(r.text)





