"""
date:       2018-08-02
comment:    test for paste.deploy
"""
# -*- coding:utf-8 -*-
from paste import httpserver

def application(environ, start_response):
    """
    test
    """
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['Hello World\n']

httpserver.serve(application, host='127.0.0.1', port=8800)
