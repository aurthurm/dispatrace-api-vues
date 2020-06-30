FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
RUN chmod +x startup.sh
#CMD [ "./startup.sh" ]