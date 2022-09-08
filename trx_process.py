#!/usr/bin/env python3

from  calendar import month_abbr

fields = {'Id':0, 'Date':1, 'Trx':2}
date = {'Month':0,'Day':1}
trx_results = ('trx_qtty','debit','credit')

def get_monthly_info(file_name):
    """Returns trx information of every month in a dictionary
       Arguments:
       file_name : Path to CSV file
    """
    try:
        with open(file_name) as file:
            columns = file.readline().split(',')
            print("columns: ", columns)
            trx_qtty , debit_amount, credit_amount= [0]*12, [0]*12, [0]*12
            rows = file.readlines()
            for elem in rows:
                req_month = int(elem.split(',')[fields['Date']].split('/')[date['Month']])
                trx_qtty[req_month-1] +=1
                trx_value = float(elem.split(',')[fields['Trx']].replace("\n",""))
                
                if trx_value < 0.0:
                    debit_amount[req_month-1] += trx_value
                else:
                    credit_amount[req_month-1] += trx_value
            month_trx = dict(zip(trx_results,[ trx_qtty, debit_amount, credit_amount]))
            print(month_trx)
            return month_trx

    except EnvironmentError:
         print("File could'nt be opened")
         return -1

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
    #Testing porpouses
    account_info = get_monthly_info("txns.csv")
    print('Total balance: {} '.format(get_total_balance(account_info)))
    print('Number of trx in {}: '.format(month_abbr[7]),account_info['trx_qtty'][7-1])
    print('Number of trx in {}: '.format(month_abbr[8]),account_info['trx_qtty'][8-1])
    print('Average debit amount: {} '.format(get_average_amount(account_info, 'debit')))
    print('Average debit amount: {} '.format(get_average_amount(account_info, 'credit')))
    print('Average XXX amount: {} '.format(get_average_amount(account_info, 'XXx')))

