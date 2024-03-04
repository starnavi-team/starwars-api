#!/bin/sh

while !</dev/tcp/${POSTGRES_HOST}/${POSTGRES_PORT};
do
    echo waiting for Postgres to start...;
    sleep 3;
done;

python manage.py collectstatic --clear --noinput
python manage.py migrate
make load_data


if  [[ $RUN_TYPE == "production" ]]; then
    gunicorn swapi.wsgi:application --bind 0.0.0.0:8000 --workers $((2 * $(nproc) + 1))
elif [[ $RUN_TYPE == "development" ]]; then
    python manage.py runserver 0.0.0.0:8000;
fi