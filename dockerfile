FROM php:8.0-apache

RUN apt-get update && \
    apt-get install -y \
        libzip-dev \
        unzip \
        && \
    a2enmod rewrite && \
    service apache2 restart

WORKDIR /var/www/html

#copy code to var/www/html
COPY ./src ./

EXPOSE 80
