FROM python:3.6-alpine

LABEL Name=open-dataverse Version=0.0.1
EXPOSE 9898

WORKDIR /app
ADD . /app

# Using pip:
# RUN python3 -m pip install -r requirements.txt
# CMD ["python3", "-m", "open-dataverse"]

# Using pipenv:
RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile
CMD ["pipenv", "run", "python3", "-m", "open-dataverse"]