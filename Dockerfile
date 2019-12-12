FROM python:3.7.5

ADD . .

RUN pip install --upgrade pip

CMD ["python", "-m", "unittest", "discover", "-s","Tests"]
