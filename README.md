# Transaction reader

## Brief intro
- This app read a .csv file that contains trx information, send a formatted email with this content and load the information into a Mongodb cluster.
- Info will be stored this way (in a json file) : 
</br> <code>{"_id":{"$oid":"631f4bdfb01fc30b3d3345ae"},"user_name":"TESTING","trx_qtty":[0,0,0,0,0,0,2,2,0,0,0,0],"debit":[0,0,0,0,0,0,-10.3,-20.46,0,0,0,0],"credit":[0,0,0,0,0,0,60.5,10.0,0,0,0,0],"email_date":"12/09/2022 15:10:23"}
</code>

## Tech
- Mongodb 
- Docker
- Docker compose
- Python 3.8.10

# Download docker container from DockerHub:
https://hub.docker.com/repository/docker/romibareiro/stori01

Or

## Clone repository and install:
<code>pip3 install -r requirements.txt</code>

## Load env variables:
Create an .env file with this content:

```sh
CSV_PATH=CSV_PATH
SENDER_EMAIL=SENDER_EMAIL
DEST_EMAIL=DEST_EMAIL
EMAIL_PWD=EMAIL_PWD
USER_NAME=USER_NAME
MONGODB_CONNSTRING=MONGODB_CONNSTRING
```

## And then run:
<code>python3  main.py
</code>


Note: if your email sender is a gmal account, you must get app password from gmail settings.
If you want to build the docker image, you need to change the flags values in .env ( PATH_TO_CSV, EMAIL_SENDER, EMAIL_DESTINATION,EMAIL_SENDER_PWD,USER_NAME)

## You will receive an email like this: 


![image](https://user-images.githubusercontent.com/100946603/194079425-a45a3e33-2d02-4a83-8420-c7f5ab72a80e.png)

