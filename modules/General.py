'''
This module contains general use functions so that our code isn't too messy.
'''
import json


def read_message_data(file_path: str):
    '''
    Take in a string representing a file path to a file containing JSON message
    data and returns a list of dicts representing messages
    '''
    with open(file_path, 'r') as handle:
        message_data = json.load(handle)

    return message_data