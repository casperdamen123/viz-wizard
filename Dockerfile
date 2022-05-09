FROM ubuntu:20.04
COPY . /app
WORKDIR /app
EXPOSE 8501
RUN apt-get update \
    && apt-get -y install python3-pip python3-dev unixodbc-dev 
RUN apt-get update \
    && apt-get install -y gnupg curl sudo lsb-release \
    && apt-get clean all
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN echo 'export PATH="$PATH:/opt/mssql-tools17/bin"' >> ~/.bashrc
RUN . ~/.bashrc
RUN pip3 install -r requirements.txt 
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]