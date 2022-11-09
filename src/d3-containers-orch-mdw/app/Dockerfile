# use the official lightweight python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# allow statements and log messages to immediately appear in the knative logs.
ENV PYTHONUNBUFFERED True

# copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# run the web service on container startup. here we use the gunicorn
# webserver, with one worker process and 8 threads.
# for environments with multiple cpu cores, increase the number of workers
# to be equal to the cores available.
# timeout is set to 0 to disable the timeouts of the workers to allow cloud run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app