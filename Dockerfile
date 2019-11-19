FROM python:3.6-alpine

LABEL Name=open-dataverse Version=1.0.0
EXPOSE 4000

WORKDIR /usr/src/app
ADD . /usr/src/app

# Using pip:
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "run.py"]

# Using pipenv:
# RUN python3 -m pip install pipenv
# RUN pipenv install --ignore-pipfile
# CMD ["pipenv", "run", "python3","run.py"]