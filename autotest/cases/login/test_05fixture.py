import pytest
@pytest.fixture
def createzhangSan():
    print("create zhangsan")
    zhangSan={
        "username":"zhangsan",
        "password":"111111",
    }
    # return zhangSan
    yield zhangSan
#根据参数变化的user
@pytest.fixture()
def createUser(request):
    print("\n*** createUser ***")
    user = {
        'username':request.param[0],
        'password':request.param[1]
    }
    yield user
@pytest.mark.parametrize("createUser",
                         [("lisi",'111')],
                         indirect=True
                         )
def test_A001002(createUser):
    print('\n 用例 A001002')
    print('\n password is', createUser['password'])
# 这里测试张三账号登录的功能
def test_A001001(createzhangSan):
    print('\n 用例 A001001')
    print('\n password is', createzhangSan['password'])