FROM python:3.9-slim
COPY . /app
WORKDIR /app
EXPOSE 8501
RUN apt-get update && apt-get -y install gcc 
RUN pip3 install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
