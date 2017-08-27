# -*-coding:utf-8-*-
import sys
sys.path.append('..')  
                 
from lib.log import logging,sys

class Dict(dict):
    #这里的dict是pyton的内建class, super之后Dict就具备了dict的能力
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, vaule):
        self[key] = vaule

if __name__ == '__main__':
    logging.info((len(dir(dict))))
    logging.info((len(dir(Dict))))
    logging.debug(sys.path)