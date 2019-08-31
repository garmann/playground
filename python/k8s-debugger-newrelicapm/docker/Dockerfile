FROM alpine:3.7

RUN apk update
RUN apk add --update python3 py3-pip

COPY docker/requirements.txt /myapp/
RUN pip3 install -r /myapp/requirements.txt

COPY k8sdebug /myapp/k8sdebug/
COPY k8sdebug/newrelic.ini /myapp/
RUN chmod +x -R /myapp/

EXPOSE 8080
WORKDIR /myapp/
ENV NEW_RELIC_CONFIG_FILE newrelic.ini
ENV PYTHONUNBUFFERED=1
CMD ["newrelic-admin", "run-python", "k8sdebug/k8sdebug.py"]
