import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

from pprint import pprint as pp

from modules import General, Message


def filter_messages_by_date(message_objects, month=None, day=None, year=None):
    """
    Take in a list of messages and only get the messages that match the desired time
    """
    filtered_messages = []

    for msg in message_objects:
        date_object = datetime.fromtimestamp(msg.time_sent / 1000)
        msg_day = date_object.strftime('%A')
        msg_month = date_object.strftime('%B')
        msg_year = date_object.strftime('%Y')

        if day is not None and day != msg_day:
            continue

        if month is not None and month != msg_month:
            continue

        if year is not None and year != msg_year:
            continue

        filtered_messages.append(msg)

    return filtered_messages


def create_pie_chart(data):
    """
    Create a pie chart given some data
    data is some dictionary of strings to numbers
    """

    labels = []
    numbers = []
    for string, number in data.items():
        labels.append(string) 
        numbers.append(number) 

    plt.pie(numbers, labels=labels, autopct='%.1f%%')
    plt.show() 


def create_bar_chart(data):
    """
    Create a bar chart given a dict of data
    """
    labels = []
    numbers = []
    for string, number in data.items():
        labels.append(string)
        numbers.append(number)

    plt.bar(labels, numbers)
    # plt.title('Country Vs GDP Per Capita')
    plt.xlabel('Names')
    plt.ylabel('Messages Sent')
    plt.show()


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
    for sender, messages in name_msg_dict.items():
        print(sender)
        print(f'  Messages sent: {len(messages)}')

    print('~~~~~~~~~~~~~~~~~~~~~~~')
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    months_of_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']
    total = 0
    bar_data = {}
    for month in months_of_year:
        msgs = filter_messages_by_date(message_objects, month=month)
        num_msgs = len(msgs)
        bar_data[month[:3]] = len(msgs)
        print(f'{month}: {num_msgs} messages sent')
        total += num_msgs

    # print(total)

    # Create a pie chart that displays the total number of messages per member
    # construct the data dictionary of strings to numbers to pass in
    pie_data = {}

    for name, messages in name_msg_dict.items():
        pie_data[name] = len(messages)
    # create_pie_chart(pie_data)

    # Create a bar chart of messages sent per month
    create_bar_chart(bar_data)


    # Use the message data to create message objects
        # Get the average messages sent per day of the week (Sun - Sat)


if __name__ == '__main__':
    main()