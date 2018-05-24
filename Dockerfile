# pull pre-built docker image
FROM centos/python-36-centos7:latest
USER root

# create app dir & copy project folder
ADD . /var/www/refrigerator/

# install python3.6 packages which not included in image
WORKDIR /var/www/refrigerator
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose port
EXPOSE 8000
