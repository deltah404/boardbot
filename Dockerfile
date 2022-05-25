FROM python:latest

RUN pip3 freeze > requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install python-gist

RUN pip3 install numpy

RUN git clone https://github.com/Pycord-Development/pycord && pip3 install -U ./pycord

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python3", "./main.py" ]
