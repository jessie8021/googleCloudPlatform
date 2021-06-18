from google.cloud import pubsub_v1

project_id = 'velvety-argon-309103'
topic_name = 'test_topic'

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/velvety-argon-309103/topics/test-topic'.format(
    project_id = project_id,
    topic = topic_name
)

for i in range(10):
    msg = '{index}-Hello World'.format(index=i).encode('utf-8')

    publisher.publish(topic=topic_path, data=msg)