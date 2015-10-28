FROM ubuntu
MAINTAINER klas@vionlabs.com

RUN apt-get update && apt-get install -y gcc libffi-dev python python-dev python-setuptools python-pip
RUN pip install j2cli
ADD ./setup.py /setup.py
RUN python /setup.py install

ADD ./docker-templates /docker-templates
ADD ./docker-entrypoint.sh /docker-entrypoint.sh

ADD . /code
WORKDIR /code

ENV value "hello world"

# EXPOSE 8080

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "code.py"]