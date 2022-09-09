FROM python:latest

LABEL Maintainer="rominabareiro"

# Container working directory
WORKDIR /usr/app/src

# COPY files at working directory in container
COPY . ./

RUN python -m pip install --no-cache-dir --upgrade -r /usr/app/src/requirements.txt

CMD [ "python", "./main.py", "-csv_path=txns.csv", "-sender_email=EMAIL_SENDER", "-dest_email=EMAIL_DESTINATION","-email_pwd=EMAIL_PASSWORD", "-user_name=TESTING USER" ]