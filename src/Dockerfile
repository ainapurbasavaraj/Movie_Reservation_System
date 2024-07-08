FROM rockylinux:9.3
RUN yum -y update && \
    yum -y install python3 epel-release python3-pip python-devel postgresql-devel

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./ /app
ENV PYTHONPATH "/app"

CMD [ "python3","/app/ApiInterface/app.py" ]