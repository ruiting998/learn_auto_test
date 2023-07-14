import pytest
from Hello_world.lib.webui import loginAndCheck
class Test_error_login:
    def test_UI_0001(self):
        alertText =  loginAndCheck(None,'88888888')
        assert alertText =='请输入用户名'
    def test_UI_0002(self):
        alertText =  loginAndCheck('byhe',None)
        assert alertText =='请输入密码'
    def test_UI_0003(self):
        alertText = loginAndCheck('byhe', "88888888")
        assert alertText == '登录失败 : 用户名或者密码错误'