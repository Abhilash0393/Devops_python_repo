From python:3.12-alpine

COPY ./src /src
COPY ./requirements.txt /src
RUN pip install -r /src/requirments.txt

CMD python /src/app.py
