FROM python:3.9-alpine3.13
LABEL maintainer="smartquail.io"

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git
ARG username=smartquailDev
ARG password=ms1719183830
RUN git clone https://github.com/smartquailDev/qnode1.0_app.git

#COPY . /qnode0_app
#COPY ./qnode0_app.dev/qnode0_app_env_dev/qnode0_app/ /qnode0_app
COPY ./scripts /scripts
#COPY ./.env /qnode10_app/.env 
#No olvidar sacar las variables de entorno.
COPY ./requirements.txt /requirements.txt




WORKDIR /qnode1.0_app/qnode10_app/
EXPOSE 8000 443 
EXPOSE 25


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps && \
    apk add build-base  postgresql-dev gcc musl-dev python3-dev linux-headers && \
    apk add libffi-dev build-base py3-cffi py3-cryptography && \
    apk add jpeg-dev   zlib-dev libjpeg build-base  wget  && \
    apk del libressl-dev && \
    apk add busybox-extras && \
     apk add gtk+3.0 pango && \
    apk add openssl-dev && \
    #/py/bin/pip install  rust  &&  \
    #/py/bin/pip install   py3-kiwisolver &&  \
    /py/bin/pip install -r /requirements.txt && \
    apk del openssl-dev  &&  \
    apk add libressl-dev  && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home qnode10 && \
    
    mkdir -p /qnode1.0_app/qnode10_app/static && \
   # mkdir -p /qnode0.0_app/qnode0_app/static/media && \
    chmod -R 755 /qnode1.0_app/qnode10_app/static  && \

    mkdir -p /qnode1.0_app/qnode10_app/media && \
    chmod -R 755 /qnode1.0_app/qnode10_app/media  && \
    chown -R qnode10:qnode10 /qnode1.0_app/qnode10_app/media && \
    
    mkdir -p /qnode1.0_app/qnode10_app/staticfiles && \
    chmod -R 755 /qnode1.0_app/qnode10_app/staticfiles  && \
    chown -R qnode10:qnode10 /qnode1.0_app/qnode10_app/staticfiles && \

    #chmod -R 755 /qnode0.0_app/qnode0_app/static/media  && \
    chown -R qnode10:qnode10 /qnode1.0_app/qnode10_app/static && \
    #chown -R qnode0:qnode0 /qnode0.0_app/qnode0_app/static/media && \

    mkdir -p /qnode1.0_app/qnode10_app/run/ && \
    mkdir -p /var/log/gunicorn &&\
    chown -R qnode10:qnode10 /var/log/gunicorn &&\
    
    chmod -R 755 /qnode1.0_app/qnode10_app/ && \
    
    chmod -R 755 /scripts  && \
    chown -R qnode10:qnode10 /qnode1.0_app/qnode10_app/run/  && \
    chmod -R 755 /var/log/gunicorn  && \
    
    chmod -R u+x /scripts/gunicorn_run.sh &&\
    chmod -R u+x /scripts/run.sh &&\
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER qnode10

CMD ["run.sh"]
