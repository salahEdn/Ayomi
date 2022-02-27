FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python3","manage.py","--bind","runserver","0.0.0.0:8000","ayomi_profil.wsgi"]
