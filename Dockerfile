FROM python:3.8

RUN pip3 install pipenv
COPY Pipfile /usr/src/
WORKDIR /usr/src
COPY requirements.txt .
RUN pipenv lock --requirements > requirements.txt
RUN pip3 install -r requirements.txt
COPY configuration/* .
COPY modules/* .
COPY robbinsvault.py .
CMD ["python3", "robbinsvault.py"]