FROM arm64v8/python:3.6-buster

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# CMD ["python3", "bot.py"]
