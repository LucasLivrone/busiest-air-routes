FROM python:3.10
WORKDIR /app
COPY ./app /app
COPY requirements.txt /
RUN pip install -r /requirements.txt
ENV PYTHONPATH /
CMD ["python", "api/main.py"]