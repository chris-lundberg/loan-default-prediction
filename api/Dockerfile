# File name: Dockerfile
# FROM rayproject/ray:latest
FROM python:3.10

# Copy local files into container 
COPY . /serve_app

# Set the working dir for the container to /serve_app
WORKDIR /serve_app

RUN pip install -r requirements.txt

CMD ["serve run serve:loan_default_app"]