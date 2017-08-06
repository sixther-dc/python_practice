# -*-coding:utf-8-*-

"""
这里需要添加文件注释
"""

from webob.dec import wsgify
from webob import Request
import routes
import routes.middleware
import controllers

class Router(object):
    def __init__(self):
        self.mapper = routes.Mapper()
        self.add_routes()
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)

    def add_routes(self):
        controller = controllers.Controller()
        self.mapper.connect('/instances',
                        controller=controller,
                        action='create',
                        conditions=dict(method=['POST']))
        self.mapper.connect('/instances',
                        controller=controller,
                        action='index',
                        conditions=dict(method=['GET']))
        self.mapper.connect('/instances/{instance_id}',
                        controller=controller,
                        action='update',
                        conditions=dict(method=['PUT']))
        self.mapper.connect('/instances/{instance_id}',
                        controller=controller,
                        action='delete',
                        conditions=dict(method=['DELETE']))                

    @wsgify(RequestClass=Request)
    def __call__(self, request):
        return self._router

    @staticmethod
    @wsgify(RequestClass=Request)
    def _dispatch(request):
        """
        根据routes.middleware.RoutesMiddleware的mapper参数，决定要disatch哪个controller的哪个action来执行操作
        request.environ记录了http请求的详细信息,wsgiorg.routing_args包含了url的参数，
        url映射的controller对象, 数据格式为
          {
            'action': u'index',
            'controller': <controllers.Controllerobjectat0x10608bc90>
          }
        """
        match = request.environ['wsgiorg.routing_args'][1]
        if not match:
            return _err() 
        app = match['controller']
        return app

def _err():
    return "The Resource is Not Found. \n"  

def app_factory(global_config, **local_config):
    return Router()
