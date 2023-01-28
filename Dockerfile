FROM python:3.12.0a4-alpine3.17

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]