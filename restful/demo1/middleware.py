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
    def factoryy(cls, global_config, **local_config):
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
        print(dir(self.app))
        return req.get_response(self.app)

    def process_request(self, req):
        if req.headers.get('X-Auth-Token') != 'open-sesame':
            return exc.HTTPForbidden()

"""
这个函数的作用跟在Auth类里面使用classmethod的作用是一样的，使用classmethod更有利于函数的聚合
这里的app应该就是pipeline的下一个app(配置文件中定义的)
"""
def factory(global_config, **local_config):
    def _factory(app):
        return Auth(app)
    return _factory       