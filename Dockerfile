FROM python:3.9.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz


COPY poetry.lock /
COPY pyproject.toml .
RUN apt update && apt install -y python3-dev
RUN pip install poetry && poetry config virtualenvs.create false && poetry install
RUN pip install websocket_client

COPY . /code/

EXPOSE 8000
