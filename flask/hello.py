"""
test
"""
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    test
    """
    return "Hello,World"

@app.route('/user/<username>')
def hello_user(username):
    """
    test for URL contain variable
    """
    return "Hello, %s" % username

@app.route('/user/<int:user_id>')
def get_user(user_id):
    """
    test for variable in URL is specific type
    """
    return "This is %d" % user_id
