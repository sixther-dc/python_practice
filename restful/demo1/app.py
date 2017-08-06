# -*-coding:utf-8-*-

"""
这里需要添加文件注释
"""
from webob import Response
from webob import Request
from webob.dec import wsgify
from webob import exc

class Hello(object):

    @wsgify(RequestClass=Request)
    def __call__(self, request):
        return Response('Hello, Secret World of WebOb !\n')

def app_factory(global_config, **local_config):
    return Hello()
