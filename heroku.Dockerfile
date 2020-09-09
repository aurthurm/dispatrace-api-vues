FROM node:12 as frontend
COPY . /app
WORKDIR /app
RUN cd frontend && yarn install && yarn build

FROM python:3.8-slim
WORKDIR /app
RUN groupadd --gid 10001 app && useradd -g app --uid 10001 --shell /usr/sbin/nologin app
RUN chown app:app /tmp
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    gcc apt-transport-https python-dev \
    build-essential libpq-dev
COPY ./backend/requirements.txt /app/backend/requirements.txt
RUN pip install --upgrade --no-cache-dir -r backend/requirements.txt

COPY . /app
COPY --from=frontend /app/frontend/dist /app/frontend/dist
RUN chmod +x /app/backend/startup.sh

USER app

ENV PORT=8000
EXPOSE $PORT

CMD gunicorn backend/dispatrace.wsgi:application --host 0.0.0.0 --port $PORT