FROM python:3.9

WORKDIR /src
COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

CMD python3 main.py
