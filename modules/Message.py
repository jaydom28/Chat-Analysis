class Message:
    def __init__(self, sender: str, content: str, time_sent: float):
        self.sender = sender
        self.content = content
        self.time_sent = time_sent

    def __repr__(self):
        return f'{self.sender} ({self.time_sent}): {self.content}'


def create_messages_from_data(message_data):
    '''
    Take in a list of message data and return a list of message objects from the
    data
    '''
    message_objects = []
    for msg_dict in message_data['messages']:
        if not msg_dict.get('content'):
            continue

        msg_object = Message(sender=msg_dict['sender_name'],
                             content=msg_dict['content'],
                             time_sent=msg_dict['timestamp_ms']) 

        message_objects.append(msg_object)

    return message_objects


def divide_messages_by_sender(message_objects):
    '''
    Take in a list of message objects and then return a dict of names to message
    objects
    '''
    name_msg_dict = {}

    for msg in message_objects:
        name = msg.sender
        if name not in name_msg_dict:
            name_msg_dict[name] = []
        name_msg_dict[name].append(msg)

    return name_msg_dict