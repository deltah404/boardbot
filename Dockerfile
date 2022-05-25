FROM python:3.10.4

RUN pip3 freeze > requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install python-gist

RUN pip3 install python-decouple

RUN pip3 install python-dotenv

RUN git clone https://github.com/Pycord-Development/pycord && pip3 install -U ./pycord

COPY . .

EXPOSE 1337

USER 1000

RUN python3 main.py