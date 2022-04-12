FROM python:3.9.12

# Set environemnt variables
ENV KEY_VAULT_NAME=viz-wizard

# Install poetry
RUN pip3 install poetry

# Copy our Python requirements here and install using Poetry
COPY . /app
WORKDIR /app
RUN poetry config virtualenvs.create false
RUN poetry install

# Copy app code and run application
EXPOSE 8501
WORKDIR /app
CMD streamlit run ./main.py
