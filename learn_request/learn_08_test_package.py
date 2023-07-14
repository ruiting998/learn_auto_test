from lib.webapi import Test_API_Package_test_Login

if __name__ == '__main__':
    api_test = Test_API_Package_test_Login()
    request1 = api_test.mrg_login("byhy","88888888")
    request2 = api_test.customer_list("10","1","")