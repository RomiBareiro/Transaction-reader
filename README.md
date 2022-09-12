# Trx_reader

# Download docker container from DockerHub:
https://hub.docker.com/repository/docker/romibareiro/stori01

Or

# Clone repository and install:
<text>pip3 install -r requirements.txt</text>

# Load env variables:
Create an .env file with this content:

<code>
CSV_PATH=CSV_PATH
SENDER_EMAIL=SENDER_EMAIL
DEST_EMAIL=DEST_EMAIL
EMAIL_PWD=EMAIL_PWD
USER_NAME=USER_NAME
</code>

# And then run:
<code>python3  main.py
</code>

Note: if your email sender is a gmal account, you must get app password from gmail settings.
If you want to build the docker image, you need to change the flags values in .env ( PATH_TO_CSV, EMAIL_SENDER, EMAIL_DESTINATION,EMAIL_SENDER_PWD,USER_NAME)

# You will receive an email like this: 


![index](https://user-images.githubusercontent.com/100946603/189212924-1cd51e00-cfa7-4c53-8ebd-18bd6328c7e8.jpeg)
