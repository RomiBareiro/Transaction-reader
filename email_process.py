#!/usr/bin/env python3
import trx_process
from calendar import month_abbr
from email.message import EmailMessage
import smtplib

class  EmailInfo:
    def __init__(self, account_info, sender_email="", password="", dest_email="", subject ="[Stori] Your Balance Report"):
        self.account_info = account_info
        self.sender_email = sender_email
        self.password = password
        self.dest_email = dest_email
        self.subject = subject


    def total_balance(self):
        return ('Total balance: {} '.format(round(trx_process.get_total_balance(self.account_info),2)))
    
    def trx_number_month(self, month):
        return ('Number of trx in {}: {}\n'.format(month_abbr[month], self.account_info['trx_qtty'][month-1]))

    def average_debit_amount(self):
        return('Average debit amount: {} '.format(trx_process.get_average_amount(self.account_info, 'debit')))

    def average_credit_amount(self):
        return('Average credit amount: {} '.format(trx_process.get_average_amount(self.account_info, 'credit')))

    def create_email_content(self):
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.sender_email 
        msg['To'] = self.dest_email 
        balance_info = '''<h2 style="text-align:center;">{}</h2>
                         <div style="background-color:#81f463 ;"><h3>{}</h3><h3>{}</h3></div>'''.format(self.total_balance(), 
                        self.average_debit_amount(),
                        self.average_credit_amount())
        print("balance_info: ", balance_info)

        monthly_info = ''
        for i, elem in enumerate(self.account_info['trx_qtty']):
            if elem !=0:
               monthly_info += '''<h3>{}</h3>'''.format(self.trx_number_month(i+1))
        if monthly_info == '':
            monthly_info = "<h2>No registered transactions</h2>"
        monthly_info = '''<div style="background-color:#f463cd;">{}</div>'''.format(monthly_info)
        content = '''<!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#63f4f1;padding:10px 20px;">
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
        </html>'''.format(balance_info, monthly_info)
        print(content)
        msg.set_content(content, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender_email, self.password) 
            smtp.send_message(msg)