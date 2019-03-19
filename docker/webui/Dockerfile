# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM node:8-stretch

ARG EXAMPLE_DIR=/src/skillitor/core/api

RUN apt-get -qq update && apt-get -qq install -y \
  unzip \
  curl

COPY src /src

RUN curl -sSL https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/\
protoc-3.6.1-linux-x86_64.zip -o /tmp/protoc.zip && \
  cd /tmp && \
  unzip -qq protoc.zip && \
  cp /tmp/bin/protoc /usr/local/bin/protoc

RUN curl -sSL https://github.com/grpc/grpc-web/releases/download/1.0.3/\
protoc-gen-grpc-web-1.0.3-linux-x86_64 -o /usr/local/bin/protoc-gen-grpc-web && \
  chmod +x /usr/local/bin/protoc-gen-grpc-web

RUN mkdir -p /var/www/html/dist
RUN protoc -I=$EXAMPLE_DIR skillitor.proto \
--js_out=import_style=commonjs:\
$EXAMPLE_DIR/commonjs-example \
--grpc-web_out=import_style=commonjs,mode=grpcwebtext:\
$EXAMPLE_DIR/commonjs-example

RUN cd $EXAMPLE_DIR/commonjs-example && \
  npm install && \
  npx webpack && \
  cp echotest.html /var/www/html && \
  cp dist/main.js /var/www/html/dist

EXPOSE 8081
WORKDIR /var/www/html
CMD ["python", "-m", "SimpleHTTPServer", "8081"]
