#!/usr/bin/env bash
ENV=${ENV:-API}
PROCESSES=${PROCESSES:-8}

if  [ $ENV == "STATIC" ]; then
    echo "start nginx on port 80"
    nginx -g "daemon off;"
    exit 0
fi

python manage.py migrate

uwsgi --chdir=/code \
      --module=config.wsgi:application \
      --master \
      --processes $PROCESSES \
      --reload-mercy 10 \
      --worker-reload-mercy 10 \
      --enable-threads \
      --disable-logging \
      --vacuum \
      --single-interpreter \
      --http-keepalive \
      --post-buffering 32768 \
      --http=0.0.0.0:8000 \
      --stats 0.0.0.0:8001 \
      --harakiri-verbose \
      --harakiri=10
