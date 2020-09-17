FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY ./django/requirements.txt /backend/
RUN pip install -r requirements.txt
COPY ./django /backend/
RUN chmod +x ./startup.sh
CMD ["/bin/bash", "./startup.sh" ]
