# syntax=docker/dockerfile:1
FROM python:3.10-alpine AS base

# Create install directories
RUN mkdir /install
WORKDIR /install

# Install python dependancies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --prefix=/install -r /requirements.txt

# Copy the binaries
# FROM base as runtime
FROM python:3.10-alpine AS runtime 
COPY --from=base /install /usr/local
WORKDIR /app

# Be able to configure the port on the image build
ENV APP_PORT=7711
ENV PYTHONUNBUFFERED=TRUE

# Copy the app
COPY app.py .

# Expose the port
EXPOSE $APP_PORT

# Need to specify path to gunicorn
RUN export PATH=$PATH:/usr/local/bin/gunicorn

# Run command
CMD ["gunicorn", "-b", "0.0.0.0:7711", "--timeout", "600", "--workers", "4", "app:app"]
