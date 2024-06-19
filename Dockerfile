
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip && \
pip install -r requirements.txt

COPY cas_tool/ ./cas_tool/

ENV PYTHONPATH "${PYTHONPATH}:/app/cas_tool/"
ENV PYTHONUNBUFFERED=1

CMD fastapi dev cas_tool/api/main.py --reload
