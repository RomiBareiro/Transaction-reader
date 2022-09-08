from email.message import EmailMessage
import smtplib
import ssl
msg = EmailMessage()
msg['Subject'] = 'Here is my newsletter'
msg['From'] = "bareiro.romina@gmail.com" 
msg['To'] = "bareiro.romina@gmail.com" 
msg.set_content('''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:MediumSeaGreen;padding:10px 20px;">
                  <div style="text-align:center;">
                    <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">Your account balance</h2>
                    </div>
                </div>
                <div style="padding:20px 0px">
                    <div style="height: 500px;width:400px">
                      <div style="text-align:center;">
                        <img src="https://s4-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/579/700/resized/LogoStori-azul_Horizontal_-_Copy_(2).png?1634748560">                            
                    </div>
                    </div>
                </div>
            </body>
        </html>
        ''', subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("bareiro.romina@gmail.com" , 'cznsiinftbxmozql') 
    smtp.send_message(msg)
