# Getting os and python official image from dockerhub
FROM python:3.9.13-buster

# Setting the working directory
WORKDIR /docker

# Copying the requirements.txt file to the container
COPY requirements.txt ./

# Installing the dependencies
RUN pip install -r requirements.txt

# Copying the rest of the application code to the working directory
COPY . .

# Exposing the port
CMD ["python3", "-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]