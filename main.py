from email import message
from modules import General, Message


def main():
    # Read the messages from a file
    data_file = 'message_data/message_1.json'

    print(f'Attempting to read data from: {data_file}')
    message_data = General.read_message_data(data_file)
    message_objects = Message.create_messages_from_data(message_data)

    # List the total number of messages
    print(f'Loaded a total of {len(message_objects)} messages')

    # List the participants and the total number of messages per participant
    name_msg_dict = Message.divide_messages_by_sender(message_objects)
    for sender in name_msg_dict:
        print(sender)
        messages = name_msg_dict[sender]
        number_messages = len(messages)
        print(f'  Messages sent: {number_messages}')


    # Use the message data to create message objects
        # Get the average messages sent per day of the week (Sun - Sat)


if __name__ == '__main__':
    main()