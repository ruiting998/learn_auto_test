import requests
def pretty_print_request(req):
    if req.body == None:
        msgBody=""
    else:
        msgBody=req.body
    print(
        '{}\n{}\n{}\n\n{}'.format(
            '\n\n--------------------------发送请求------------------------',
            req.method+" "+req.url,
            '\n'.join('{}:{}'.format(k,v)for k,v in req.headers.items()),
            msgBody,
        )
    )

def pretty_print_response(res):
    print(
        '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
        '\n\n----------- 得到响应 -----------',
        res.status_code,
        '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
        res.text,
    ))

req = requests.Request(
    'post',
    'http://www.baidu.com',
    headers={
        'head1':'value1',
        'head2':'value2',
    },
    data={
        'item1':'body-value1',
        'item2':'body-value2',
    })

session = requests.Session()
prepared = session.prepare_request(req)
pretty_print_request(prepared)
r = session.send(prepared)
pretty_print_response(r)
