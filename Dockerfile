FROM ubuntu:latest
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python-is-python3 \
    gfortran \
    liblapack-dev \
    liblapacke-dev \
    python3-pip

RUN python -m pip install -r requirements.txt
CMD python ./scripts.py