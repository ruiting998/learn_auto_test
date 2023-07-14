import requests
class Test_API_Package_test_Login():
    def __init__(self):
        self.s = requests.Session()
    def _printResponse(self,response):
        print("\n\n====================print respinse Begin========================")
        # 响应码
        print(response.status_code)
        print("")
        for k,v in response.headers.items():
            print(f'{k}:{v}')
        print(" ")
        print(response.content.decode('utf-8'))
        print("\n\n====================print respinse End========================")

    def mrg_login(self,username,password):
        print(self.s)
        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                                 data={
                                     'username': username,
                                     'password': password
                                 })
        print("\n==========header begin==============")
        print(self.s.headers.items())
        print()
        print(self.s.cookies)
        print("\n==========header end==============")
        self.cookie = response.cookies
        self._printResponse(response)
        return response

    def customer_list(self, pagesize, pagenumber, keywords):
        print(self.s)
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
                              params={
                                  'action': 'list_customer',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        self._printResponse(response)
        return response

if __name__ == '__main__':
    t =Test_API_Package_test_Login()
    t.mrg_login("byhy","88888888")
    t.customer_list("10","1","")