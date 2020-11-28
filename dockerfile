from python:3.7

ENV DJANGO_SETTINGS_MODULE NoticiasUnab.production

ENV PYTHONUNBUFFERED 1

RUN mkdir NoticiasUnab

WORKDIR /NoticiasUnab

ADD . /NoticiasUnab

RUN ./setup.sh

ENTRYPOINT ["./start.sh"]

EXPOSE 80