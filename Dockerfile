FROM python:3.8

RUN pip3 install pipreqs && pipreqs ./

RUN pip install -r requirements.txt

RUN git clone https://github.com/Pycord-Development/pycord && pip3 install -U ./pycord

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python3", "./main.py" ]
