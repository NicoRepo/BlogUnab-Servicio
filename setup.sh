#!/bin/bash
pip install -r requirements.txt
apt-get update
apt-get -y install apache2
a2enmod proxy
a2enmod proxy_http
a2enmod ssl
rm /etc/apache2/sites-enabled/*
cp servicio.conf /etc/apache2/sites-enabled
rm oauth_settings.yml
cp oauth_settings_prod.yml oauth_settings.yml
python secret.py >> ~/.bashrc
