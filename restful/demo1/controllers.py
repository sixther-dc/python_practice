# -*-coding:utf-8-*-

"""
这里需要添加文件注释
"""

import uuid
import simplejson
from webob.dec import wsgify
from webob import Request, Response

class Controller(object):
    def __init__(self):
        self.instances = {}
        for i in xrange(3):
            inst_id = str(uuid.uuid4())
            self.instances[i] = {
                'id': inst_id,
                'name': 'inst_' + inst_id 
            }

    def create(self, req):
        print(req.params)
        name = req.params['name']
        if name:
            inst_id = str(uuid.uuid4())
            inst = {'id': inst_id, 
                    'name': name}
        
            self.instances[inst_id] = inst
            return {'instance': inst}

    def show(self, req, instance_id):
        inst = self.instances.get(instance_id)
        return {'instance': inst}        

    def index(self, req):
        return {'instances': self.instances.values()}

    def delete(self, req, instance_id):
        if self.instances.get(instance_id):
            self.instances.pop(instance_id)

    def update(self, req, instance_id):
        inst = self.instances.get(instance_id)
        name = req.params['name']
        if inst and name:
            inst['name'] = name
            return {'instance': inst}

    @wsgify(RequestClass=Request)
    def __call__(self, req):
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        action = arg_dict.pop('action')
        del arg_dict['controller']

        method = getattr(self, action)
        result = method(req, **arg_dict)
        
        if result is None:
            return Response(body='',
                            status='204 Not Found',
                            headerlist=[('Content-Type',
                                        'application/json')])
        else:
            if not isinstance(result, basestring):
                result = simplejson.dumps(result)
            return result