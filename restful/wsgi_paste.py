# -*-coding:utf-8-*-

"""
test     
"""

import os
import sys
from webob import Response
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp

init_path = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, 'api-paste.ini'))

#wsgify修饰器的作用是将一个函数转换为一个WSGI应用
@wsgify
def application(request):
    """
    定义处理HTTP请求的函数
    """
    return Response('Hello, World of WebOb! \n')

def app_factory(golbal_config, **local_config):
    """
    定义工厂函数
    """
    return application

if not os.path.isfile(init_path):
    print('Can not find api-paste.ini. \n')
    exit(1)

wsgi_app = loadapp('config:%s' % init_path)

httpserver.serve(wsgi_app, host='127.0.0.1', port=8800)
    