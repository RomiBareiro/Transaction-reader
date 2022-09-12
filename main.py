#!/usr/bin/env python3
import os
from datetime import  datetime
import logging
from email_process import EmailInfo
from register import insert_historic_balance
import trx_process
from envparse import env
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)

def main():
    if os.path.isfile('.env'):
        env.read_envfile()

    CSV_PATH = os.getenv('CSV_PATH')
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    EMAIL_PWD = os.getenv('EMAIL_PWD')
    DEST_EMAIL = os.getenv('DEST_EMAIL')
    USER_NAME = os.getenv('USER_NAME')
    account_info = {'user_name':USER_NAME}

    transactions = trx_process.get_monthly_info(CSV_PATH)
    if transactions == -1:
        return -1

    account_info.update(transactions)
    emailInfo = EmailInfo(account_info, SENDER_EMAIL,
    EMAIL_PWD,DEST_EMAIL, USER_NAME)
    if emailInfo.create_email_content() == -1:
        return -1
    
    account_info['email_date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if insert_historic_balance(account_info) == None:
        logging.error("Email information couldn't be saved")
        return -1
    
if __name__ == '__main__':
  main()