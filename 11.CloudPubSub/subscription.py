from google.cloud import pubsub_v1

project_id = 'velvety-argon-309103'
topic_name = 'test_topic'
subscription_id = 'test_subscription'

subscriber = pubsub_v1.SubscriberClient()

topic_path = 'projects/velvety-argon-309103/topics/test-topic'.format(
    project_id = project_id,
    topic = topic_name
)

subcription_path = 'projects/velvety-argon-309103/subscriptions/test_subscription'.format(
    project_id = project_id,
    subscription_id = subscription_id
)

def callback(message):
    print(message.data)
    message.ack()


subscribe = subscriber.subscribe(subcription_path, callback)


try:
    subscribe.result()
except Exception as e:
    subscribe.cancel()