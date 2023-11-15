FROM python:3.11-slim-buster
WORKDIR namesday/

ENV TZ=Europe/Stockholm
COPY . namesday/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r namesday/requirements.txt
RUN pip install cryptography
CMD ["python", "namesday/app/main.py"]

