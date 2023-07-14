import json

import pytest
import requests


@pytest.fixture()
def create_post(request_p):
    my_data={
        "url": "http://127.0.0.1/api/mgr/signin",
        "user_data":{
            'username':request_p.param[0],
            'password':request_p.param[1],
        },
        "header":{
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }
    return my_data

@pytest.fixture()
def create_get(request_p):
    my_data={
        'url' : "http://127.0.0.1/api/mgr/customers",
        "params":{
            "action":request_p.param
        },
        "header":{
            "Content-Type": "application/json"
        }
    }
    return my_data

@pytest.mark.parametrize("create_post",
                         [("byhy","88888888")],
                         indirect=True,
                         )
def test_API001(create_post):
    s = requests.Session()
    response = s.post(url=create_post["url"], data=create_post["user_data"], headers=create_post["header"]);
    assert response.json()["ret"]==0

@pytest.mark.parametrize("create_get",
                         [("list_customer")],
                         indirect=True,
                         )
def test_API002(create_get):
    response = requests.get(url=create_get["url"], params=create_get["params"], headers=create_get["header"]);
    assert  response.json()["ret"]==0


