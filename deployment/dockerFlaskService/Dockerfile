FROM python:3.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY main.py /app
COPY model.h5 /app
COPY templates /app/templates
COPY static/css /app/static/css
COPY static/js /app/static/js
CMD ["python", "main.py"]