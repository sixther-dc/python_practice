from kombu import Connection, Producer, Exchange, Queue

with Connection('amqp://guest:guest@10.0.0.3:5672//') as conn:
    producer = conn.Producer()

task_queue = Queue('tasks', Exchange('tasks'), routing_key='tasks')
test_queue = Queue('tests', Exchange('tasks'), routing_key='tests')

producer.publish(
    {'hello': 'world'},
    retry=True,
    exchange=task_queue.exchange,
    routing_key=task_queue.routing_key,
    declare=[task_queue],
)

producer.publish(
    {'hello': 'world'},
    retry=True,
    exchange=task_queue.exchange,
    routing_key='tests',
    declare=[test_queue]
)