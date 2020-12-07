from python:3.7

ENV DJANGO_SETTINGS_MODULE NoticiasUnab.production

ENV PYTHONUNBUFFERED 1

RUN mkdir BlogUnab-Servicio

WORKDIR /BlogUnab-Servicio

ADD . /BlogUnab-Servicio

RUN ./setup.sh

ENTRYPOINT ["./start.sh"]

EXPOSE 80