FROM postgres:latest
RUN apt-get update && apt-get install -y dos2unix
COPY . .
#RUN dos2unix ./postgres_init.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
RUN sed -i -e 's/\r$//' postgres_init.sh
RUN chmod +x postgres_init.sh
CMD ["/bin/bash", "./postgres_init.sh" ]