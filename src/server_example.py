#!/usr/bin/env python3
from concurrent import futures
import grpc
import time

from skillitor.core.api import skillitor_pb2, skillitor_pb2_grpc


class SkillitorQueryHandler(skillitor_pb2_grpc.SkillitorQueryServicer):
    def SetSkill(self, request, context):
        print("Got a request to SetSkill. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.Acknowledgement(success=True)

    def UnsetSkill(self, request, context):
        print("Got a request to UnsetSkill. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.Acknowledgement(success=True)

    def FindSkill(self, request, context):
        print("Got a request to FindSkill. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.Acknowledgement(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    skillitor_pb2_grpc.add_SkillitorQueryServicer_to_server(
        SkillitorQueryHandler(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Listening on port 50051")

    # The server code above runs asynchronously, so we need to do a sleep loop
    # to avoid exiting.
    while True:
        time.sleep(10)
        # Time passes. If only we had something useful to do.


if __name__ == '__main__':
    serve()
