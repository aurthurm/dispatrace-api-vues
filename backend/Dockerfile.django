FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend/
RUN chmod +x ./startup.sh
CMD ["/bin/bash", "./startup.sh" ]
