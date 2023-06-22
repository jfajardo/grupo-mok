FROM python:3.9

WORKDIR /flask_app

ARG DJANGO_API_URL
ENV DJANGO_API_URL ${DJANGO_API_URL}


COPY ./flask_app/requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN cd flask_app/
CMD [ "python3", "main.py"]
