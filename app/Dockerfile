FROM python:3.7-buster
RUN mkdir src/
COPY requirements.txt src/
WORKDIR /src/
RUN pip install -r requirements.txt
ADD . /src/
CMD ["python", "manage.py", "migrate"]