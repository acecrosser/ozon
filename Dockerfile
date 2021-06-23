FROM python
LABEL maintainer="Shilke Alex acecrosser@yandex.ru"
RUN apt-get update
RUN apt-get install -y supervisor
RUN mkdir -p /home/short
COPY . /home/short/app
ADD  supervisor.conf /etc/supervisor/conf.d/supervisor.conf
ADD .env /home/short/app/.env
ADD requirements.txt /home/short/app/requirements.txt
RUN pip install -r /home/short/app/requirements.txt
WORKDIR /home/short/app
EXPOSE 8000
CMD ["/usr/bin/supervisord"]