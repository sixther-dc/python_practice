# -*-coding:utf-8-*-
"""
rabbitmq生产者
"""
import datetime
from kombu import Connection

with Connection('amqp://guest:guest@10.0.0.3:5672//') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')
    message = 'helloworld, sent at {0}'.format(datetime.datetime.today())
    simple_queue.put(message)
    print('Sent: {0}'.format(message))
    simple_queue.close()

