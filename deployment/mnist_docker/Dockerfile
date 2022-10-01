FROM python:3.6
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r ./requirements.txt
COPY mnist_prediction.py /app
COPY mnistModel.mdl /app
COPY templates /app/templates
CMD ["python", "mnist_prediction.py"]