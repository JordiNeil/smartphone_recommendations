FROM python:3.8

WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code/

ENV host=192.168.96.1
ENV dbname=smartphones
ENV password=654321
ENV user=postgres


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]