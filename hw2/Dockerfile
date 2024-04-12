FROM python:3.12

RUN pip install pipenv && pipenv install

COPY hw.py /app/hw.py

WORKDIR /app

ENTRYPOINT ["pipenv", "run", "python", "hw.py"]