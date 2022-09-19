#!/usr/bin/env python3
import os
from datetime import  datetime
import logging
from src import save_in_cluster, EmailInfo, trx_process
from envparse import env

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)
class Environment:
    def __init__( self,CSV_PATH, SENDER_EMAIL,EMAIL_PWD, DEST_EMAIL, USER_NAME, MONGODB_CONNSTRING ):
        self.csv_path = CSV_PATH
        self.sender_email = SENDER_EMAIL
        self.email_pwd = EMAIL_PWD
        self.dest_email = DEST_EMAIL
        self.user_name = USER_NAME
        self.mongo_conn = MONGODB_CONNSTRING

def main():
    if os.path.isfile('.env') is False:
        logging.error(".env file not found")
        return -1
        
    env.read_envfile()
    envir = check_flags() 

    if envir == -1:
        logging.error("Couldn't read flags")
        return -1

    account_info = {'user_name':envir.user_name}

    file_handler = trx_process.get_csv_file(envir.csv_path)
    if file_handler == -1:
        return -1

    transactions = trx_process.get_monthly_info(file_handler)
    if transactions == -1:
        return -1

    account_info.update(transactions)
    emailInfo = EmailInfo(account_info, envir.sender_email,
    envir.email_pwd,envir.dest_email, envir.user_name)

    emailInfo.create_email_content() 

    if emailInfo.send_email() == -1:
        return -1

    account_info['email_date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if save_in_cluster(account_info, envir.mongo_conn) == None:
        logging.error("Email information couldn't be saved")
        return -1

def check_flags():
    """Check .env flags
    """
    CSV_PATH = os.getenv('CSV_PATH')
    if CSV_PATH is None:
        logging.error("CSV_PATH is empty")
        return -1
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    if SENDER_EMAIL is None:
        logging.error("SENDER_EMAIL is empty")
        return -1
    EMAIL_PWD = os.getenv('EMAIL_PWD')
    if EMAIL_PWD is None:
        logging.error("EMAIL_PWD is empty")
        return -1
    DEST_EMAIL = os.getenv('DEST_EMAIL')
    if DEST_EMAIL is None:
        logging.error("DEST_EMAIL is empty")
        return -1
    USER_NAME = os.getenv('USER_NAME')
    if USER_NAME is None:
        logging.error("USER_NAME is empty")
        return -1
    MONGODB_CONNSTRING = os.getenv('MONGODB_CONNSTRING')
    if MONGODB_CONNSTRING is None:
        logging.error("MONGODB_CONNSTRING is empty")
        return -1
    return Environment(CSV_PATH, SENDER_EMAIL,EMAIL_PWD, DEST_EMAIL, USER_NAME, MONGODB_CONNSTRING)

if __name__ == '__main__':
    main()
