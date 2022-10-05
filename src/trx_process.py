#!/usr/bin/env python3
import logging
from  calendar import month_abbr

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)

fields = {'Id':0, 'Date':1, 'Trx':2}
date = {'Month':0,'Day':1}
trx_results = ('trx_qtty','debit','credit')

def get_csv_file(file_name):
    file =  open(file_name)
    if file is None:
        logging.error("File couldn't be opened")
        return -1
    return file

def get_monthly_info(file_handler):
    """Returns trx information of every month in a dictionary
       Arguments:
       file_name : Path to CSV file
    """
    columns = file_handler.readline().split(',')
    trx_qtty , debit_amount, credit_amount= [0]*12, [0]*12, [0]*12
    rows = file_handler.readlines()
    for elem in rows:
        req_month = int(elem.split(',')[fields['Date']].split('/')[date['Month']])
        trx_qtty[req_month-1] +=1
        trx_value = float(elem.split(',')[fields['Trx']].replace("\n",""))

        if trx_value < 0.0:
            debit_amount[req_month-1] += trx_value
        else:
            credit_amount[req_month-1] += trx_value
    month_trx = dict(zip(trx_results,[ trx_qtty, debit_amount, credit_amount]))
    logging.debug(month_trx)
    file_handler.close()
    return month_trx


def get_total_balance(account_info):
    """Get total account balance
    """
    return sum(account_info['debit']) + sum(account_info['credit'])

def get_total_type_trx(account_info, trx_type):
    """ Get count  of credit or debit trx
    Arg:
    account_info : trx information
    trx_type : credit or debit
    """
    if trx_type != 'debit' and trx_type != 'credit':
        return "Trx not allowed"
    count = 0
    for elem in  account_info[trx_type]:
        if elem != 0:
            count+=1
    return count


def get_average_amount(account_info, trx_type):
    """ Get average amount of credit or debit trx
    Arg:
    account_info : trx information
    trx_type : credit or debit
    """
    if trx_type != 'debit' and trx_type != 'credit':
        return "Trx not allowed"
    total_type_trx = get_total_type_trx(account_info,trx_type)
    return(sum(account_info[trx_type])/total_type_trx)

if __name__== "__main__":
    account_info = get_monthly_info("txns.csv")
    logging.debug('Total balance: {} '.format(get_total_balance(account_info)))
    logging.debug('Number of trx in {}:'.format(month_abbr[7]),account_info['trx_qtty'][7-1])
    logging.debug('Number of trx in {}:'.format(month_abbr[8]),account_info['trx_qtty'][8-1])
    logging.debug('Average debit amount: {} '.format(get_average_amount(account_info, 'debit')))
    logging.debug('Average debit amount: {} '.format(get_average_amount(account_info, 'credit')))
    logging.debug('Average XXX amount: {} '.format(get_average_amount(account_info, 'XXx')))
