#!/usr/bin/env python3
from datetime import date, datetime
from absl import app
from absl import flags
import logging

from email_process import EmailInfo
from register import insert_historic_balance
import trx_process

FLAGS = flags.FLAGS
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)

# If there is a conflict, we'll get an error at import time.
flags.DEFINE_string('csv_path', None, 'CSV trx file path')
flags.DEFINE_string('sender_email', None, 'Sender email')
flags.DEFINE_string('email_pwd', None, 'Email password')
flags.DEFINE_string('dest_email', None, 'Destination email')
flags.DEFINE_string('user_name', "Testing User", 'User name')
flags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'Job status.')

def check_flags():
    """Check if we have all params to run
    """
    if FLAGS.csv_path is None:
        logging.error("No file path defined")
        return -1
    if FLAGS.sender_email is None:
        logging.error("No sender email defined")
        return -1
    if FLAGS.email_pwd is None:
        logging.error("No sender email password defined")
        return -1
    if FLAGS.dest_email is None:
        logging.error("No destination email defined")
        return -1
    return 0

def main(argv):
    if check_flags() != 0:
        return -1
    
    account_info={'user_name':FLAGS.user_name}
    transactions = trx_process.get_monthly_info(FLAGS.csv_path)
    if transactions == -1:
        return -1

    account_info.update(transactions)
    emailInfo = EmailInfo(account_info, FLAGS.sender_email,
    FLAGS.email_pwd,FLAGS.user_name, FLAGS.dest_email)

    if emailInfo.create_email_content() == -1:
        return -1
    
    account_info['email_date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if insert_historic_balance(account_info) == None:
        logging.error("Email information couldn't be saved")
        return -1
    
if __name__ == '__main__':
  app.run(main)
