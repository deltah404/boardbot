FROM python:3.9
COPY . ./
WORKDIR ./
RUN pip install python-decouple
RUN git clone https://github.com/Pycord-Development/pycord
RUN pip install -U pycord/.
RUN python3 main.py