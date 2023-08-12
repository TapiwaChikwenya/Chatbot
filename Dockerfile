FROM python:3.8-slim
FROM python:3.8-slim
COPY . /app/chatterbot
COPY tagging.py /app/chatterbot/chatterbot/tagging.py


WORKDIR /app/chatterbot

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran


RUN pip install --no-cache-dir --upgrade pip
RUN pip install --upgrade setuptools wheel
RUN pip install --use-pep517 numpy
RUN pip install  pyyaml==5.1.2

RUN pip install chatterbot

RUN   pip install chatterbot_corpus

RUN pip install flask

#RUN pip install spacy

RUN python3 -m spacy download en_core_web_sm

CMD [ "python3","chatbot.py" ]



EXPOSE 1032