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

def main(argv):
    if FLAGS.csv_path is None:
        print("No file path defined")
        return -1
    else:
        print("path: ", FLAGS.csv_path)
        account_info = trx_process.get_monthly_info(FLAGS.csv_path)

        if account_info == -1:
            return account_info

        emailInfo = EmailInfo(account_info, FLAGS.sender_email,
        FLAGS.email_pwd, FLAGS.dest_email)
        emailInfo.create_email_content()
    
if __name__ == '__main__':
  app.run(main)
