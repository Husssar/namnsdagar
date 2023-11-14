FROM python:3.11-slim-buster
COPY requirements.txt requirements.txt
WORKDIR .
RUN echo "Timezone!!!!!"
ENV TZ=Europe/Stockholm
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install cryptography
CMD ["python", "app/main.py"]

