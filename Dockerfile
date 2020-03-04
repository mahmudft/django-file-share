FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_ENV=debug
RUN mkdir /filesharing
WORKDIR /filesharing
COPY requirements.txt /filesharing/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /filesharing
EXPOSE 8080
