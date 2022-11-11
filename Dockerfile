FROM python:3.7

RUN apt-get update -y && \
    apt-get install -y python3-pip

RUN pip3 install pip --upgrade
RUN pip3 install --no-cache-dir loguru

ENV APP /genLog
WORKDIR $APP
RUN mkdir log
COPY ./main.py .
CMD ["python3","main.py"]