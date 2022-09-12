FROM python:latest

LABEL Maintainer="rominabareiro"

# Container working directory
WORKDIR /usr/app/src

# COPY files at working directory in container
COPY . ./

RUN python -m pip install --no-cache-dir --upgrade -r /usr/app/src/requirements.txt

ENTRYPOINT [ "python", "main.py"]
