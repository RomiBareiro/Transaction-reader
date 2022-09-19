#!/usr/bin/env python3
from src import trx_process
from calendar import month_abbr
from email.message import EmailMessage
import smtplib
import logging 

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)

class  EmailInfo:
    def __init__(self, account_info, sender_email="", password="", 
                 dest_email="", user=None,subject ="[Stori] Your Balance Report"):
        self.account_info = account_info
        self.sender_email = sender_email
        self.password = password
        self.dest_email = dest_email
        self.subject = subject
        self.user = user
        self.msg = EmailMessage()
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.sender_email 
        self.msg['To'] = self.dest_email 

    def total_balance(self):
        return ('Total balance: $ {} '.format(round(trx_process.get_total_balance(self.account_info),2)))
    
    def trx_number_month(self, month):
        return ('Number of trx in {}: {}\n'.format(month_abbr[month], self.account_info['trx_qtty'][month-1]))

    def average_debit_amount(self):
        return('Average debit amount: $ {} '.format(trx_process.get_average_amount(self.account_info, 'debit')))

    def average_credit_amount(self):
        return('Average credit amount: $ {} '.format(trx_process.get_average_amount(self.account_info, 'credit')))
    
    def hello_user(self):
        return "Hi {}!, here is your monthly account information ".format(self.user)

    def create_email_content(self):
        balance_info = self.format_balance_info(self.total_balance(), 
                        self.average_debit_amount(),
                        self.average_credit_amount())

        monthly_info = self.format_monthly_info(self.account_info['trx_qtty'])

        content = self.create_content(balance_info, monthly_info)
        logging.debug(content)
        self.msg.set_content(content, subtype='html')


    def format_balance_info(self, total_balance,average_debit_amount, average_credit_amount):
        return '''<h2 style="text-align:center;">{}</h2>
                            <div style="background-color:#81f463 ;"><h3>{}</h3><h3>{}</h3></div>'''.format(total_balance, 
                            average_debit_amount,
                            average_credit_amount)

    def format_monthly_info(self, trx_qtty):
        monthly_info = ''
        for i, elem in enumerate(trx_qtty):
            if elem !=0:
                monthly_info += '''<h3>{}</h3>'''.format(self.trx_number_month(i+1))
        if monthly_info == '':
            monthly_info = "<h2>No registered transactions</h2>"
        return '''<div style="background-color:#f463cd;">{}</div>'''.format(monthly_info)

    def create_content(self, balance, monthly_info):
        return '''<!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#63f4f1;padding:10px 20px;">
                <h2>{}
                </h2>
                  <div style="text-align:center;">
                    <h1 style="font-family:Georgia, 'Times New Roman', Times, serif;color:white;">Balance Information</h1>
                  </div>
                </div>
                {}{}
                <div style="padding:20px 0px">
                     <div style="height: 500px;width:400px">
                      <div style="text-align:center;">
                        <img src="https://s4-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/579/700/resized/LogoStori-azul_Horizontal_-_Copy_(2).png?1634748560">                            
                      </div>
                    </div>
                </div>
            </body>
        </html>'''.format(self.hello_user(), balance, monthly_info)
    
    def send_email(self):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.sender_email, self.password) 
                smtp.send_message(self.msg)
        except:
            logging.critical("Email couldn't be sent")
            return -1
