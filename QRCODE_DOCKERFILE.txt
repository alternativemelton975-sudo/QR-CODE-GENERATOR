FROM python:3.11-slim AS builder

WORKDIR /build
COPY requirements-qrcode.txt requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY QrCodeGenerator.py .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "QrCodeGenerator.py"]
