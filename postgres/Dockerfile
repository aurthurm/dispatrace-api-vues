FROM postgres
RUN apt-get update && apt-get install -y dos2unix
COPY . .
RUN dos2unix ./postgres_init.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
RUN chmod +x ./postgres_init.sh
CMD [ "./postgres_init.sh" ]