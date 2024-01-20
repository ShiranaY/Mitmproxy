from mitmproxy import http
from mitmproxy.http import Request


# 运行命令: mitmdump -q -p 8888 -s v1.py

def request(flow):
    print("---------------------------------------------------------------------------------------------------------")
    print("请求-->", flow.request.url)
    print("host-->", flow.request.host)
    print("path-->", flow.request.path)
    print("query-->", flow.request.query)
    print("cookies-->", flow.request.cookies)
    print("headers-->", flow.request.headers)
    print("method-->", flow.request.method)
    print("content-->", flow.request.content)


def response(flow: http.HTTPFlow):
    pass
