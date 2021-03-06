/**
 *
 * Copyright 2018 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

const {RawMessage,
       RawResponse} = require('./skillitor_pb.js');
const {SkillitorQueryClient} = require('./skillitor_grpc_web_pb.js');
const {EchoApp} = require('../echoapp.js');
const grpc = {};
grpc.web = require('grpc-web');

var echoService = new SkillitorQueryClient('http://'+window.location.hostname+':8080', null, null);

var echoApp = new EchoApp(
  echoService,
  {
    RawMessage: RawMessage,
    RawResponse: RawResponse
  },
  {
    checkGrpcStatusCode: function(status) {
      if (status.code != grpc.web.StatusCode.OK) {
        EchoApp.addRightMessage('Error code: '+status.code+' "'+
                                status.details+'"');
      }
    }
  }
);

echoApp.load();
