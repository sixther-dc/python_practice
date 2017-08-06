# -*-coding:utf-8-*-

"""
这里需要添加文件注释
"""

from webob import Response
from webob.dec import wsgify
from webob import exc
import webob

class Auth(object):

    def __init__(self, app):
        self.app = app

    @classmethod
    def factory(cls, global_config, **local_config):
        def _factory(app):
            return cls(app)
            #这里等于执行了Auth(app), app为下执行paste.deploy的下一个app,也就是执行了
            #__call__方法
        return _factory
    #自定义req的修饰类，req的执行交给了webob包        
    @wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        resp = self.process_request(req)
        if resp:
            return resp
        return req.get_response(self.app)

    def process_request(self, req):
        if req.headers.get('X-Auth-Token') != 'open-sesame':
            return exc.HTTPForbidden()