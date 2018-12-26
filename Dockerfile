FROM python:3.6-slim
MAINTAINER "Kaio Aresi"

ENV PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo

WORKDIR /usr/src/app

COPY teste_vars.py ./

ENTRYPOINT [ "python3","-u","./teste_vars.py" ]
