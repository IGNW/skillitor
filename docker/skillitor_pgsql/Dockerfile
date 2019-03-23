ARG PYTHON_VERSION=3.7.2-alpine
FROM python:${PYTHON_VERSION} as builder
RUN apk add --update --no-cache \
    gcc \
    libstdc++ \
    linux-headers \
    make \
    musl-dev \
    postgresql-dev \
    python-dev \
    g++
WORKDIR /wheels
COPY src/requirements.txt /wheels/requirements.txt
RUN pip install -U pip && \
    pip wheel --requirement requirements.txt

FROM python:${PYTHON_VERSION}
ENV PYTHONPATH /app
ENV APP_HOME /app
ENV PYTHONUNBUFFERED 1
COPY --from=builder /wheels /wheels
RUN pip install -U pip && \
    pip install -r /wheels/requirements.txt -f /wheels && \
    rm -rf /wheels && \
    rm -rf /root/.cache/pip/* && \
    apk add --no-cache libstdc++ libpq
COPY src /app
WORKDIR /app
RUN /app/grpc_generate.sh
EXPOSE 50051
CMD ["python3", "/app/postgres_db_service.py"]
