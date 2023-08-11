FROM python:3.8-slim
COPY . /app/chatterbot
COPY tagging.py /app/chatterbot/chatterbot/tagging.py


WORKDIR /app/chatterbot

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python dependencies
COPY requirements.pip /app/chatterbot/
RUN pip install --no-cache-dir --upgrade --use-pep517 -r requirements.pip

RUN python3 -m spacy download en_core_web_sm

EXPOSE 5000

CMD [ "python3","chatbot.py" ]
