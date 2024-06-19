FROM python:3.12-slim

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /cas_tool
COPY *.py /cas_tool/
WORKDIR /cas_tool
CMD fastapi dev cas_tool/api/main.py --host=0.0.0.0 --port=80