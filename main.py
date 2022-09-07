#!/usr/bin/env python3
from absl import app
from absl import flags
import trx_process
from  calendar import month_abbr
FLAGS = flags.FLAGS

# If there is a conflict, we'll get an error at import time.
flags.DEFINE_string('csv_path', 'txns.csv', 'CSV trx file path')
flags.DEFINE_integer('age', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')
flags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'Job status.')


def main(argv):
    '''if FLAGS.debug:
        print('non-flag arguments:', argv)
    '''
    if FLAGS.csv_path is None:
        print("No file path defined")
        return -1
    else:
        #TODO: CATCH ERRORS
        #TODO: Send email
        print("path: ", FLAGS.csv_path)
        monthly = trx_process.get_monthly_info(FLAGS.csv_path)
        print('Total balance: {} '.format(trx_process.get_total_balance(monthly)))
        print('Number of trx in {}: '.format(month_abbr[7]),monthly['trx_qtty'][7-1])
        print('Number of trx in {}: '.format(month_abbr[8]),monthly['trx_qtty'][8-1])
        print('Average debit amount: {} '.format(trx_process.get_average_amount(monthly, 'debit')))
        print('Average debit amount: {} '.format(trx_process.get_average_amount(monthly, 'credit')))
        print('Average XXX amount: {} '.format(trx_process.get_average_amount(monthly, 'XXx')))
    
if __name__ == '__main__':
  app.run(main)
