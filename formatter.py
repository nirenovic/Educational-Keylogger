import sys
from pynput.keyboard import Key

class Formatter(object):
    def __init__(self):
        pass

    def format(self, text):
        output_data = ""
        # remove unwanted characters, translate special Key types
        for line in text:
            line = line.replace('\n', '')
            line = line.replace('\'', '')
            output_data += line
        return output_data
