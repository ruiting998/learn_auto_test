# py文件取名为Test_xxx.py
import pytest
class Test_login:
    #这里是标签测试
    @pytest.mark.webtest
    def test_C001001(self):
        print("\n用例C001001")
        # 断言验证
        assert 1==1
    @pytest.mark.网页测试
    def test_C001002(self):
        print("\n用例C001002")
        assert 2==2
    def test_C001003(self):
        print("\n用例C001002")
        assert 2==3

if __name__ == '__main__':
    pytest.main(["-s","test_login.py"])