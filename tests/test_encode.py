import sqlite3
from rosbags.serde import deserialize_cdr


def get_messages(file: str):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    query = """
       SELECT topics.id, topics.name, topics.type, messages.timestamp, messages.data
       FROM messages JOIN topics ON messages.topic_id=topics.id
       LIMIT 5
    """
    cursor.execute(query)

    for topic_id, topic_name, topic_type, timestamp, data in cursor:
        yield topic_id, topic_name, topic_type, timestamp, data


for topic_id, topic_name, topic_type, timestamp, data in get_messages(
    "/Users/miles/dl/sample_rosbag2.db3"
):
    msg = deserialize_cdr(data, topic_type)
    print(msg.header.frame_id)
    print(msg.header)
