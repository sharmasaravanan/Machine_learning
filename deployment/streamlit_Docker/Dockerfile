FROM python:3.6
WORKDIR /app
EXPOSE 3000
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY streamliteApp.py /app
COPY LogisticRegressionModel.pickel /app
COPY vector.pickel /app
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["streamliteApp.py"]