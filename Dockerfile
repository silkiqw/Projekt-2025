FROM python:3

 WORKDIR /usr/src/app

COPY hello_world.py .

CMD ["python", "./hello_world.py"]
