#!/usr/bin/env bash
# Generates files in skillitor/api/
# Assumes that the grpcio-tools pip package is istalled

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. skillitor/core/api/skillitor.proto
