FROM python:latest
RUN pip3 install pipreqs && pipreqs ./ && python3 -m pip install -r requirements.txt
RUN git clone https://github.com/Pycord-Development/pycord && pip3 install -U ./pycord
RUN python3 main.py