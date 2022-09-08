#!/usr/bin/env python3
from absl import app
from absl import flags

from email_process import EmailInfo
import trx_process

FLAGS = flags.FLAGS

# If there is a conflict, we'll get an error at import time.
flags.DEFINE_string('csv_path', None, 'CSV trx file path')
flags.DEFINE_string('sender_email', None, 'Sender email')
flags.DEFINE_string('email_pwd', None, 'Email password')
flags.DEFINE_string('dest_email', None, 'Destination email')
flags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'Job status.')

def check_flags():
    """Check if we have all params to run
    """
    if FLAGS.csv_path is None:
            print("No file path defined")
            return -1
    if FLAGS.sender_email is None:
        print("No sender email defined")
        return -1
    if FLAGS.email_pwd is None:
        print("No sender email password defined")
        return -1
    if FLAGS.dest_email is None:
        print("No destination email defined")
        return -1
    return 0

def main(argv):
    if check_flags() != 0:
        return -1

    account_info = trx_process.get_monthly_info(FLAGS.csv_path)

    if account_info == -1:
        return account_info

    emailInfo = EmailInfo(account_info, FLAGS.sender_email,
    FLAGS.email_pwd, FLAGS.dest_email)
    emailInfo.create_email_content()
    
if __name__ == '__main__':
  app.run(main)
