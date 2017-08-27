from kombu import Connection, Consumer, Queue, Exchange

connection = Connection('amqp://guest:guest@10.0.0.3:5672//')
channel = connection.channel()

queue = Queue('tasks')
with Consumer(connection, queue, accept=['json']):
    connection.drain_events(timeout=1)
