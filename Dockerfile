FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y wget curl gnupg && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m playwright install --with-deps

CMD ["python", "bot/loopdrop_bot.py"]